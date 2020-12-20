#!/usr/bin/env python3

import sys
import os
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "deps/readies"))
import paella

#----------------------------------------------------------------------------------------------

class RedisModuleBuilderSetup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)

    #------------------------------------------------------------------------------------------
    def common_first(self):
        self.setup_pip()
        self.pip3_install("wheel")
        self.pip3_install("setuptools --upgrade")
        if self.osnick == 'centos7' or self.osnick == 'bionic':
            self.pip3_install("mkdocs mkdocs-material mkdocs-extensions")

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

RedisModuleBuilderSetup(nop = args.nop).setup()
