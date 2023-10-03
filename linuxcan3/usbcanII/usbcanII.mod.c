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
	{ 0xef31351c, "usb_alloc_urb" },
	{ 0x8514a6d5, "try_module_get" },
	{ 0x49cd25ed, "alloc_workqueue" },
	{ 0xef07e8e1, "usb_free_urb" },
	{ 0x4a3ad70e, "wait_for_completion_timeout" },
	{ 0x1eaab143, "vCanAddCardChannel" },
	{ 0x7f02188f, "__msecs_to_jiffies" },
	{ 0xf865343f, "usb_alloc_coherent" },
	{ 0xa6257a2f, "complete" },
	{ 0xc5b6f236, "queue_work_on" },
	{ 0x30372d96, "queue_release" },
	{ 0x55555880, "queue_reinit" },
	{ 0x244ab863, "queue_back" },
	{ 0x608741b5, "__init_swait_queue_head" },
	{ 0x10fa71db, "queue_remove_wait_for_space" },
	{ 0x914ccc00, "usb_register_driver" },
	{ 0x828398ff, "vCanFlushSendBuffer" },
	{ 0x1229cb50, "vCanInit" },
	{ 0x37a0cba, "kfree" },
	{ 0x166163ff, "vCanGetCardInfo" },
	{ 0xf72e8c06, "pcpu_hot" },
	{ 0xe2964344, "__wake_up" },
	{ 0x34db050b, "_raw_spin_lock_irqsave" },
	{ 0xba8fbd64, "_raw_spin_lock" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x33b2abe8, "wake_up_process" },
	{ 0x122c3a7e, "_printk" },
	{ 0x8ddd8aad, "schedule_timeout" },
	{ 0x8968d689, "usb_bulk_msg" },
	{ 0xa19b956, "__stack_chk_fail" },
	{ 0xec8d96be, "vCanGetCardInfo2" },
	{ 0x2e6c9f5a, "usb_submit_urb" },
	{ 0xb5385e3c, "vCanInitData" },
	{ 0x87a21cb3, "__ubsan_handle_out_of_bounds" },
	{ 0xffcd2306, "usb_free_coherent" },
	{ 0xf0034cbb, "__module_put_and_kthread_exit" },
	{ 0x8c03d20c, "destroy_workqueue" },
	{ 0x220f6eb0, "queue_pop" },
	{ 0xe6cf5658, "queue_wakeup_on_space" },
	{ 0x4a379bbf, "set_capability_value" },
	{ 0x9ed12e20, "kmalloc_large" },
	{ 0x21d81531, "usb_deregister" },
	{ 0xd35cce70, "_raw_spin_unlock_irqrestore" },
	{ 0xffd473e4, "vCanDispatchEvent" },
	{ 0x87d7787f, "queue_add_wait_for_space" },
	{ 0xfaa20ff6, "queue_front" },
	{ 0xfb578fc5, "memset" },
	{ 0x25974000, "wait_for_completion" },
	{ 0x9166fc03, "__flush_workqueue" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0x6782eeca, "queue_push" },
	{ 0x679e43d1, "queue_empty" },
	{ 0xaad8c7d6, "default_wake_function" },
	{ 0xafec5d3, "vCanRemoveCardChannel" },
	{ 0xd8025f97, "kthread_create_on_node" },
	{ 0x7b0c27e0, "usb_kill_urb" },
	{ 0x56470118, "__warn_printk" },
	{ 0xa02aea3a, "queue_length" },
	{ 0x850e6a88, "kmalloc_trace" },
	{ 0x54b1fac6, "__ubsan_handle_load_invalid_value" },
	{ 0xb5b54b34, "_raw_spin_unlock" },
	{ 0x86204941, "vCanCleanup" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0xfe2fd6f8, "queue_init" },
	{ 0xad6d045f, "kmalloc_caches" },
	{ 0x2d3385d3, "system_wq" },
	{ 0x453e7dc, "module_layout" },
};

MODULE_INFO(depends, "kvcommon");

MODULE_ALIAS("usb:v0BFDp0004d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0002d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0005d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0003d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "A4FB0D8956B021E9E887777");
