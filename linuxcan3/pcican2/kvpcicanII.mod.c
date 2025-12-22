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
	{ 0x9dd4105e, "free_irq" },
	{ 0x7e2232fb, "ioread32" },
	{ 0x57860fb4, "wait_for_completion_timeout" },
	{ 0xef95a802, "pci_enable_device" },
	{ 0xfad8f384, "iowrite32" },
	{ 0x59b87546, "vCanAddCardChannel" },
	{ 0xd710adbf, "__kmalloc_noprof" },
	{ 0x954b0cc3, "pci_iomap" },
	{ 0x65026e43, "complete" },
	{ 0x49733ad6, "queue_work_on" },
	{ 0x39b5bb15, "queue_release" },
	{ 0x39b5bb15, "queue_reinit" },
	{ 0x60c9c0b3, "__init_swait_queue_head" },
	{ 0xc87f4bab, "finish_wait" },
	{ 0x59b87546, "vCanFlushSendBuffer" },
	{ 0x04cf7d01, "__pci_register_driver" },
	{ 0x645c8a85, "vCanInit" },
	{ 0xbd06710b, "pci_request_regions" },
	{ 0xa53f4e29, "memcpy" },
	{ 0xcb8b6ec6, "kfree" },
	{ 0x48feac32, "vCanGetCardInfo" },
	{ 0x0db8d68d, "prepare_to_wait_event" },
	{ 0x16ab4215, "__wake_up" },
	{ 0xe1e1f979, "_raw_spin_lock_irqsave" },
	{ 0xde338d9a, "_raw_spin_lock" },
	{ 0xc720a5c5, "pci_unregister_driver" },
	{ 0xd272d446, "__fentry__" },
	{ 0xc7ca1fbd, "_raw_read_unlock_irqrestore" },
	{ 0xe8213e80, "_printk" },
	{ 0x6ac784f4, "schedule_timeout" },
	{ 0xd272d446, "__stack_chk_fail" },
	{ 0x7870c5f2, "vCanGetCardInfo2" },
	{ 0xd710adbf, "__kmalloc_large_noprof" },
	{ 0x4d40f3a6, "const_pcpu_hot" },
	{ 0x78bbf245, "_raw_read_lock_irqsave" },
	{ 0xd9d667bd, "vCanInitData" },
	{ 0x90a48d82, "__ubsan_handle_out_of_bounds" },
	{ 0x7a5ffe84, "init_wait_entry" },
	{ 0x9126ce86, "request_threaded_irq" },
	{ 0xbd03ed67, "random_kmalloc_seed" },
	{ 0x39b5bb15, "queue_pop" },
	{ 0x39b5bb15, "queue_wakeup_on_space" },
	{ 0xba8e1447, "set_capability_value" },
	{ 0xe54e0a6b, "__fortify_panic" },
	{ 0x81a1a811, "_raw_spin_unlock_irqrestore" },
	{ 0x022d2c4d, "pci_iounmap" },
	{ 0x689ff9d2, "vCanDispatchEvent" },
	{ 0xe7db7ec6, "queue_front" },
	{ 0x27683a56, "memset" },
	{ 0xd272d446, "__x86_return_thunk" },
	{ 0xe7db7ec6, "queue_empty" },
	{ 0x5403c125, "__init_waitqueue_head" },
	{ 0x34e23247, "vCanRemoveCardChannel" },
	{ 0xc7ca1fbd, "_raw_write_unlock_irqrestore" },
	{ 0x2b718ccd, "pci_release_regions" },
	{ 0x70db3fe4, "__kmalloc_cache_noprof" },
	{ 0x75738bed, "__warn_printk" },
	{ 0x33ba6a25, "pci_disable_device" },
	{ 0x78bbf245, "_raw_write_lock_irqsave" },
	{ 0xe4de56b4, "__ubsan_handle_load_invalid_value" },
	{ 0xde338d9a, "_raw_spin_unlock" },
	{ 0x34583558, "vCanCleanup" },
	{ 0x7851be11, "__SCT__might_resched" },
	{ 0xfed1e3bc, "kmalloc_caches" },
	{ 0xaef1f20d, "system_wq" },
	{ 0xba157484, "module_layout" },
};

