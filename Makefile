#Making braw sdk wrapper module
UNAME_S := $(shell uname -s 2>/dev/null)

ifeq ($(OS),Windows_NT)
    include platform_makefiles/Makefile.win
else ifeq ($(UNAME_S),Linux)
    include platform_makefiles/Makefile.linux
else ifeq ($(UNAME_S),Darwin)
    include platform_makefiles/Makefile.macos
else
    $(error Unsupported platform)
endif
