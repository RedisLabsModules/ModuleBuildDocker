.NOTPARALLEL:

# OSNICK=buster|stretch|trusty|xenial|bionic|centos6|centos7|centos8|fedora30
OSNICK ?= buster

# OS ?= debian:buster-slim

REDIS_VER ?= 6.0.9

#----------------------------------------------------------------------------------------------

REPO=redisfab
STEM=$(REPO)/rmbuilder

OS.trusty=ubuntu:trusty
OS.xenial=ubuntu:xenial
OS.bionic=ubuntu:bionic
OS.focal=ubuntu:focal
OS.stretch=debian:stretch-slim
OS.buster=debian:buster-slim
OS.centos6=centos:6.10
OS.centos7=centos:7.8.2003
OS.centos8=centos:8
OS.fedora=fedora:33
OS.fedora33=fedora:33
OS:=$(OS.$(OSNICK))

ifeq ($(OS),)
$(error cannot determine OS for OSNICK $(OSNICK))
endif

DOCKER=docker
BUILD_OPT=--rm
# --squash

ifeq ($(CACHE),0)
CACHE_ARG=--no-cache
endif

#----------------------------------------------------------------------------------------------

define targets # (1=OP, 2=op)
$(1)_TARGETS :=
$(1)_TARGETS += $(if $(findstring $(X64),1),$(2)_x64)
$(1)_TARGETS += $(if $(findstring $(ARM7),1),$(2)_arm32v7)
$(1)_TARGETS += $(if $(findstring $(ARM8),1),$(2)_arm64v8)

# $(1)_TARGETS += $$(if $$(strip $$($(1)_TARGETS)),,$(2)_x64 $(2)_arm32v7 $(2)_arm64v8)
$(1)_TARGETS += $$(if $$(strip $$($(1)_TARGETS)),,$(2)_x64)
endef

$(eval $(call targets,BUILD,build))
$(eval $(call targets,PUBLISH,publish))

#----------------------------------------------------------------------------------------------

define build_x64
build_x64:
	@echo "Building $(STEM):$(REDIS_VER)-x64-$(OSNICK) ($(OS))"
	@$(DOCKER) pull $(OS)
	@$(DOCKER) build $(BUILD_OPT) -t $(STEM):$(REDIS_VER)-x64-$(OSNICK) -f Dockerfile \
		$(CACHE_ARG) \
		--build-arg ARCH=x64 \
		--build-arg OSNICK=$(OSNICK) \
		--build-arg OS=$(OS) \
		--build-arg REDIS_VER=$(REDIS_VER) \
		.

.PHONY: build_x64
endef

define build_arm # (1=arch)
build_$(1): 
	@$(DOCKER) build $(BUILD_OPT) -t $(STEM)-xbuild:$(REDIS_VER)-$(1)-$(OSNICK) -f Dockerfile.arm \
		--build-arg ARCH=$(1) \
		--build-arg OSNICK=$(OSNICK) \
		--build-arg OS=$(OS) \
		--build-arg REDIS_VER=$(REDIS_VER) \
		.

.PHONY: build_$(1)
endef

#----------------------------------------------------------------------------------------------

define publish_x64
publish_x64:
	@$(DOCKER) push $(STEM):$(REDIS_VER)-x64-$(OSNICK)

.PHONY: publish_x64
endef

define publish_arm # (1=arch)
publish_$(1):
	@$(DOCKER) push $(STEM)-xbuild:$(REDIS_VER)-$(1)-$(OSNICK)

.PHONY: publish_$(1)
endef

#----------------------------------------------------------------------------------------------

all: build publish

build: $(BUILD_TARGETS)

$(eval $(call build_x64))
$(eval $(call build_arm,arm64v8))
$(eval $(call build_arm,arm32v7))

publish: $(PUBLISH_TARGETS)

$(eval $(call publish_x64))
$(eval $(call publish_arm,arm64v8))
$(eval $(call publish_arm,arm32v7))

#----------------------------------------------------------------------------------------------

define HELP
make [build|publish] [X64=1|ARM8=1|ARM7=1] [OSNICK=<nick> | OS=<os>] [REDIS_VER=<ver>] [ARGS...]

build    Build image(s)
publish  Push image(s) to Docker Hub

Arguments:
OSNICK     buster|stretch|xenial|bionic|centos6|centos7|centos8|fedora30
OS         (optional) OS Docker image name (e.g., debian:buster-slim)
REDIS_VER  Redis version (e.g. $(REDIS_VER))
TEST=1     Run tests after build
CACHE=0    Build without cache


endef

help:
	$(file >/tmp/help,$(HELP))
	@cat /tmp/help
	@rm -f /tmp/help

#----------------------------------------------------------------------------------------------

.PHONY: all build publish help