static const u32 ____version_ext_crcs[]
__used __section("__version_ext_crcs") = {
	0x9dd4105e,
	0x7e2232fb,
	0x57860fb4,
	0xef95a802,
	0xfad8f384,
	0x59b87546,
	0xd710adbf,
	0x954b0cc3,
	0x65026e43,
	0x49733ad6,
	0x39b5bb15,
	0x39b5bb15,
	0x60c9c0b3,
	0xc87f4bab,
	0x59b87546,
	0x04cf7d01,
	0x645c8a85,
	0xbd06710b,
	0xa53f4e29,
	0xcb8b6ec6,
	0x48feac32,
	0x0db8d68d,
	0x16ab4215,
	0xe1e1f979,
	0xde338d9a,
	0xc720a5c5,
	0xd272d446,
	0xc7ca1fbd,
	0xe8213e80,
	0x6ac784f4,
	0xd272d446,
	0x7870c5f2,
	0xd710adbf,
	0x4d40f3a6,
	0x78bbf245,
	0xd9d667bd,
	0x90a48d82,
	0x7a5ffe84,
	0x9126ce86,
	0xbd03ed67,
	0x39b5bb15,
	0x39b5bb15,
	0xba8e1447,
	0xe54e0a6b,
	0x81a1a811,
	0x022d2c4d,
	0x689ff9d2,
	0xe7db7ec6,
	0x27683a56,
	0xd272d446,
	0xe7db7ec6,
	0x5403c125,
	0x34e23247,
	0xc7ca1fbd,
	0x2b718ccd,
	0x70db3fe4,
	0x75738bed,
	0x33ba6a25,
	0x78bbf245,
	0xe4de56b4,
	0xde338d9a,
	0x34583558,
	0x7851be11,
	0xfed1e3bc,
	0xaef1f20d,
	0xba157484,
};
static const char ____version_ext_names[]
__used __section("__version_ext_names") =
	"free_irq\0"
	"ioread32\0"
	"wait_for_completion_timeout\0"
	"pci_enable_device\0"
	"iowrite32\0"
	"vCanAddCardChannel\0"
	"__kmalloc_noprof\0"
	"pci_iomap\0"
	"complete\0"
	"queue_work_on\0"
	"queue_release\0"
	"queue_reinit\0"
	"__init_swait_queue_head\0"
	"finish_wait\0"
	"vCanFlushSendBuffer\0"
	"__pci_register_driver\0"
	"vCanInit\0"
	"pci_request_regions\0"
	"memcpy\0"
	"kfree\0"
	"vCanGetCardInfo\0"
	"prepare_to_wait_event\0"
	"__wake_up\0"
	"_raw_spin_lock_irqsave\0"
	"_raw_spin_lock\0"
	"pci_unregister_driver\0"
	"__fentry__\0"
	"_raw_read_unlock_irqrestore\0"
	"_printk\0"
	"schedule_timeout\0"
	"__stack_chk_fail\0"
	"vCanGetCardInfo2\0"
	"__kmalloc_large_noprof\0"
	"const_pcpu_hot\0"
	"_raw_read_lock_irqsave\0"
	"vCanInitData\0"
	"__ubsan_handle_out_of_bounds\0"
	"init_wait_entry\0"
	"request_threaded_irq\0"
	"random_kmalloc_seed\0"
	"queue_pop\0"
	"queue_wakeup_on_space\0"
	"set_capability_value\0"
	"__fortify_panic\0"
	"_raw_spin_unlock_irqrestore\0"
	"pci_iounmap\0"
	"vCanDispatchEvent\0"
	"queue_front\0"
	"memset\0"
	"__x86_return_thunk\0"
	"queue_empty\0"
	"__init_waitqueue_head\0"
	"vCanRemoveCardChannel\0"
	"_raw_write_unlock_irqrestore\0"
	"pci_release_regions\0"
	"__kmalloc_cache_noprof\0"
	"__warn_printk\0"
	"pci_disable_device\0"
	"_raw_write_lock_irqsave\0"
	"__ubsan_handle_load_invalid_value\0"
	"_raw_spin_unlock\0"
	"vCanCleanup\0"
	"__SCT__might_resched\0"
	"kmalloc_caches\0"
	"system_wq\0"
	"module_layout\0"
;

MODULE_INFO(depends, "kvcommon");

MODULE_ALIAS("pci:v000010E8d00008407sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000006sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000009sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000007sv*sd*bc*sc*i*");

MODULE_INFO(srcversion, "2994A0672F63EE487B670E9");
