savedcmd_dlc.o := gcc-13 -Wp,-MMD,./.dlc.o.d -nostdinc -I/usr/src/linux-headers-6.14.0-37-generic/arch/x86/include -I/usr/src/linux-headers-6.14.0-37-generic/arch/x86/include/generated -I/usr/src/linux-headers-6.14.0-37-generic/include -I/usr/src/linux-headers-6.14.0-37-generic/include -I/usr/src/linux-headers-6.14.0-37-generic/arch/x86/include/uapi -I/usr/src/linux-headers-6.14.0-37-generic/arch/x86/include/generated/uapi -I/usr/src/linux-headers-6.14.0-37-generic/include/uapi -I/usr/src/linux-headers-6.14.0-37-generic/include/generated/uapi -include /usr/src/linux-headers-6.14.0-37-generic/include/linux/compiler-version.h -include /usr/src/linux-headers-6.14.0-37-generic/include/linux/kconfig.h -I/usr/src/linux-headers-6.14.0-37-generic/ubuntu/include -include /usr/src/linux-headers-6.14.0-37-generic/include/linux/compiler_types.h -D__KERNEL__ -std=gnu11 -fshort-wchar -funsigned-char -fno-common -fno-PIE -fno-strict-aliasing -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -fcf-protection=none -m64 -falign-jumps=1 -falign-loops=1 -mno-80387 -mno-fp-ret-in-387 -mpreferred-stack-boundary=3 -mskip-rax-setup -mtune=generic -mno-red-zone -mcmodel=kernel -Wno-sign-compare -fno-asynchronous-unwind-tables -mindirect-branch=thunk-extern -mindirect-branch-register -mindirect-branch-cs-prefix -mfunction-return=thunk-extern -fno-jump-tables -mharden-sls=all -fpatchable-function-entry=16,16 -fno-delete-null-pointer-checks -O2 -fno-allow-store-data-races -fstack-protector-strong -fno-omit-frame-pointer -fno-optimize-sibling-calls -ftrivial-auto-var-init=zero -fno-stack-clash-protection -fzero-call-used-regs=used-gpr -pg -mrecord-mcount -mfentry -DCC_USING_FENTRY -falign-functions=16 -fstrict-flex-arrays=3 -fno-strict-overflow -fno-stack-check -fconserve-stack -fno-builtin-wcslen -Wall -Wextra -Wundef -Werror=implicit-function-declaration -Werror=implicit-int -Werror=return-type -Werror=strict-prototypes -Wno-format-security -Wno-trigraphs -Wno-frame-address -Wno-address-of-packed-member -Wmissing-declarations -Wmissing-prototypes -Wframe-larger-than=1024 -Wno-main -Wno-dangling-pointer -Wvla -Wno-pointer-sign -Wcast-function-type -Wno-array-bounds -Wno-stringop-overflow -Wno-alloc-size-larger-than -Wimplicit-fallthrough=5 -Werror=date-time -Werror=incompatible-pointer-types -Werror=designated-init -Wenum-conversion -Wunused -Wno-unused-but-set-variable -Wno-unused-const-variable -Wno-packed-not-aligned -Wno-format-overflow -Wno-format-truncation -Wno-stringop-truncation -Wno-override-init -Wno-missing-field-initializers -Wno-type-limits -Wno-shift-negative-value -Wno-maybe-uninitialized -Wno-sign-compare -Wno-unused-parameter -g -gdwarf-5 -DLINUX=1 -I././../include/ -Wall -Wno-date-time -D_DEBUG=0 -DDEBUG=0 -DWIN32=0 -Wframe-larger-than=1024  -fsanitize=bounds-strict -fsanitize=shift -fsanitize=bool -fsanitize=enum    -DMODULE  -DKBUILD_BASENAME='"dlc"' -DKBUILD_MODNAME='"kvcommon"' -D__KBUILD_MODNAME=kmod_kvcommon -c -o dlc.o dlc.c   ; /usr/src/linux-headers-6.14.0-37-generic/tools/objtool/objtool --hacks=jump_label --hacks=noinstr --hacks=skylake --retpoline --rethunk --sls --stackval --static-call --uaccess --prefix=16   --module dlc.o

source_dlc.o := dlc.c

