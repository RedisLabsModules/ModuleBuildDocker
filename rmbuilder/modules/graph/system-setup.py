#!/usr/bin/env python2

import sys
import os
from subprocess import Popen, PIPE
import argparse

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
READIES = os.path.join(ROOT, "deps/readies")
sys.path.insert(0, READIES)
import paella

#----------------------------------------------------------------------------------------------

class RedisGraphSetup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)

    def common_first(self):
        self.install_downloaders()
        self.setup_pip()
        self.pip_install("wheel virtualenv")
        self.pip_install("setuptools --upgrade")

        self.install("git automake peg libtool autoconf cmake valgrind astyle")

    def debian_compat(self):
        self.install("build-essential")
        self.install("python-psutil")

    def redhat_compat(self):
        self.group_install("'Development Tools'")
        self.install("redhat-lsb-core")
        self.pip_install("psutil")

    def fedora(self):
        self.group_install("'Development Tools'")
        self.install("python-psutil")

    def macosx(self):
        self.install_gnu_utils()
        self.install("redis")

    def common_last(self):
        # this is due to rmbuilder older versions. should be removed once fixed.
        # self.run("pip uninstall -y -q redis redis-py-cluster ramp-packer RLTest rmtest semantic-version || true")
        # redis-py-cluster should be installed from git due to redis-py dependency
        # self.pip_install("--no-cache-dir git+https://github.com/Grokzen/redis-py-cluster.git@master")
        self.pip_install("redis-py-cluster")
        # the following can be probably installed from pypi
        self.pip_install("--no-cache-dir git+https://github.com/RedisLabsModules/RLTest.git@master")
        self.pip_install("--no-cache-dir git+https://github.com/RedisLabs/RAMP@master")

        # self.pip_install("-r tests/requirements.txt")

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RedisGraphSetup(nop=args.nop).setup()
