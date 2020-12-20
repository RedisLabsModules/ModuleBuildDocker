#!/usr/bin/env python2

import sys
import os
import argparse

HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "../../.."))
READIES = os.path.join(ROOT, "deps/readies")
sys.path.insert(0, READIES)
import paella

#----------------------------------------------------------------------------------------------

class RedisTimeSeriesSetup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)

    def common_first(self):
        self.setup_pip()
        self.pip_install("wheel")
        self.pip_install("setuptools --upgrade")

        self.install("git jq curl")

    def debian_compat(self):
        self.install("build-essential")

    def redhat_compat(self):
        self.group_install("'Development Tools'")
        self.install("redhat-lsb-core")

    def fedora(self):
        self.group_install("'Development Tools'")

    def macos(self):
        if sh('xcode-select -p') == '':
            fatal("Xcode tools are not installed. Please run xcode-select --install.")
        self.install_gnu_utils()
        self.install("redis")

    def freebsd(self):
        self.install_gnu_utils()

    def common_last(self):
        self.install("lcov")
        if not self.has_command("ramp"):
            self.pip_install("git+https://github.com/RedisLabs/RAMP@master")
        self.pip_install("-r tests/requirements.txt")
        self.pip_install("jinja2")

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RedisTimeSeriesSetup(nop = args.nop).setup()
