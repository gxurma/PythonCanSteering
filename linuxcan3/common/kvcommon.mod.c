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

KSYMTAB_FUNC(vCanTime, "", "");
KSYMTAB_FUNC(kv_do_gettimeofday, "", "");
KSYMTAB_FUNC(vCanCalc_dt, "", "");
KSYMTAB_FUNC(vCanSupportsBusParamsTq, "", "");
KSYMTAB_FUNC(vCanFlushSendBuffer, "", "");
KSYMTAB_FUNC(vCanGetCardInfo, "", "");
KSYMTAB_FUNC(vCanGetCardInfo2, "", "");
KSYMTAB_FUNC(vCanAddCardChannel, "", "");
KSYMTAB_FUNC(vCanRemoveCardChannel, "", "");
KSYMTAB_FUNC(vCanDispatchEvent, "", "");
KSYMTAB_FUNC(vCanDispatchPrintfEvent, "", "");
KSYMTAB_FUNC(vCanInitData, "", "");
KSYMTAB_FUNC(vCanInit, "", "");
KSYMTAB_FUNC(vCanCleanup, "", "");
KSYMTAB_FUNC(queue_reinit, "", "");
KSYMTAB_FUNC(queue_init, "", "");
KSYMTAB_FUNC(queue_irq_lock, "", "");
KSYMTAB_FUNC(queue_length, "", "");
KSYMTAB_FUNC(queue_empty, "", "");
KSYMTAB_FUNC(queue_back, "", "");
KSYMTAB_FUNC(queue_push, "", "");
KSYMTAB_FUNC(queue_front, "", "");
KSYMTAB_FUNC(queue_pop, "", "");
KSYMTAB_FUNC(queue_release, "", "");
KSYMTAB_FUNC(queue_add_wait_for_space, "", "");
KSYMTAB_FUNC(queue_remove_wait_for_space, "", "");
KSYMTAB_FUNC(queue_wakeup_on_space, "", "");
KSYMTAB_FUNC(calculateCRC32, "", "");
KSYMTAB_FUNC(packed_EAN_to_BCD_with_csum, "", "");
KSYMTAB_FUNC(get_usb_root_hub_id, "", "");
KSYMTAB_FUNC(softSyncLoc2Glob, "", "");
KSYMTAB_FUNC(softSyncHandleTRef, "", "");
KSYMTAB_FUNC(softSyncAddMember, "", "");
KSYMTAB_FUNC(softSyncRemoveMember, "", "");
KSYMTAB_FUNC(softSyncGetTRefList, "", "");
KSYMTAB_FUNC(set_capability_value, "", "");
KSYMTAB_FUNC(set_capability_mask, "", "");
KSYMTAB_FUNC(convert_vcan_to_hydra_cmd, "", "");
KSYMTAB_FUNC(card_has_capability, "", "");
KSYMTAB_FUNC(card_has_capability_ex, "", "");
KSYMTAB_FUNC(set_capability_ex_value, "", "");
KSYMTAB_FUNC(set_capability_ex_mask, "", "");
KSYMTAB_FUNC(convert_vcan_ex_to_hydra_cmd, "", "");
KSYMTAB_FUNC(dlc_bytes_to_dlc_fd, "", "");
KSYMTAB_FUNC(dlc_dlc_to_bytes_fd, "", "");
KSYMTAB_FUNC(dlc_is_dlc_ok, "", "");
KSYMTAB_FUNC(dlc_dlc_to_bytes_classic, "", "");
KSYMTAB_FUNC(ticks_init, "", "");
KSYMTAB_FUNC(ticks_to_64bit_ns, "", "");

