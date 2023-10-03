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
	{ 0xc1514a3b, "free_irq" },
	{ 0xc31db0ce, "is_vmalloc_addr" },
	{ 0xa78af5f3, "ioread32" },
	{ 0x4a3ad70e, "wait_for_completion_timeout" },
	{ 0x84f5e0d0, "pci_enable_device" },
	{ 0x4a453f53, "iowrite32" },
	{ 0x1eaab143, "vCanAddCardChannel" },
	{ 0x7f02188f, "__msecs_to_jiffies" },
	{ 0x22af591a, "pci_iomap" },
	{ 0xa6257a2f, "complete" },
	{ 0xc5b6f236, "queue_work_on" },
	{ 0x30372d96, "queue_release" },
	{ 0x55555880, "queue_reinit" },
	{ 0x608741b5, "__init_swait_queue_head" },
	{ 0x92540fbf, "finish_wait" },
	{ 0xbe8d5277, "dma_unmap_page_attrs" },
	{ 0xdbef4a92, "__pci_register_driver" },
	{ 0x26fdd84e, "dma_sync_single_for_device" },
	{ 0x1229cb50, "vCanInit" },
	{ 0x4896ad3, "pci_request_regions" },
	{ 0x69acdf38, "memcpy" },
	{ 0x37a0cba, "kfree" },
	{ 0x166163ff, "vCanGetCardInfo" },
	{ 0x206ebad6, "queue_irq_lock" },
	{ 0xf72e8c06, "pcpu_hot" },
	{ 0xc3055d20, "usleep_range_state" },
	{ 0x8c26d495, "prepare_to_wait_event" },
	{ 0xe2964344, "__wake_up" },
	{ 0x30d1029a, "set_capability_mask" },
	{ 0x34db050b, "_raw_spin_lock_irqsave" },
	{ 0x4822a91b, "__dynamic_dev_dbg" },
	{ 0xba8fbd64, "_raw_spin_lock" },
	{ 0x9ec8f984, "pci_unregister_driver" },
	{ 0xcbd4898c, "fortify_panic" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x2cc8345c, "dev_driver_string" },
	{ 0xdf2ebb87, "_raw_read_unlock_irqrestore" },
	{ 0x65487097, "__x86_indirect_thunk_rax" },
	{ 0x1dcc18f3, "dma_map_page_attrs" },
	{ 0x6b2dc060, "dump_stack" },
	{ 0x122c3a7e, "_printk" },
	{ 0x8427cc7b, "_raw_spin_lock_irq" },
	{ 0x8ddd8aad, "schedule_timeout" },
	{ 0xa19b956, "__stack_chk_fail" },
	{ 0xec8d96be, "vCanGetCardInfo2" },
	{ 0x803ad55b, "set_capability_ex_value" },
	{ 0xa916b694, "strnlen" },
	{ 0xb1342cdb, "_raw_read_lock_irqsave" },
	{ 0xb5385e3c, "vCanInitData" },
	{ 0x87a21cb3, "__ubsan_handle_out_of_bounds" },
	{ 0x7cd8d75e, "page_offset_base" },
	{ 0x795350a7, "pci_clear_master" },
	{ 0xfe487975, "init_wait_entry" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0x24d273d1, "add_timer" },
	{ 0x235ea4c1, "calculateCRC32" },
	{ 0x69dd3b5b, "crc32_le" },
	{ 0x220f6eb0, "queue_pop" },
	{ 0x4b750f53, "_raw_spin_unlock_irq" },
	{ 0xe6cf5658, "queue_wakeup_on_space" },
	{ 0xb0d3a1c6, "set_capability_ex_mask" },
	{ 0x4a379bbf, "set_capability_value" },
	{ 0x4c9d28b0, "phys_base" },
	{ 0x449ad0a7, "memcmp" },
	{ 0x9ed12e20, "kmalloc_large" },
	{ 0xd35cce70, "_raw_spin_unlock_irqrestore" },
	{ 0x86ffe54a, "pci_iounmap" },
	{ 0xffd473e4, "vCanDispatchEvent" },
	{ 0xeeee73e1, "dma_sync_single_for_cpu" },
	{ 0xfaa20ff6, "queue_front" },
	{ 0xfb578fc5, "memset" },
	{ 0xa5083a26, "pci_set_master" },
	{ 0x25974000, "wait_for_completion" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0x679e43d1, "queue_empty" },
	{ 0xd9a5ea54, "__init_waitqueue_head" },
	{ 0xbfc177bc, "iowrite32_rep" },
	{ 0xafec5d3, "vCanRemoveCardChannel" },
	{ 0xeb078aee, "_raw_write_unlock_irqrestore" },
	{ 0x15ba50a6, "jiffies" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0x97651e6c, "vmemmap_base" },
	{ 0xa648e561, "__ubsan_handle_shift_out_of_bounds" },
	{ 0xc6f46339, "init_timer_key" },
	{ 0xb560f28, "pci_release_regions" },
	{ 0x2cf56265, "__dynamic_pr_debug" },
	{ 0x56470118, "__warn_printk" },
	{ 0x2aca3546, "pci_disable_device" },
	{ 0x1d86c193, "dma_set_mask" },
	{ 0x850e6a88, "kmalloc_trace" },
	{ 0x5021bd81, "_raw_write_lock_irqsave" },
	{ 0x54b1fac6, "__ubsan_handle_load_invalid_value" },
	{ 0xb5b54b34, "_raw_spin_unlock" },
	{ 0x86204941, "vCanCleanup" },
	{ 0xf9a482f9, "msleep" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0xe2c17b5d, "__SCT__might_resched" },
	{ 0xad6d045f, "kmalloc_caches" },
	{ 0x2d3385d3, "system_wq" },
	{ 0x188ea314, "jiffies_to_timespec64" },
	{ 0x453e7dc, "module_layout" },
};

MODULE_INFO(depends, "kvcommon");


MODULE_INFO(srcversion, "0782DF656D85F4254B6FFB0");
