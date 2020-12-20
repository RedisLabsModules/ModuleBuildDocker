[![CircleCI](https://circleci.com/gh/RedisLabsModules/ModuleBuildDocker/tree/master.svg?style=svg)](https://circleci.com/gh/RedisLabsModules/ModuleBuildDocker/tree/master)
[![Dockerhub](https://img.shields.io/badge/dockerhub-rmbuilder-blue)](https://hub.docker.com/r/redisfab/rmbuilder/tags) 

# Builders for Redis Modules related projects
# RMBuilder

Docker image for constructing platform-specific, optimized build environment for Redis Modules.
Note that this image is to be used primarily in CI for purpose of optimizing build times, and better not be relied on for satisfying build requirements (for this, we have each module's system-seup.py script and Dockerfiles).

## How to build

Display build instructions:
```sh
$ make help
make [build|publish] [X64=1|ARM8=1|ARM7=1] [OSNICK=<nick> | OS=<os>] [REDIS_VERSION=<ver>] [ARGS...]

build    Build image(s)
publish  Push image(s) to Docker Hub

Arguments:
OS         OS Docker image name (e.g., debian:buster-slim)
OSNICK     buster|stretch|xenial|bionic|centos6|centos7|centos8|fedora30
REDIS_VER  Redis version (e.g. 6.0.9)
TEST=1     Run tests after build
CACHE=0    Build without cache
```

Typical build (this will build and publish images for the common platforms):
```sh
make build publish X64=1 OSNICK=buster  REDIS_VER=6.0.9
make build publish X64=1 OSNICK=centos7 REDIS_VER=6.0.9
make build publish X64=1 OSNICK=bionic  REDIS_VER=6.0.9
```

# CLang

A Debian-based container that includes an up-to-date build of LLVM, Clang, Clang memory and address sanitizers, and a Redis server copmatibally-built for those sanitizers.

# Python

Platform-specific build of Python 3 interpreter, installed in `/usr/local`, that allows building and installing Python packages into that directory, to be later included in other Docker images to be utilized by RedisGears and RedisEdge, for instance.

# nVidia Jetpack

Docker image that tries to approximate the Nvidia Jetpack SDK, as installed on nVidia-provided SDCard. This allows to build and run programs that use Jetpack SDK in a container (which is not currently possible if using ` nvcr.io/nvidia/l4t-base:r32.4.4 `).