SYMBOL_CRC(vCanTime, 0xb5cbfe81, "");
SYMBOL_CRC(kv_do_gettimeofday, 0xe525afc2, "");
SYMBOL_CRC(vCanCalc_dt, 0xc9dfc516, "");
SYMBOL_CRC(vCanSupportsBusParamsTq, 0x59b87546, "");
SYMBOL_CRC(vCanFlushSendBuffer, 0x59b87546, "");
SYMBOL_CRC(vCanGetCardInfo, 0x48feac32, "");
SYMBOL_CRC(vCanGetCardInfo2, 0x7870c5f2, "");
SYMBOL_CRC(vCanAddCardChannel, 0x59b87546, "");
SYMBOL_CRC(vCanRemoveCardChannel, 0x34e23247, "");
SYMBOL_CRC(vCanDispatchEvent, 0x689ff9d2, "");
SYMBOL_CRC(vCanDispatchPrintfEvent, 0x6579be82, "");
SYMBOL_CRC(vCanInitData, 0xd9d667bd, "");
SYMBOL_CRC(vCanInit, 0x645c8a85, "");
SYMBOL_CRC(vCanCleanup, 0x34583558, "");
SYMBOL_CRC(queue_reinit, 0x39b5bb15, "");
SYMBOL_CRC(queue_init, 0x8ac3b8f9, "");
SYMBOL_CRC(queue_irq_lock, 0x39b5bb15, "");
SYMBOL_CRC(queue_length, 0xe7db7ec6, "");
SYMBOL_CRC(queue_empty, 0xe7db7ec6, "");
SYMBOL_CRC(queue_back, 0xe7db7ec6, "");
SYMBOL_CRC(queue_push, 0x39b5bb15, "");
SYMBOL_CRC(queue_front, 0xe7db7ec6, "");
SYMBOL_CRC(queue_pop, 0x39b5bb15, "");
SYMBOL_CRC(queue_release, 0x39b5bb15, "");
SYMBOL_CRC(queue_add_wait_for_space, 0x4cea2553, "");
SYMBOL_CRC(queue_remove_wait_for_space, 0x4cea2553, "");
SYMBOL_CRC(queue_wakeup_on_space, 0x39b5bb15, "");
SYMBOL_CRC(calculateCRC32, 0x7a3ad30b, "");
SYMBOL_CRC(packed_EAN_to_BCD_with_csum, 0x9d6f0248, "");
SYMBOL_CRC(get_usb_root_hub_id, 0x6ad5179b, "");
SYMBOL_CRC(softSyncLoc2Glob, 0xc5b77680, "");
SYMBOL_CRC(softSyncHandleTRef, 0x355ac0b5, "");
SYMBOL_CRC(softSyncAddMember, 0xaddd9dda, "");
SYMBOL_CRC(softSyncRemoveMember, 0x50a79768, "");
SYMBOL_CRC(softSyncGetTRefList, 0xf4bc80cb, "");
SYMBOL_CRC(set_capability_value, 0xba8e1447, "");
SYMBOL_CRC(set_capability_mask, 0xba8e1447, "");
SYMBOL_CRC(convert_vcan_to_hydra_cmd, 0xacba77f5, "");
SYMBOL_CRC(card_has_capability, 0xb0dfe37a, "");
SYMBOL_CRC(card_has_capability_ex, 0xa1fdbbbb, "");
SYMBOL_CRC(set_capability_ex_value, 0xcfc54b4a, "");
SYMBOL_CRC(set_capability_ex_mask, 0xcfc54b4a, "");
SYMBOL_CRC(convert_vcan_ex_to_hydra_cmd, 0x93642ce3, "");
SYMBOL_CRC(dlc_bytes_to_dlc_fd, 0xa7665c08, "");
SYMBOL_CRC(dlc_dlc_to_bytes_fd, 0x2502e48b, "");
SYMBOL_CRC(dlc_is_dlc_ok, 0xbabca771, "");
SYMBOL_CRC(dlc_dlc_to_bytes_classic, 0x2502e48b, "");
SYMBOL_CRC(ticks_init, 0x278ef35d, "");
SYMBOL_CRC(ticks_to_64bit_ns, 0xde9f3bec, "");

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x9f222e1e, "alloc_chrdev_region" },
	{ 0xa61fd7aa, "__check_object_size" },
	{ 0xdf4bee3d, "alloc_workqueue" },
	{ 0x092a35a2, "_copy_from_user" },
	{ 0x534ed5f3, "__msecs_to_jiffies" },
	{ 0xd710adbf, "__kmalloc_noprof" },
	{ 0x65026e43, "complete" },
	{ 0x49733ad6, "queue_work_on" },
	{ 0x60c9c0b3, "__init_swait_queue_head" },
	{ 0xc87f4bab, "finish_wait" },
	{ 0x14fcde53, "class_destroy" },
	{ 0xa53f4e29, "memcpy" },
	{ 0xcb8b6ec6, "kfree" },
	{ 0xc87f4bab, "add_wait_queue" },
	{ 0x0db8d68d, "prepare_to_wait_event" },
	{ 0x16ab4215, "__wake_up" },
	{ 0xe1e1f979, "_raw_spin_lock_irqsave" },
	{ 0xde338d9a, "_raw_spin_lock" },
	{ 0xd272d446, "__fentry__" },
	{ 0x5a844b26, "__x86_indirect_thunk_rax" },
	{ 0xe8213e80, "_printk" },
	{ 0x7851be11, "__get_user_8" },
	{ 0xd272d446, "schedule" },
	{ 0x6ac784f4, "schedule_timeout" },
	{ 0xd272d446, "__stack_chk_fail" },
	{ 0xde338d9a, "_raw_spin_unlock_bh" },
	{ 0xd710adbf, "__kmalloc_large_noprof" },
	{ 0xf64ac983, "__copy_overflow" },
	{ 0xd272d446, "__put_user_4" },
	{ 0x4d40f3a6, "const_pcpu_hot" },
	{ 0x5a844b26, "__x86_indirect_thunk_rdx" },
	{ 0x90a48d82, "__ubsan_handle_out_of_bounds" },
	{ 0x4c1dbbd9, "cdev_add" },
	{ 0x7a5ffe84, "init_wait_entry" },
	{ 0xf98f93a7, "device_create" },
	{ 0xea5ac1d9, "class_create" },
	{ 0xbd03ed67, "random_kmalloc_seed" },
	{ 0xbeb1d261, "destroy_workqueue" },
	{ 0xf46d5bf3, "mutex_lock" },
	{ 0xd272d446, "__put_user_1" },
	{ 0xc609ff70, "strncpy" },
	{ 0x680628e7, "ktime_get_real_ts64" },
	{ 0xc1e6c71e, "__mutex_init" },
	{ 0x81a1a811, "_raw_spin_unlock_irqrestore" },
	{ 0x27683a56, "memset" },
	{ 0xd272d446, "__put_user_8" },
	{ 0x65026e43, "wait_for_completion" },
	{ 0xd272d446, "__x86_return_thunk" },
	{ 0x092a35a2, "_copy_to_user" },
	{ 0x5403c125, "__init_waitqueue_head" },
	{ 0xec203997, "kasprintf" },
	{ 0x82fd7238, "__ubsan_handle_shift_out_of_bounds" },
	{ 0x7851be11, "__get_user_1" },
	{ 0x0bc5fb0d, "unregister_chrdev_region" },
	{ 0xf46d5bf3, "mutex_unlock" },
	{ 0x5a844b26, "__x86_indirect_thunk_rcx" },
	{ 0x7851be11, "__get_user_4" },
	{ 0x6fdeeff0, "device_destroy" },
	{ 0x70db3fe4, "__kmalloc_cache_noprof" },
	{ 0x75738bed, "__warn_printk" },
	{ 0xde338d9a, "_raw_spin_lock_bh" },
	{ 0xc87f4bab, "remove_wait_queue" },
	{ 0xe4de56b4, "__ubsan_handle_load_invalid_value" },
	{ 0xde338d9a, "_raw_spin_unlock" },
	{ 0x5a844b26, "__x86_indirect_thunk_r8" },
	{ 0xefd5d5d8, "cdev_init" },
	{ 0x7851be11, "__SCT__might_resched" },
	{ 0xfed1e3bc, "kmalloc_caches" },
	{ 0x0c72f9ad, "cdev_del" },
	{ 0xba157484, "module_layout" },
};

