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
	{ 0x0dba6eb8, "usb_alloc_urb" },
	{ 0xdf4bee3d, "alloc_workqueue" },
	{ 0xd6d46b9d, "usb_free_urb" },
	{ 0x6ad5179b, "get_usb_root_hub_id" },
	{ 0x57860fb4, "wait_for_completion_timeout" },
	{ 0x2502e48b, "dlc_dlc_to_bytes_classic" },
	{ 0x6579be82, "vCanDispatchPrintfEvent" },
	{ 0x59b87546, "vCanAddCardChannel" },
	{ 0x534ed5f3, "__msecs_to_jiffies" },
	{ 0xd710adbf, "__kmalloc_noprof" },
	{ 0x2502e48b, "dlc_dlc_to_bytes_fd" },
	{ 0x2a87283a, "usb_alloc_coherent" },
	{ 0x65026e43, "complete" },
	{ 0x49733ad6, "queue_work_on" },
	{ 0x39b5bb15, "queue_release" },
	{ 0x39b5bb15, "queue_reinit" },
	{ 0xe7db7ec6, "queue_back" },
	{ 0x60c9c0b3, "__init_swait_queue_head" },
	{ 0x4cea2553, "queue_remove_wait_for_space" },
	{ 0xaba46e12, "usb_register_driver" },
	{ 0x59b87546, "vCanFlushSendBuffer" },
	{ 0x7f6d5e1a, "__put_task_struct" },
	{ 0x645c8a85, "vCanInit" },
	{ 0xa53f4e29, "memcpy" },
	{ 0xcb8b6ec6, "kfree" },
	{ 0x5e505530, "kthread_should_stop" },
	{ 0x50a79768, "softSyncRemoveMember" },
	{ 0x16ab4215, "__wake_up" },
	{ 0xba8e1447, "set_capability_mask" },
	{ 0xe1e1f979, "_raw_spin_lock_irqsave" },
	{ 0xde338d9a, "_raw_spin_lock" },
	{ 0xa7665c08, "dlc_bytes_to_dlc_fd" },
	{ 0xd272d446, "__fentry__" },
	{ 0xda80ecf4, "wake_up_process" },
	{ 0xe8213e80, "_printk" },
	{ 0x6ac784f4, "schedule_timeout" },
	{ 0x76a26ca1, "usb_bulk_msg" },
	{ 0xd272d446, "__stack_chk_fail" },
	{ 0x2520ea93, "refcount_warn_saturate" },
	{ 0xcfc54b4a, "set_capability_ex_value" },
	{ 0xd710adbf, "__kmalloc_large_noprof" },
	{ 0x4d40f3a6, "const_pcpu_hot" },
	{ 0x0819dba7, "usb_submit_urb" },
	{ 0xd9d667bd, "vCanInitData" },
	{ 0x90a48d82, "__ubsan_handle_out_of_bounds" },
	{ 0x355ac0b5, "softSyncHandleTRef" },
	{ 0xc9dfc516, "vCanCalc_dt" },
	{ 0x32cd3258, "usb_free_coherent" },
	{ 0xbd03ed67, "random_kmalloc_seed" },
	{ 0xbeb1d261, "destroy_workqueue" },
	{ 0x39b5bb15, "queue_pop" },
	{ 0x39b5bb15, "queue_wakeup_on_space" },
	{ 0xd6d46b9d, "usb_poison_urb" },
	{ 0xc609ff70, "strncpy" },
	{ 0xcfc54b4a, "set_capability_ex_mask" },
	{ 0xba8e1447, "set_capability_value" },
	{ 0xde9f3bec, "ticks_to_64bit_ns" },
	{ 0x732dd6e2, "kthread_stop" },
	{ 0xef4e4365, "usb_deregister" },
	{ 0xe54e0a6b, "__fortify_panic" },
	{ 0x81a1a811, "_raw_spin_unlock_irqrestore" },
	{ 0x689ff9d2, "vCanDispatchEvent" },
	{ 0x4cea2553, "queue_add_wait_for_space" },
	{ 0xe7db7ec6, "queue_front" },
	{ 0x27683a56, "memset" },
	{ 0x278ef35d, "ticks_init" },
	{ 0x65026e43, "wait_for_completion" },
	{ 0xd272d446, "__x86_return_thunk" },
	{ 0x39b5bb15, "queue_push" },
	{ 0xe7db7ec6, "queue_empty" },
	{ 0x2247bd2b, "default_wake_function" },
	{ 0x34e23247, "vCanRemoveCardChannel" },
	{ 0x8fdc4711, "kthread_create_on_node" },
	{ 0xaddd9dda, "softSyncAddMember" },
	{ 0x3f35b56e, "usb_unlink_urb" },
	{ 0xc5b77680, "softSyncLoc2Glob" },
	{ 0x82fd7238, "__ubsan_handle_shift_out_of_bounds" },
	{ 0xacba77f5, "convert_vcan_to_hydra_cmd" },
	{ 0x70db3fe4, "__kmalloc_cache_noprof" },
	{ 0x2d88a3ab, "cancel_work_sync" },
	{ 0x75738bed, "__warn_printk" },
	{ 0xe7db7ec6, "queue_length" },
	{ 0xe525afc2, "kv_do_gettimeofday" },
	{ 0xe4de56b4, "__ubsan_handle_load_invalid_value" },
	{ 0xde338d9a, "_raw_spin_unlock" },
	{ 0x34583558, "vCanCleanup" },
	{ 0x8ac3b8f9, "queue_init" },
	{ 0xfed1e3bc, "kmalloc_caches" },
	{ 0x93642ce3, "convert_vcan_ex_to_hydra_cmd" },
	{ 0xaef1f20d, "system_wq" },
	{ 0xba157484, "module_layout" },
};

