# BUILD redisfab/jetson-jetpack:$(VERSION)-$(MODEL)-arm64v8-$(OSNICK)

ARG VERSION=4.4.1
ARG MODEL=nano
ARG BASE_OS=ubuntu:bionic
ARG OSNICK=bionic

#----------------------------------------------------------------------------------------------
FROM $(BASE_OS)

COPY /xetc/alternatives/cud*    /etc/alternatives/
COPY /xetc/alternatives/libcud* /etc/alternatives/
COPY /xetc/alternatives/libmpi* /etc/alternatives/
COPY /xetc/alternatives/vpi/    /etc/alternatives/vpi/
COPY /xetc/alternatives/vpi-*   /etc/alternatives/

COPY /xetc/ld.conf.d/cuda-10-2.conf    /etc/ld.conf.d/
COPY /xetc/ld.conf.d/nvidia-tegra.conf /etc/ld.conf.d/

RUN mkdir -p /usr/include/aarch64-linux-gnu/ /usr/include/hwloc

COPY /usr/include/aarch64-linux-gnu/Nv*  /usr/include/aarch64-linux-gnu/
COPY /usr/include/aarch64-linux-gnu/cud* /usr/include/aarch64-linux-gnu/
COPY /xusr/include/cub*       /usr/include/
COPY /xusr/include/cud*       /usr/include/
COPY /xusr/include/NVX/       /usr/include/NVX/
COPY /xusr/include/hwloc/cud* /usr/include/hwloc/

COPY /xusr/local/cuda10.2/ /usr/local/cuda10.2/
RUN cd /usr/local; ln -s cuda10.2 cuda

# COPY /xusr/local/cuda-10.2/targets/aarch64-linux/lib/libcufft*      /usr/local/cuda-10.2/targets/aarch64-linux/lib/
# COPY /xusr/local/cuda-10.2/targets/aarch64-linux/lib/stubs/libcuff* /usr/local/cuda-10.2/targets/aarch64-linux/lib/stub/

COPY /xusr/lib/libmpi* /usr/lib/

COPY /xusr/lib/aarch64-linux-gnu/libcublas.so /usr/lib/aarch64-linux-gnu/
COPY /xusr/lib/aarch64-linux-gnu/tegra/       /usr/lib/aarch64-linux-gnu/tegra/
COPY /xusr/lib/aarch64-linux-gnu/tegra-egl/   /usr/lib/aarch64-linux-gnu/tegra-egl/
COPY /xusr/lib/aarch64-linux-gnu/libcud*      /usr/lib/aarch64-linux-gnu/
COPY /xusr/lib/aarch64-linux-gnu/libcub*      /usr/lib/aarch64-linux-gnu/
COPY /xusr/lib/aarch64-linux-gnu/openmpi/     /usr/lib/aarch64-linux-gnu/openmpi/
COPY /xusr/lib/aarch64-linux-gnu/libmpi*      /usr/lib/aarch64-linux-gnu/
COPY /xusr/lib/aarch64-linux-gnu/libopen-*    /usr/lib/aarch64-linux-gnu/

# COPY /xopt/nvidia/ /opt/nvidia/
