#include <linux/module.h>
#include <linux/export-internal.h>
#include <linux/compiler.h>

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



static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x59b87546, "vCanAddCardChannel" },
	{ 0x39b5bb15, "queue_release" },
	{ 0x59b87546, "vCanFlushSendBuffer" },
	{ 0x645c8a85, "vCanInit" },
	{ 0xcb8b6ec6, "kfree" },
	{ 0x48feac32, "vCanGetCardInfo" },
	{ 0x16ab4215, "__wake_up" },
	{ 0xde338d9a, "_raw_spin_lock" },
	{ 0xd272d446, "__fentry__" },
	{ 0x5a844b26, "__x86_indirect_thunk_rax" },
	{ 0xe8213e80, "_printk" },
	{ 0x6ac784f4, "schedule_timeout" },
	{ 0xd272d446, "__stack_chk_fail" },
	{ 0x7870c5f2, "vCanGetCardInfo2" },
	{ 0xd710adbf, "__kmalloc_large_noprof" },
	{ 0x4d40f3a6, "const_pcpu_hot" },
	{ 0xd9d667bd, "vCanInitData" },
	{ 0x90a48d82, "__ubsan_handle_out_of_bounds" },
	{ 0xbd03ed67, "random_kmalloc_seed" },
	{ 0x39b5bb15, "queue_pop" },
	{ 0x39b5bb15, "queue_wakeup_on_space" },
	{ 0xba8e1447, "set_capability_value" },
	{ 0x689ff9d2, "vCanDispatchEvent" },
	{ 0xe7db7ec6, "queue_front" },
	{ 0x27683a56, "memset" },
	{ 0xd272d446, "__x86_return_thunk" },
	{ 0xe7db7ec6, "queue_empty" },
	{ 0x34e23247, "vCanRemoveCardChannel" },
	{ 0xb5cbfe81, "vCanTime" },
	{ 0x70db3fe4, "__kmalloc_cache_noprof" },
	{ 0xde338d9a, "_raw_spin_unlock" },
	{ 0x34583558, "vCanCleanup" },
	{ 0xfed1e3bc, "kmalloc_caches" },
	{ 0xba157484, "module_layout" },
};

static const u32 ____version_ext_crcs[]
__used __section("__version_ext_crcs") = {
	0x59b87546,
	0x39b5bb15,
	0x59b87546,
	0x645c8a85,
	0xcb8b6ec6,
	0x48feac32,
	0x16ab4215,
	0xde338d9a,
	0xd272d446,
	0x5a844b26,
	0xe8213e80,
	0x6ac784f4,
	0xd272d446,
	0x7870c5f2,
	0xd710adbf,
	0x4d40f3a6,
	0xd9d667bd,
	0x90a48d82,
	0xbd03ed67,
	0x39b5bb15,
	0x39b5bb15,
	0xba8e1447,
	0x689ff9d2,
	0xe7db7ec6,
	0x27683a56,
	0xd272d446,
	0xe7db7ec6,
	0x34e23247,
	0xb5cbfe81,
	0x70db3fe4,
	0xde338d9a,
	0x34583558,
	0xfed1e3bc,
	0xba157484,
};
static const char ____version_ext_names[]
__used __section("__version_ext_names") =
	"vCanAddCardChannel\0"
	"queue_release\0"
	"vCanFlushSendBuffer\0"
	"vCanInit\0"
	"kfree\0"
	"vCanGetCardInfo\0"
	"__wake_up\0"
	"_raw_spin_lock\0"
	"__fentry__\0"
	"__x86_indirect_thunk_rax\0"
	"_printk\0"
	"schedule_timeout\0"
	"__stack_chk_fail\0"
	"vCanGetCardInfo2\0"
	"__kmalloc_large_noprof\0"
	"const_pcpu_hot\0"
	"vCanInitData\0"
	"__ubsan_handle_out_of_bounds\0"
	"random_kmalloc_seed\0"
	"queue_pop\0"
	"queue_wakeup_on_space\0"
	"set_capability_value\0"
	"vCanDispatchEvent\0"
	"queue_front\0"
	"memset\0"
	"__x86_return_thunk\0"
	"queue_empty\0"
	"vCanRemoveCardChannel\0"
	"vCanTime\0"
	"__kmalloc_cache_noprof\0"
	"_raw_spin_unlock\0"
	"vCanCleanup\0"
	"kmalloc_caches\0"
	"module_layout\0"
;

MODULE_INFO(depends, "kvcommon");


MODULE_INFO(srcversion, "F691342F17CCFB55EDFB3B3");
