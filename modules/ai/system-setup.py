#!/usr/bin/env python3

import sys
import os
from subprocess import Popen, PIPE
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../deps/readies"))
import paella

#----------------------------------------------------------------------------------------------

class RedisAISetup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)
        if self.osnick == 'xenial' or self.osnick == 'trusty':
            exit(0)

    def common_first(self):
        self.install_downloaders()
        self.setup_pip()
        self.pip_install("wheel virtualenv")
        self.pip_install("setuptools --upgrade")

        if self.os == 'linux':
            self.install("ca-certificates")
        self.install("git cmake unzip wget patchelf")
        self.install("coreutils") # for realpath

    def debian_compat(self):
        self.install("build-essential")
        self.install("python3-venv python3-psutil python3-networkx python3-numpy") # python3-skimage
        self.install_git_lfs_on_linux()

    def redhat_compat(self):
        self.group_install("'Development Tools'")
        self.install("redhat-lsb-core")

        if not self.dist == "amzn":
            self.install("epel-release")
            self.install("python36 python36-pip")
            self.install("python36-psutil")
        else:
            self.run("amazon-linux-extras install epel", output_on_error=True)
            self.install("python3 python3-devel")
            self.pip_install("psutil")

        self.install_git_lfs_on_linux()

    def fedora(self):
        self.group_install("'Development Tools'")
        self.install("python3-venv python3-psutil python3-networkx")
        self.install_git_lfs_on_linux()

    def macosx(self):
        p = Popen('xcode-select -p', stdout=PIPE, close_fds=True, shell=True)
        out, _ = p.communicate()
        if out.splitlines() == []:
            fatal("Xcode tools are not installed. Please run xcode-select --install.")

        self.install_gnu_utils()
        self.install("git-lfs")
        self.install("redis")

    def common_last(self):
        # redis-py-cluster should be installed from git due to redis-py dependency
        self.pip_install("--no-cache-dir git+https://github.com/Grokzen/redis-py-cluster.git@master")
        # the following can be probably installed from pypi
        self.pip_install("--no-cache-dir git+https://github.com/RedisLabsModules/RLTest.git@master")
        self.pip_install("--no-cache-dir git+https://github.com/RedisLabs/RAMP@master")

        root = os.path.join(os.path.dirname(__file__), "..")
        # self.pip_install("-r {}/test/test_requirements.txt".format(root))

        self.pip_install("awscli")
        self.pip_install("mkdocs mkdocs-material mkdocs-extensions")

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RedisAISetup(nop = args.nop).setup()