deps_dlc.o := \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/compiler-version.h \
    $(wildcard include/config/CC_VERSION_TEXT) \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/kconfig.h \
    $(wildcard include/config/CPU_BIG_ENDIAN) \
    $(wildcard include/config/BOOGER) \
    $(wildcard include/config/FOO) \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/compiler_types.h \
    $(wildcard include/config/DEBUG_INFO_BTF) \
    $(wildcard include/config/PAHOLE_HAS_BTF_TAG) \
    $(wildcard include/config/FUNCTION_ALIGNMENT) \
    $(wildcard include/config/CC_HAS_SANE_FUNCTION_ALIGNMENT) \
    $(wildcard include/config/X86_64) \
    $(wildcard include/config/ARM64) \
    $(wildcard include/config/LD_DEAD_CODE_DATA_ELIMINATION) \
    $(wildcard include/config/LTO_CLANG) \
    $(wildcard include/config/HAVE_ARCH_COMPILER_H) \
    $(wildcard include/config/CC_HAS_COUNTED_BY) \
    $(wildcard include/config/UBSAN_SIGNED_WRAP) \
    $(wildcard include/config/CC_HAS_ASM_INLINE) \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/compiler_attributes.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/compiler-gcc.h \
    $(wildcard include/config/MITIGATION_RETPOLINE) \
    $(wildcard include/config/ARCH_USE_BUILTIN_BSWAP) \
    $(wildcard include/config/SHADOW_CALL_STACK) \
    $(wildcard include/config/KCOV) \
  ../include/dlc.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/types.h \
    $(wildcard include/config/HAVE_UID16) \
    $(wildcard include/config/UID16) \
    $(wildcard include/config/ARCH_DMA_ADDR_T_64BIT) \
    $(wildcard include/config/PHYS_ADDR_T_64BIT) \
    $(wildcard include/config/64BIT) \
    $(wildcard include/config/ARCH_32BIT_USTAT_F_TINODE) \
  /usr/src/linux-headers-6.14.0-37-generic/include/uapi/linux/types.h \
  /usr/src/linux-headers-6.14.0-37-generic/arch/x86/include/generated/uapi/asm/types.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/uapi/asm-generic/types.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/asm-generic/int-ll64.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/uapi/asm-generic/int-ll64.h \
  /usr/src/linux-headers-6.14.0-37-generic/arch/x86/include/uapi/asm/bitsperlong.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/asm-generic/bitsperlong.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/uapi/asm-generic/bitsperlong.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/uapi/linux/posix_types.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/stddef.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/uapi/linux/stddef.h \
  /usr/src/linux-headers-6.14.0-37-generic/arch/x86/include/asm/posix_types.h \
    $(wildcard include/config/X86_32) \
  /usr/src/linux-headers-6.14.0-37-generic/arch/x86/include/uapi/asm/posix_types_64.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/uapi/asm-generic/posix_types.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/generated/uapi/linux/version.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/export.h \
    $(wildcard include/config/MODVERSIONS) \
    $(wildcard include/config/GENDWARFKSYMS) \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/compiler.h \
    $(wildcard include/config/TRACE_BRANCH_PROFILING) \
    $(wildcard include/config/PROFILE_ALL_BRANCHES) \
    $(wildcard include/config/OBJTOOL) \
  /usr/src/linux-headers-6.14.0-37-generic/arch/x86/include/generated/asm/rwonce.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/asm-generic/rwonce.h \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/kasan-checks.h \
    $(wildcard include/config/KASAN_GENERIC) \
    $(wildcard include/config/KASAN_SW_TAGS) \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/kcsan-checks.h \
    $(wildcard include/config/KCSAN) \
    $(wildcard include/config/KCSAN_WEAK_MEMORY) \
    $(wildcard include/config/KCSAN_IGNORE_ATOMICS) \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/linkage.h \
    $(wildcard include/config/ARCH_USE_SYM_ANNOTATIONS) \
  /usr/src/linux-headers-6.14.0-37-generic/include/linux/stringify.h \
  /usr/src/linux-headers-6.14.0-37-generic/arch/x86/include/asm/linkage.h \
    $(wildcard include/config/CALL_PADDING) \
    $(wildcard include/config/MITIGATION_RETHUNK) \
    $(wildcard include/config/MITIGATION_SLS) \
    $(wildcard include/config/FUNCTION_PADDING_BYTES) \
    $(wildcard include/config/UML) \
  /usr/src/linux-headers-6.14.0-37-generic/arch/x86/include/asm/ibt.h \
    $(wildcard include/config/X86_KERNEL_IBT) \

dlc.o: $(deps_dlc.o)

$(deps_dlc.o):

dlc.o: $(wildcard /usr/src/linux-headers-6.14.0-37-generic/tools/objtool/objtool)
#SYMVER dlc_dlc_to_bytes_classic 0x2502e48b
#SYMVER dlc_is_dlc_ok 0xbabca771
#SYMVER dlc_dlc_to_bytes_fd 0x2502e48b
#SYMVER dlc_bytes_to_dlc_fd 0xa7665c08
