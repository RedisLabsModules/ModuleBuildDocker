#!/usr/bin/env python3

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
        self.setup_pip()
        self.pip_install("wheel")
        self.pip_install("setuptools --upgrade")
        if self.osnick == 'centos7' or self.osnick == 'bionic':
            self.pip_install("mkdocs mkdocs-material mkdocs-extensions")

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RedisModuleBuilderSetup(nop = args.nop).setup()
