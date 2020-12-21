#!/usr/bin/env python2

import sys
import os
import argparse

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = HERE
READIES = os.path.join(ROOT, "deps/readies")
sys.path.insert(0, READIES)
import paella

#----------------------------------------------------------------------------------------------

class RedisModuleBuilderSetup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)

    #------------------------------------------------------------------------------------------
    def common_first(self):
        self.install_downloaders()
        self.setup_pip()
        self.pip_install("wheel")
        self.pip_install("setuptools --upgrade")

        self.install("git")
        self.install("coreutils") # for realpath

    #------------------------------------------------------------------------------------------
    def debian_compat(self):
        self.install("build-essential")
        if self.osnick == 'trusty':
            self.run("%s/bin/getgcc --modern" % READIES)
        self.install("openssh-client")
        self.install("python-regex")

    #------------------------------------------------------------------------------------------
    def redhat_compat(self):
        self.group_install("'Development Tools'")

        self.install("redhat-lsb-core")
        self.install("epel-release")

        self.install("openssh-clients")
        self.install("python2-regex")

    #------------------------------------------------------------------------------------------
    def fedora(self):
        self.group_install("'Development Tools'")
        self.install("openssh-clients")
        self.install("python2-regex")

    #------------------------------------------------------------------------------------------
    def linux_last(self):
        # self.run("%s/bin/getdocker" % READIES)
        self.install_git_lfs_on_linux()

    #------------------------------------------------------------------------------------------
    def macos(self):
        self.install("redis")
        self.install("binutils") # into /usr/local/opt/binutils
        self.install("git-lfs")

    #------------------------------------------------------------------------------------------
    def common_last(self):
        self.install("valgrind")
        self.pip_install("pytest rmtest")

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RedisModuleBuilderSetup(nop = args.nop).setup()
