#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif


static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x1eaab143, "vCanAddCardChannel" },
	{ 0x30372d96, "queue_release" },
	{ 0x828398ff, "vCanFlushSendBuffer" },
	{ 0x1229cb50, "vCanInit" },
	{ 0x37a0cba, "kfree" },
	{ 0x166163ff, "vCanGetCardInfo" },
	{ 0xf72e8c06, "pcpu_hot" },
	{ 0xe2964344, "__wake_up" },
	{ 0xba8fbd64, "_raw_spin_lock" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x65487097, "__x86_indirect_thunk_rax" },
	{ 0x122c3a7e, "_printk" },
	{ 0x8ddd8aad, "schedule_timeout" },
	{ 0xa19b956, "__stack_chk_fail" },
	{ 0xec8d96be, "vCanGetCardInfo2" },
	{ 0xb5385e3c, "vCanInitData" },
	{ 0x87a21cb3, "__ubsan_handle_out_of_bounds" },
	{ 0x220f6eb0, "queue_pop" },
	{ 0xe6cf5658, "queue_wakeup_on_space" },
	{ 0x4a379bbf, "set_capability_value" },
	{ 0x9ed12e20, "kmalloc_large" },
	{ 0xffd473e4, "vCanDispatchEvent" },
	{ 0xfaa20ff6, "queue_front" },
	{ 0xfb578fc5, "memset" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0x679e43d1, "queue_empty" },
	{ 0xafec5d3, "vCanRemoveCardChannel" },
	{ 0x84f435c1, "vCanTime" },
	{ 0x850e6a88, "kmalloc_trace" },
	{ 0xb5b54b34, "_raw_spin_unlock" },
	{ 0x86204941, "vCanCleanup" },
	{ 0xad6d045f, "kmalloc_caches" },
	{ 0x453e7dc, "module_layout" },
};

MODULE_INFO(depends, "kvcommon");


MODULE_INFO(srcversion, "F691342F17CCFB55EDFB3B3");