static const u32 ____version_ext_crcs[]
__used __section("__version_ext_crcs") = {
	0x0dba6eb8,
	0xdf4bee3d,
	0xd6d46b9d,
	0x6ad5179b,
	0x57860fb4,
	0x2502e48b,
	0x6579be82,
	0x59b87546,
	0x534ed5f3,
	0xd710adbf,
	0x2502e48b,
	0x2a87283a,
	0x65026e43,
	0x49733ad6,
	0x39b5bb15,
	0x39b5bb15,
	0xe7db7ec6,
	0x60c9c0b3,
	0x4cea2553,
	0xaba46e12,
	0x59b87546,
	0x7f6d5e1a,
	0x645c8a85,
	0xa53f4e29,
	0xcb8b6ec6,
	0x5e505530,
	0x50a79768,
	0x16ab4215,
	0xba8e1447,
	0xe1e1f979,
	0xde338d9a,
	0xa7665c08,
	0xd272d446,
	0xda80ecf4,
	0xe8213e80,
	0x6ac784f4,
	0x76a26ca1,
	0xd272d446,
	0x2520ea93,
	0xcfc54b4a,
	0xd710adbf,
	0x4d40f3a6,
	0x0819dba7,
	0xd9d667bd,
	0x90a48d82,
	0x355ac0b5,
	0xc9dfc516,
	0x32cd3258,
	0xbd03ed67,
	0xbeb1d261,
	0x39b5bb15,
	0x39b5bb15,
	0xd6d46b9d,
	0xc609ff70,
	0xcfc54b4a,
	0xba8e1447,
	0xde9f3bec,
	0x732dd6e2,
	0xef4e4365,
	0xe54e0a6b,
	0x81a1a811,
	0x689ff9d2,
	0x4cea2553,
	0xe7db7ec6,
	0x27683a56,
	0x278ef35d,
	0x65026e43,
	0xd272d446,
	0x39b5bb15,
	0xe7db7ec6,
	0x2247bd2b,
	0x34e23247,
	0x8fdc4711,
	0xaddd9dda,
	0x3f35b56e,
	0xc5b77680,
	0x82fd7238,
	0xacba77f5,
	0x70db3fe4,
	0x2d88a3ab,
	0x75738bed,
	0xe7db7ec6,
	0xe525afc2,
	0xe4de56b4,
	0xde338d9a,
	0x34583558,
	0x8ac3b8f9,
	0xfed1e3bc,
	0x93642ce3,
	0xaef1f20d,
	0xba157484,
};
static const char ____version_ext_names[]
__used __section("__version_ext_names") =
	"usb_alloc_urb\0"
	"alloc_workqueue\0"
	"usb_free_urb\0"
	"get_usb_root_hub_id\0"
	"wait_for_completion_timeout\0"
	"dlc_dlc_to_bytes_classic\0"
	"vCanDispatchPrintfEvent\0"
	"vCanAddCardChannel\0"
	"__msecs_to_jiffies\0"
	"__kmalloc_noprof\0"
	"dlc_dlc_to_bytes_fd\0"
	"usb_alloc_coherent\0"
	"complete\0"
	"queue_work_on\0"
	"queue_release\0"
	"queue_reinit\0"
	"queue_back\0"
	"__init_swait_queue_head\0"
	"queue_remove_wait_for_space\0"
	"usb_register_driver\0"
	"vCanFlushSendBuffer\0"
	"__put_task_struct\0"
	"vCanInit\0"
	"memcpy\0"
	"kfree\0"
	"kthread_should_stop\0"
	"softSyncRemoveMember\0"
	"__wake_up\0"
	"set_capability_mask\0"
	"_raw_spin_lock_irqsave\0"
	"_raw_spin_lock\0"
	"dlc_bytes_to_dlc_fd\0"
	"__fentry__\0"
	"wake_up_process\0"
	"_printk\0"
	"schedule_timeout\0"
	"usb_bulk_msg\0"
	"__stack_chk_fail\0"
	"refcount_warn_saturate\0"
	"set_capability_ex_value\0"
	"__kmalloc_large_noprof\0"
	"const_pcpu_hot\0"
	"usb_submit_urb\0"
	"vCanInitData\0"
	"__ubsan_handle_out_of_bounds\0"
	"softSyncHandleTRef\0"
	"vCanCalc_dt\0"
	"usb_free_coherent\0"
	"random_kmalloc_seed\0"
	"destroy_workqueue\0"
	"queue_pop\0"
	"queue_wakeup_on_space\0"
	"usb_poison_urb\0"
	"strncpy\0"
	"set_capability_ex_mask\0"
	"set_capability_value\0"
	"ticks_to_64bit_ns\0"
	"kthread_stop\0"
	"usb_deregister\0"
	"__fortify_panic\0"
	"_raw_spin_unlock_irqrestore\0"
	"vCanDispatchEvent\0"
	"queue_add_wait_for_space\0"
	"queue_front\0"
	"memset\0"
	"ticks_init\0"
	"wait_for_completion\0"
	"__x86_return_thunk\0"
	"queue_push\0"
	"queue_empty\0"
	"default_wake_function\0"
	"vCanRemoveCardChannel\0"
	"kthread_create_on_node\0"
	"softSyncAddMember\0"
	"usb_unlink_urb\0"
	"softSyncLoc2Glob\0"
	"__ubsan_handle_shift_out_of_bounds\0"
	"convert_vcan_to_hydra_cmd\0"
	"__kmalloc_cache_noprof\0"
	"cancel_work_sync\0"
	"__warn_printk\0"
	"queue_length\0"
	"kv_do_gettimeofday\0"
	"__ubsan_handle_load_invalid_value\0"
	"_raw_spin_unlock\0"
	"vCanCleanup\0"
	"queue_init\0"
	"kmalloc_caches\0"
	"convert_vcan_ex_to_hydra_cmd\0"
	"system_wq\0"
	"module_layout\0"
;

MODULE_INFO(depends, "kvcommon");

MODULE_ALIAS("usb:v0BFDp0100d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0102d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0104d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0105d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0106d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0107d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0108d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0109d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp010Ad*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp010Bd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp010Cd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp010Dd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp010Ed*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp010Fd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0110d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0111d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0112d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0113d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0114d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0115d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0116d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0117d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0118d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0119d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp011Ad*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp011Bd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp011Cd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp011Dd*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "C727CEDA12C8E15C97AA722");
