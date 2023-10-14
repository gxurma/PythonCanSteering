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

SYMBOL_CRC(vCanTime, 0x84f435c1, "");
SYMBOL_CRC(kv_do_gettimeofday, 0x88c2dbba, "");
SYMBOL_CRC(vCanCalc_dt, 0x118238a0, "");
SYMBOL_CRC(vCanSupportsBusParamsTq, 0xe6c6764e, "");
SYMBOL_CRC(vCanFlushSendBuffer, 0x828398ff, "");
SYMBOL_CRC(vCanGetCardInfo, 0x166163ff, "");
SYMBOL_CRC(vCanGetCardInfo2, 0xec8d96be, "");
SYMBOL_CRC(vCanAddCardChannel, 0x1eaab143, "");
SYMBOL_CRC(vCanRemoveCardChannel, 0x0afec5d3, "");
SYMBOL_CRC(vCanDispatchEvent, 0xffd473e4, "");
SYMBOL_CRC(vCanDispatchPrintfEvent, 0x2dc3d54c, "");
SYMBOL_CRC(vCanInitData, 0xb5385e3c, "");
SYMBOL_CRC(vCanInit, 0x1229cb50, "");
SYMBOL_CRC(vCanCleanup, 0x86204941, "");
SYMBOL_CRC(queue_reinit, 0x55555880, "");
SYMBOL_CRC(queue_init, 0xfe2fd6f8, "");
SYMBOL_CRC(queue_irq_lock, 0x206ebad6, "");
SYMBOL_CRC(queue_length, 0xa02aea3a, "");
SYMBOL_CRC(queue_empty, 0x679e43d1, "");
SYMBOL_CRC(queue_back, 0x244ab863, "");
SYMBOL_CRC(queue_push, 0x6782eeca, "");
SYMBOL_CRC(queue_front, 0xfaa20ff6, "");
SYMBOL_CRC(queue_pop, 0x220f6eb0, "");
SYMBOL_CRC(queue_release, 0x30372d96, "");
SYMBOL_CRC(queue_add_wait_for_space, 0x87d7787f, "");
SYMBOL_CRC(queue_remove_wait_for_space, 0x10fa71db, "");
SYMBOL_CRC(queue_wakeup_on_space, 0xe6cf5658, "");
SYMBOL_CRC(calculateCRC32, 0x235ea4c1, "");
SYMBOL_CRC(packed_EAN_to_BCD_with_csum, 0xfd06f019, "");
SYMBOL_CRC(get_usb_root_hub_id, 0x9a8e7a78, "");
SYMBOL_CRC(softSyncLoc2Glob, 0x0b3939f9, "");
SYMBOL_CRC(softSyncHandleTRef, 0xf5b634f0, "");
SYMBOL_CRC(softSyncAddMember, 0x1dfbaca0, "");
SYMBOL_CRC(softSyncRemoveMember, 0x87451115, "");
SYMBOL_CRC(softSyncGetTRefList, 0xbf8182fa, "");
SYMBOL_CRC(set_capability_value, 0x4a379bbf, "");
SYMBOL_CRC(set_capability_mask, 0x30d1029a, "");
SYMBOL_CRC(convert_vcan_to_hydra_cmd, 0x15388bbc, "");
SYMBOL_CRC(card_has_capability, 0x358a4e46, "");
SYMBOL_CRC(card_has_capability_ex, 0x204683ad, "");
SYMBOL_CRC(set_capability_ex_value, 0x803ad55b, "");
SYMBOL_CRC(set_capability_ex_mask, 0xb0d3a1c6, "");
SYMBOL_CRC(convert_vcan_ex_to_hydra_cmd, 0x752b9cc1, "");
SYMBOL_CRC(dlc_bytes_to_dlc_fd, 0xbfaf25a3, "");
SYMBOL_CRC(dlc_dlc_to_bytes_fd, 0x63fbdd18, "");
SYMBOL_CRC(dlc_is_dlc_ok, 0xab1ad228, "");
SYMBOL_CRC(dlc_dlc_to_bytes_classic, 0xede295c6, "");
SYMBOL_CRC(ticks_init, 0x2289f050, "");
SYMBOL_CRC(ticks_to_64bit_ns, 0x6adf812a, "");

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xe3ec2f2b, "alloc_chrdev_region" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x49cd25ed, "alloc_workqueue" },
	{ 0xeea3c1d8, "__class_create" },
	{ 0x13c49cc2, "_copy_from_user" },
	{ 0x7f02188f, "__msecs_to_jiffies" },
	{ 0xa6257a2f, "complete" },
	{ 0xc5b6f236, "queue_work_on" },
	{ 0x608741b5, "__init_swait_queue_head" },
	{ 0x92540fbf, "finish_wait" },
	{ 0x6a2dd7c, "class_destroy" },
	{ 0x37a0cba, "kfree" },
	{ 0xf72e8c06, "pcpu_hot" },
	{ 0x4afb2238, "add_wait_queue" },
	{ 0x8c26d495, "prepare_to_wait_event" },
	{ 0xe2964344, "__wake_up" },
	{ 0x34db050b, "_raw_spin_lock_irqsave" },
	{ 0xba8fbd64, "_raw_spin_lock" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x65487097, "__x86_indirect_thunk_rax" },
	{ 0x122c3a7e, "_printk" },
	{ 0x6d334118, "__get_user_8" },
	{ 0x1000e51, "schedule" },
	{ 0x8ddd8aad, "schedule_timeout" },
	{ 0xa19b956, "__stack_chk_fail" },
	{ 0xe46021ca, "_raw_spin_unlock_bh" },
	{ 0x7682ba4e, "__copy_overflow" },
	{ 0xb2fd5ceb, "__put_user_4" },
	{ 0x6383b27c, "__x86_indirect_thunk_rdx" },
	{ 0x87a21cb3, "__ubsan_handle_out_of_bounds" },
	{ 0x2dcc02c1, "cdev_add" },
	{ 0xfe487975, "init_wait_entry" },
	{ 0x4c0ac327, "device_create" },
	{ 0x8c03d20c, "destroy_workqueue" },
	{ 0xc3aaf0a9, "__put_user_1" },
	{ 0x9166fada, "strncpy" },
	{ 0x9ec6ca96, "ktime_get_real_ts64" },
	{ 0x9ed12e20, "kmalloc_large" },
	{ 0xd35cce70, "_raw_spin_unlock_irqrestore" },
	{ 0xfb578fc5, "memset" },
	{ 0xb8e7ce2c, "__put_user_8" },
	{ 0x25974000, "wait_for_completion" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0x6b10bee1, "_copy_to_user" },
	{ 0xd9a5ea54, "__init_waitqueue_head" },
	{ 0xfb384d37, "kasprintf" },
	{ 0xa648e561, "__ubsan_handle_shift_out_of_bounds" },
	{ 0x167e7f9d, "__get_user_1" },
	{ 0x6091b333, "unregister_chrdev_region" },
	{ 0x66cca4f9, "__x86_indirect_thunk_rcx" },
	{ 0x6729d3df, "__get_user_4" },
	{ 0x7e38d25d, "device_destroy" },
	{ 0xc3690fc, "_raw_spin_lock_bh" },
	{ 0x37110088, "remove_wait_queue" },
	{ 0x850e6a88, "kmalloc_trace" },
	{ 0xb5b54b34, "_raw_spin_unlock" },
	{ 0xf90a1e85, "__x86_indirect_thunk_r8" },
	{ 0x32ab4392, "cdev_init" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0xe2c17b5d, "__SCT__might_resched" },
	{ 0xad6d045f, "kmalloc_caches" },
	{ 0xf7fb9e48, "cdev_del" },
	{ 0x453e7dc, "module_layout" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "C83F17716F4E29A0D587420");
