cmd_/media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.o := gcc-11 -Wp,-MMD,/media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/.dlc.o.d -nostdinc -I./arch/x86/include -I./arch/x86/include/generated  -I./include -I./arch/x86/include/uapi -I./arch/x86/include/generated/uapi -I./include/uapi -I./include/generated/uapi -include ./include/linux/compiler-version.h -include ./include/linux/kconfig.h -I./ubuntu/include -include ./include/linux/compiler_types.h -D__KERNEL__ -fmacro-prefix-map=./= -Wall -Wundef -Werror=strict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -fshort-wchar -fno-PIE -Werror=implicit-function-declaration -Werror=implicit-int -Werror=return-type -Wno-format-security -funsigned-char -std=gnu11 -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -fcf-protection=none -m64 -falign-jumps=1 -falign-loops=1 -mno-80387 -mno-fp-ret-in-387 -mpreferred-stack-boundary=3 -mskip-rax-setup -mtune=generic -mno-red-zone -mcmodel=kernel -Wno-sign-compare -fno-asynchronous-unwind-tables -mindirect-branch=thunk-extern -mindirect-branch-register -mindirect-branch-cs-prefix -mfunction-return=thunk-extern -fno-jump-tables -mharden-sls=all -fpatchable-function-entry=16,16 -fno-delete-null-pointer-checks -Wno-frame-address -Wno-format-truncation -Wno-format-overflow -Wno-address-of-packed-member -O2 -fno-allow-store-data-races -Wframe-larger-than=1024 -fstack-protector-strong -Wno-main -Wno-unused-but-set-variable -Wno-unused-const-variable -fno-omit-frame-pointer -fno-optimize-sibling-calls -fno-stack-clash-protection -fzero-call-used-regs=used-gpr -pg -mrecord-mcount -mfentry -DCC_USING_FENTRY -falign-functions=16 -Wdeclaration-after-statement -Wvla -Wno-pointer-sign -Wcast-function-type -Wno-stringop-truncation -Wno-stringop-overflow -Wno-restrict -Wno-maybe-uninitialized -Wno-array-bounds -Wno-alloc-size-larger-than -Wimplicit-fallthrough=5 -fno-strict-overflow -fno-stack-check -fconserve-stack -Werror=date-time -Werror=incompatible-pointer-types -Werror=designated-init -Wno-packed-not-aligned -g -gdwarf-5 -DLINUX=1 -I/media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/../include/ -Wall -Wno-date-time -D_DEBUG=0 -DDEBUG=0 -DWIN32=0 -Wframe-larger-than=1024  -fsanitize=bounds -fsanitize=shift -fsanitize=bool -fsanitize=enum  -DMODULE  -DKBUILD_BASENAME='"dlc"' -DKBUILD_MODNAME='"kvcommon"' -D__KBUILD_MODNAME=kmod_kvcommon -c -o /media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.o /media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.c   ; ./tools/objtool/objtool --hacks=jump_label --hacks=noinstr --hacks=skylake --retpoline --rethunk --sls --stackval --static-call --uaccess --prefix=16   --module /media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.o

source_/media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.o := /media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.c

deps_/media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.o := \
  include/linux/compiler-version.h \
    $(wildcard include/config/CC_VERSION_TEXT) \
  include/linux/kconfig.h \
    $(wildcard include/config/CPU_BIG_ENDIAN) \
    $(wildcard include/config/BOOGER) \
    $(wildcard include/config/FOO) \
  include/linux/compiler_types.h \
    $(wildcard include/config/DEBUG_INFO_BTF) \
    $(wildcard include/config/PAHOLE_HAS_BTF_TAG) \
    $(wildcard include/config/FUNCTION_ALIGNMENT) \
    $(wildcard include/config/CC_IS_GCC) \
    $(wildcard include/config/HAVE_ARCH_COMPILER_H) \
    $(wildcard include/config/CC_HAS_ASM_INLINE) \
  include/linux/compiler_attributes.h \
  include/linux/compiler-gcc.h \
    $(wildcard include/config/RETPOLINE) \
    $(wildcard include/config/ARCH_USE_BUILTIN_BSWAP) \
    $(wildcard include/config/SHADOW_CALL_STACK) \
    $(wildcard include/config/KCOV) \
  /media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/../include/dlc.h \
  include/linux/types.h \
    $(wildcard include/config/HAVE_UID16) \
    $(wildcard include/config/UID16) \
    $(wildcard include/config/ARCH_DMA_ADDR_T_64BIT) \
    $(wildcard include/config/PHYS_ADDR_T_64BIT) \
    $(wildcard include/config/64BIT) \
    $(wildcard include/config/ARCH_32BIT_USTAT_F_TINODE) \
  include/uapi/linux/types.h \
  arch/x86/include/generated/uapi/asm/types.h \
  include/uapi/asm-generic/types.h \
  include/asm-generic/int-ll64.h \
  include/uapi/asm-generic/int-ll64.h \
  arch/x86/include/uapi/asm/bitsperlong.h \
  include/asm-generic/bitsperlong.h \
  include/uapi/asm-generic/bitsperlong.h \
  include/uapi/linux/posix_types.h \
  include/linux/stddef.h \
  include/uapi/linux/stddef.h \
  include/linux/compiler_types.h \
  arch/x86/include/asm/posix_types.h \
    $(wildcard include/config/X86_32) \
  arch/x86/include/uapi/asm/posix_types_64.h \
  include/uapi/asm-generic/posix_types.h \
  include/generated/uapi/linux/version.h \
  include/linux/export.h \
    $(wildcard include/config/MODVERSIONS) \
    $(wildcard include/config/HAVE_ARCH_PREL32_RELOCATIONS) \
    $(wildcard include/config/MODULES) \
    $(wildcard include/config/TRIM_UNUSED_KSYMS) \
  include/linux/stringify.h \
  include/linux/compiler.h \
    $(wildcard include/config/TRACE_BRANCH_PROFILING) \
    $(wildcard include/config/PROFILE_ALL_BRANCHES) \
    $(wildcard include/config/OBJTOOL) \
  arch/x86/include/generated/asm/rwonce.h \
  include/asm-generic/rwonce.h \
  include/linux/kasan-checks.h \
    $(wildcard include/config/KASAN_GENERIC) \
    $(wildcard include/config/KASAN_SW_TAGS) \
  include/linux/kcsan-checks.h \
    $(wildcard include/config/KCSAN) \
    $(wildcard include/config/KCSAN_WEAK_MEMORY) \
    $(wildcard include/config/KCSAN_IGNORE_ATOMICS) \

/media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.o: $(deps_/media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.o)

$(deps_/media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.o):

/media/gyruma/Daten/Benutzerdaten/gyurma/Documents/git/PythonCanSteering/linuxcan3/common/dlc.o: $(wildcard ./tools/objtool/objtool)
#SYMVER dlc_bytes_to_dlc_fd 0xbfaf25a3
#SYMVER dlc_dlc_to_bytes_fd 0x63fbdd18
#SYMVER dlc_is_dlc_ok 0xab1ad228
#SYMVER dlc_dlc_to_bytes_classic 0xede295c6
