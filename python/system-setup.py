#!/usr/bin/env python2

import sys
import os
import argparse

ROOT = HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(ROOT, "deps/readies"))
import paella

#----------------------------------------------------------------------------------------------

class Python3Setup(paella.Setup):
    def __init__(self, nop=False):
        paella.Setup.__init__(self, nop)

    def common_first(self):
        self.install_downloaders()

        self.setup_pip()
        self.pip_install("wheel")
        self.pip_install("setuptools --upgrade")

        self.install("git openssl")

    def debian_compat(self):
        self.install("build-essential autotools-dev autoconf libtool gawk")
        self.install("libbz2-dev liblzma-dev lzma-dev libncurses5-dev libsqlite3-dev uuid-dev zlib1g-dev libssl-dev libreadline-dev libffi-dev")
        if sh("apt-cache search libgdbm-compat-dev") != "":
            self.install("libgdbm-compat-dev")
        self.install("libgdbm-dev")
        self.install("tcl-dev tix-dev tk-dev")

        self.install("lsb-release")
        self.install("zip unzip")

    def redhat_compat(self):
        self.group_install("'Development Tools'")
        self.install("autoconf automake libtool")

        self.install("bzip2-devel expat-devel gdbm-devel glibc-devel gmp-devel libffi-devel libuuid-devel ncurses-devel "
            "openssl-devel readline-devel sqlite-devel xz-devel zlib-devel")
        self.install("tcl-devel tix-devel tk-devel")

        self.install("redhat-lsb-core")
        self.install("zip unzip")
        self.install("libatomic file")

        self.run("wget -q -O /tmp/epel-release-latest-7.noarch.rpm http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm")
        self.run("rpm -Uv /tmp/epel-release-latest-7.noarch.rpm --replacepkgs ")

        if self.arch == 'x64':
            self.run("""
                dir=$(mktemp -d /tmp/tar.XXXXXX)
                (cd $dir; wget -q -O tar.tgz http://redismodules.s3.amazonaws.com/gnu/gnu-tar-1.32-x64-centos7.tgz; tar -xzf tar.tgz -C /; )
                rm -rf $dir
                """)

        # uninstall and install psutil (order is important), otherwise RLTest fails
        self.run("pip uninstall -y psutil || true")
        self.install("python2-psutil")

    def fedora(self):
        self.group_install("'Development Tools'")
        self.install("autoconf automake libtool")
        self.install("bzip2-devel expat-devel gdbm-devel glibc-devel gmp-devel libffi-devel libnsl2-devel libuuid-devel ncurses-devel "
            "openssl-devel readline-devel sqlite-devel xz-devel zlib-devel")
        self.install("tcl-devel tix-devel tk-devel")

        self.install("which libatomic file")

        # uninstall and install psutil (order is important), otherwise RLTest fails
        self.run("pip uninstall -y psutil || true")
        self.install("python2-psutil")

    def linux_last(self):
        pass

    def macosx(self):
        self.install("libtool autoconf automake")
        self.run("""
            dir=$(mktemp -d /tmp/gettext.XXXXXX)
            base=$(pwd)
            cd $dir
            wget -q -O gettext.tgz https://ftp.gnu.org/pub/gnu/gettext/gettext-0.20.2.tar.gz
            tar xzf gettext.tgz
            cd gettext-0.20.2
            ./configure
            make
            make install
            cd $base
            rm -rf $dir
            """, output_on_error=True)

        self.install("zlib openssl readline coreutils libiconv")
        self.install("binutils") # into /usr/local/opt/binutils
        self.install_gnu_utils()

    def common_last(self):
        pass

#----------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description='Set up system for RedisGears build.')
parser.add_argument('-n', '--nop', action="store_true", help='no operation')
args = parser.parse_args()

Python3Setup(nop = args.nop).setup()