static const u32 ____version_ext_crcs[]
__used __section("__version_ext_crcs") = {
	0x9f222e1e,
	0xa61fd7aa,
	0xdf4bee3d,
	0x092a35a2,
	0x534ed5f3,
	0xd710adbf,
	0x65026e43,
	0x49733ad6,
	0x60c9c0b3,
	0xc87f4bab,
	0x14fcde53,
	0xa53f4e29,
	0xcb8b6ec6,
	0xc87f4bab,
	0x0db8d68d,
	0x16ab4215,
	0xe1e1f979,
	0xde338d9a,
	0xd272d446,
	0x5a844b26,
	0xe8213e80,
	0x7851be11,
	0xd272d446,
	0x6ac784f4,
	0xd272d446,
	0xde338d9a,
	0xd710adbf,
	0xf64ac983,
	0xd272d446,
	0x4d40f3a6,
	0x5a844b26,
	0x90a48d82,
	0x4c1dbbd9,
	0x7a5ffe84,
	0xf98f93a7,
	0xea5ac1d9,
	0xbd03ed67,
	0xbeb1d261,
	0xf46d5bf3,
	0xd272d446,
	0xc609ff70,
	0x680628e7,
	0xc1e6c71e,
	0x81a1a811,
	0x27683a56,
	0xd272d446,
	0x65026e43,
	0xd272d446,
	0x092a35a2,
	0x5403c125,
	0xec203997,
	0x82fd7238,
	0x7851be11,
	0x0bc5fb0d,
	0xf46d5bf3,
	0x5a844b26,
	0x7851be11,
	0x6fdeeff0,
	0x70db3fe4,
	0x75738bed,
	0xde338d9a,
	0xc87f4bab,
	0xe4de56b4,
	0xde338d9a,
	0x5a844b26,
	0xefd5d5d8,
	0x7851be11,
	0xfed1e3bc,
	0x0c72f9ad,
	0xba157484,
};
static const char ____version_ext_names[]
__used __section("__version_ext_names") =
	"alloc_chrdev_region\0"
	"__check_object_size\0"
	"alloc_workqueue\0"
	"_copy_from_user\0"
	"__msecs_to_jiffies\0"
	"__kmalloc_noprof\0"
	"complete\0"
	"queue_work_on\0"
	"__init_swait_queue_head\0"
	"finish_wait\0"
	"class_destroy\0"
	"memcpy\0"
	"kfree\0"
	"add_wait_queue\0"
	"prepare_to_wait_event\0"
	"__wake_up\0"
	"_raw_spin_lock_irqsave\0"
	"_raw_spin_lock\0"
	"__fentry__\0"
	"__x86_indirect_thunk_rax\0"
	"_printk\0"
	"__get_user_8\0"
	"schedule\0"
	"schedule_timeout\0"
	"__stack_chk_fail\0"
	"_raw_spin_unlock_bh\0"
	"__kmalloc_large_noprof\0"
	"__copy_overflow\0"
	"__put_user_4\0"
	"const_pcpu_hot\0"
	"__x86_indirect_thunk_rdx\0"
	"__ubsan_handle_out_of_bounds\0"
	"cdev_add\0"
	"init_wait_entry\0"
	"device_create\0"
	"class_create\0"
	"random_kmalloc_seed\0"
	"destroy_workqueue\0"
	"mutex_lock\0"
	"__put_user_1\0"
	"strncpy\0"
	"ktime_get_real_ts64\0"
	"__mutex_init\0"
	"_raw_spin_unlock_irqrestore\0"
	"memset\0"
	"__put_user_8\0"
	"wait_for_completion\0"
	"__x86_return_thunk\0"
	"_copy_to_user\0"
	"__init_waitqueue_head\0"
	"kasprintf\0"
	"__ubsan_handle_shift_out_of_bounds\0"
	"__get_user_1\0"
	"unregister_chrdev_region\0"
	"mutex_unlock\0"
	"__x86_indirect_thunk_rcx\0"
	"__get_user_4\0"
	"device_destroy\0"
	"__kmalloc_cache_noprof\0"
	"__warn_printk\0"
	"_raw_spin_lock_bh\0"
	"remove_wait_queue\0"
	"__ubsan_handle_load_invalid_value\0"
	"_raw_spin_unlock\0"
	"__x86_indirect_thunk_r8\0"
	"cdev_init\0"
	"__SCT__might_resched\0"
	"kmalloc_caches\0"
	"cdev_del\0"
	"module_layout\0"
;

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "59F9BB295A19C30C5247EE6");
