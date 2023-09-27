#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
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
__used
__attribute__((section("__versions"))) = {
	{ 0x7ef2b274, __VMLINUX_SYMBOL_STR(module_layout) },
	{ 0x5773238, __VMLINUX_SYMBOL_STR(kmalloc_caches) },
	{ 0x946d4a0c, __VMLINUX_SYMBOL_STR(vCanCleanup) },
	{ 0x672edad8, __VMLINUX_SYMBOL_STR(pv_lock_ops) },
	{ 0xcdbfc112, __VMLINUX_SYMBOL_STR(seq_printf) },
	{ 0x2167086d, __VMLINUX_SYMBOL_STR(vCanTime) },
	{ 0xa034bb5c, __VMLINUX_SYMBOL_STR(queue_empty) },
	{ 0xfb578fc5, __VMLINUX_SYMBOL_STR(memset) },
	{ 0x50614cee, __VMLINUX_SYMBOL_STR(queue_front) },
	{ 0x53ceed87, __VMLINUX_SYMBOL_STR(vCanDispatchEvent) },
	{ 0x9b65a65f, __VMLINUX_SYMBOL_STR(current_task) },
	{ 0x27e1a049, __VMLINUX_SYMBOL_STR(printk) },
	{ 0x32e94b6b, __VMLINUX_SYMBOL_STR(set_capability_value) },
	{ 0x8c8822a4, __VMLINUX_SYMBOL_STR(queue_wakeup_on_space) },
	{ 0x256a9c87, __VMLINUX_SYMBOL_STR(queue_pop) },
	{ 0x9ea2120b, __VMLINUX_SYMBOL_STR(vCanInitData) },
	{ 0x6ca88ed, __VMLINUX_SYMBOL_STR(vCanGetCardInfo2) },
	{ 0xdb7305a1, __VMLINUX_SYMBOL_STR(__stack_chk_fail) },
	{ 0x8ddd8aad, __VMLINUX_SYMBOL_STR(schedule_timeout) },
	{ 0xa202a8e5, __VMLINUX_SYMBOL_STR(kmalloc_order_trace) },
	{ 0x2ea2c95c, __VMLINUX_SYMBOL_STR(__x86_indirect_thunk_rax) },
	{ 0xbdfb6dbb, __VMLINUX_SYMBOL_STR(__fentry__) },
	{ 0xbeee391, __VMLINUX_SYMBOL_STR(kmem_cache_alloc_trace) },
	{ 0x56321ae2, __VMLINUX_SYMBOL_STR(_raw_spin_lock) },
	{ 0xfe768495, __VMLINUX_SYMBOL_STR(__wake_up) },
	{ 0x24d5c1b2, __VMLINUX_SYMBOL_STR(vCanGetCardInfo) },
	{ 0x37a0cba, __VMLINUX_SYMBOL_STR(kfree) },
	{ 0xf41ea9f4, __VMLINUX_SYMBOL_STR(vCanInit) },
	{ 0xb217c842, __VMLINUX_SYMBOL_STR(vCanFlushSendBuffer) },
	{ 0x7794a5a7, __VMLINUX_SYMBOL_STR(queue_release) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=kvcommon";


MODULE_INFO(srcversion, "E25E249003E3D75F280D091");
