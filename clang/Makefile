
CLANG_VER ?= 12
OSNICK=strech
ARCH=x64

IMAGE=redisfab/clang:$(CLANG_VER)-$(ARCH)-$(OSNICK)
VIEW=/w

build:
	docker build -t $(IMAGE) --build-arg CLANG_VER=$(CLANG_VER) .

publish:
	docker push $(IMAGE)

run:
	docker run -it $(IMAGE) -v $(VIEW):$(VIEW) --cap-add SYS_PTRACE bash
