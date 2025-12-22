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
	{ 0xc45d298e, "is_vmalloc_addr" },
	{ 0x7e2232fb, "ioread32" },
	{ 0x57860fb4, "wait_for_completion_timeout" },
	{ 0xef95a802, "pci_enable_device" },
	{ 0xfad8f384, "iowrite32" },
	{ 0x59b87546, "vCanAddCardChannel" },
	{ 0xd710adbf, "__kmalloc_noprof" },
	{ 0x954b0cc3, "pci_iomap" },
	{ 0x2b936485, "pci_alloc_irq_vectors" },
	{ 0x65026e43, "complete" },
	{ 0x49733ad6, "queue_work_on" },
	{ 0x39b5bb15, "queue_release" },
	{ 0x39b5bb15, "queue_reinit" },
	{ 0x60c9c0b3, "__init_swait_queue_head" },
	{ 0x1a88dcc7, "dma_unmap_page_attrs" },
	{ 0x04cf7d01, "__pci_register_driver" },
	{ 0x645c8a85, "vCanInit" },
	{ 0xbd06710b, "pci_request_regions" },
	{ 0xa53f4e29, "memcpy" },
	{ 0xcb8b6ec6, "kfree" },
	{ 0x48feac32, "vCanGetCardInfo" },
	{ 0x39b5bb15, "queue_irq_lock" },
	{ 0x0feb1e94, "usleep_range_state" },
	{ 0x16ab4215, "__wake_up" },
	{ 0xe5305ebf, "pci_irq_vector" },
	{ 0xba8e1447, "set_capability_mask" },
	{ 0xe1e1f979, "_raw_spin_lock_irqsave" },
	{ 0xde338d9a, "_raw_spin_lock" },
	{ 0xc720a5c5, "pci_unregister_driver" },
	{ 0xd272d446, "__fentry__" },
	{ 0x2c226513, "dev_driver_string" },
	{ 0xc7ca1fbd, "_raw_read_unlock_irqrestore" },
	{ 0x5a844b26, "__x86_indirect_thunk_rax" },
	{ 0xcef648d8, "dma_map_page_attrs" },
	{ 0xd272d446, "dump_stack" },
	{ 0xe8213e80, "_printk" },
	{ 0xde338d9a, "_raw_spin_lock_irq" },
	{ 0x6ac784f4, "schedule_timeout" },
	{ 0xd272d446, "__stack_chk_fail" },
	{ 0x7870c5f2, "vCanGetCardInfo2" },
	{ 0xcfc54b4a, "set_capability_ex_value" },
	{ 0xd710adbf, "__kmalloc_large_noprof" },
	{ 0x9479a1e8, "strnlen" },
	{ 0x4d40f3a6, "const_pcpu_hot" },
	{ 0x78bbf245, "_raw_read_lock_irqsave" },
	{ 0xd9d667bd, "vCanInitData" },
	{ 0x90a48d82, "__ubsan_handle_out_of_bounds" },
	{ 0xbd03ed67, "page_offset_base" },
	{ 0x33ba6a25, "pci_clear_master" },
	{ 0x80a5e1e0, "__dma_sync_single_for_cpu" },
	{ 0x9126ce86, "request_threaded_irq" },
	{ 0xa470b7e2, "add_timer" },
	{ 0x7a3ad30b, "calculateCRC32" },
	{ 0xbd03ed67, "random_kmalloc_seed" },
	{ 0x39b5bb15, "queue_pop" },
	{ 0xde338d9a, "_raw_spin_unlock_irq" },
	{ 0x39b5bb15, "queue_wakeup_on_space" },
	{ 0xcfc54b4a, "set_capability_ex_mask" },
	{ 0xba8e1447, "set_capability_value" },
	{ 0xbd03ed67, "phys_base" },
	{ 0x402db74e, "memcmp" },
	{ 0xe54e0a6b, "__fortify_panic" },
	{ 0x81a1a811, "_raw_spin_unlock_irqrestore" },
	{ 0x022d2c4d, "pci_iounmap" },
	{ 0x689ff9d2, "vCanDispatchEvent" },
	{ 0xe7db7ec6, "queue_front" },
	{ 0x27683a56, "memset" },
	{ 0x33ba6a25, "pci_set_master" },
	{ 0x65026e43, "wait_for_completion" },
	{ 0xd272d446, "__x86_return_thunk" },
	{ 0xe7db7ec6, "queue_empty" },
	{ 0x6c46e0fe, "iowrite32_rep" },
	{ 0x34e23247, "vCanRemoveCardChannel" },
	{ 0xc7ca1fbd, "_raw_write_unlock_irqrestore" },
	{ 0x058c185a, "jiffies" },
	{ 0xdd6830c7, "sprintf" },
	{ 0xbd03ed67, "vmemmap_base" },
	{ 0x82fd7238, "__ubsan_handle_shift_out_of_bounds" },
	{ 0xb35a00ee, "crc32_le_arch" },
	{ 0x02f9bbf0, "init_timer_key" },
	{ 0x2b718ccd, "pci_release_regions" },
	{ 0x80a5e1e0, "__dma_sync_single_for_device" },
	{ 0x23f25c0a, "__dynamic_pr_debug" },
	{ 0x70db3fe4, "__kmalloc_cache_noprof" },
	{ 0x75738bed, "__warn_printk" },
	{ 0x33ba6a25, "pci_disable_device" },
	{ 0x64198441, "dma_set_mask" },
	{ 0x78bbf245, "_raw_write_lock_irqsave" },
	{ 0xe4de56b4, "__ubsan_handle_load_invalid_value" },
	{ 0xde338d9a, "_raw_spin_unlock" },
	{ 0x8a64c8b7, "pci_free_irq_vectors" },
	{ 0x34583558, "vCanCleanup" },
	{ 0x67628f51, "msleep" },
	{ 0xfed1e3bc, "kmalloc_caches" },
	{ 0xaef1f20d, "system_wq" },
	{ 0x74b331ef, "jiffies_to_timespec64" },
	{ 0xba157484, "module_layout" },
};

static const u32 ____version_ext_crcs[]
__used __section("__version_ext_crcs") = {
	0x9dd4105e,
	0xc45d298e,
	0x7e2232fb,
	0x57860fb4,
	0xef95a802,
	0xfad8f384,
	0x59b87546,
	0xd710adbf,
	0x954b0cc3,
	0x2b936485,
	0x65026e43,
	0x49733ad6,
	0x39b5bb15,
	0x39b5bb15,
	0x60c9c0b3,
	0x1a88dcc7,
	0x04cf7d01,
	0x645c8a85,
	0xbd06710b,
	0xa53f4e29,
	0xcb8b6ec6,
	0x48feac32,
	0x39b5bb15,
	0x0feb1e94,
	0x16ab4215,
	0xe5305ebf,
	0xba8e1447,
	0xe1e1f979,
	0xde338d9a,
	0xc720a5c5,
	0xd272d446,
	0x2c226513,
	0xc7ca1fbd,
	0x5a844b26,
	0xcef648d8,
	0xd272d446,
	0xe8213e80,
	0xde338d9a,
	0x6ac784f4,
	0xd272d446,
	0x7870c5f2,
	0xcfc54b4a,
	0xd710adbf,
	0x9479a1e8,
	0x4d40f3a6,
	0x78bbf245,
	0xd9d667bd,
	0x90a48d82,
	0xbd03ed67,
	0x33ba6a25,
	0x80a5e1e0,
	0x9126ce86,
	0xa470b7e2,
	0x7a3ad30b,
	0xbd03ed67,
	0x39b5bb15,
	0xde338d9a,
	0x39b5bb15,
	0xcfc54b4a,
	0xba8e1447,
	0xbd03ed67,
	0x402db74e,
	0xe54e0a6b,
	0x81a1a811,
	0x022d2c4d,
	0x689ff9d2,
	0xe7db7ec6,
	0x27683a56,
	0x33ba6a25,
	0x65026e43,
	0xd272d446,
	0xe7db7ec6,
	0x6c46e0fe,
	0x34e23247,
	0xc7ca1fbd,
	0x058c185a,
	0xdd6830c7,
	0xbd03ed67,
	0x82fd7238,
	0xb35a00ee,
	0x02f9bbf0,
	0x2b718ccd,
	0x80a5e1e0,
	0x23f25c0a,
	0x70db3fe4,
	0x75738bed,
	0x33ba6a25,
	0x64198441,
	0x78bbf245,
	0xe4de56b4,
	0xde338d9a,
	0x8a64c8b7,
	0x34583558,
	0x67628f51,
	0xfed1e3bc,
	0xaef1f20d,
	0x74b331ef,
	0xba157484,
};
static const char ____version_ext_names[]
__used __section("__version_ext_names") =
	"free_irq\0"
	"is_vmalloc_addr\0"
	"ioread32\0"
	"wait_for_completion_timeout\0"
	"pci_enable_device\0"
	"iowrite32\0"
	"vCanAddCardChannel\0"
	"__kmalloc_noprof\0"
	"pci_iomap\0"
	"pci_alloc_irq_vectors\0"
	"complete\0"
	"queue_work_on\0"
	"queue_release\0"
	"queue_reinit\0"
	"__init_swait_queue_head\0"
	"dma_unmap_page_attrs\0"
	"__pci_register_driver\0"
	"vCanInit\0"
	"pci_request_regions\0"
	"memcpy\0"
	"kfree\0"
	"vCanGetCardInfo\0"
	"queue_irq_lock\0"
	"usleep_range_state\0"
	"__wake_up\0"
	"pci_irq_vector\0"
	"set_capability_mask\0"
	"_raw_spin_lock_irqsave\0"
	"_raw_spin_lock\0"
	"pci_unregister_driver\0"
	"__fentry__\0"
	"dev_driver_string\0"
	"_raw_read_unlock_irqrestore\0"
	"__x86_indirect_thunk_rax\0"
	"dma_map_page_attrs\0"
	"dump_stack\0"
	"_printk\0"
	"_raw_spin_lock_irq\0"
	"schedule_timeout\0"
	"__stack_chk_fail\0"
	"vCanGetCardInfo2\0"
	"set_capability_ex_value\0"
	"__kmalloc_large_noprof\0"
	"strnlen\0"
	"const_pcpu_hot\0"
	"_raw_read_lock_irqsave\0"
	"vCanInitData\0"
	"__ubsan_handle_out_of_bounds\0"
	"page_offset_base\0"
	"pci_clear_master\0"
	"__dma_sync_single_for_cpu\0"
	"request_threaded_irq\0"
	"add_timer\0"
	"calculateCRC32\0"
	"random_kmalloc_seed\0"
	"queue_pop\0"
	"_raw_spin_unlock_irq\0"
	"queue_wakeup_on_space\0"
	"set_capability_ex_mask\0"
	"set_capability_value\0"
	"phys_base\0"
	"memcmp\0"
	"__fortify_panic\0"
	"_raw_spin_unlock_irqrestore\0"
	"pci_iounmap\0"
	"vCanDispatchEvent\0"
	"queue_front\0"
	"memset\0"
	"pci_set_master\0"
	"wait_for_completion\0"
	"__x86_return_thunk\0"
	"queue_empty\0"
	"iowrite32_rep\0"
	"vCanRemoveCardChannel\0"
	"_raw_write_unlock_irqrestore\0"
	"jiffies\0"
	"sprintf\0"
	"vmemmap_base\0"
	"__ubsan_handle_shift_out_of_bounds\0"
	"crc32_le_arch\0"
	"init_timer_key\0"
	"pci_release_regions\0"
	"__dma_sync_single_for_device\0"
	"__dynamic_pr_debug\0"
	"__kmalloc_cache_noprof\0"
	"__warn_printk\0"
	"pci_disable_device\0"
	"dma_set_mask\0"
	"_raw_write_lock_irqsave\0"
	"__ubsan_handle_load_invalid_value\0"
	"_raw_spin_unlock\0"
	"pci_free_irq_vectors\0"
	"vCanCleanup\0"
	"msleep\0"
	"kmalloc_caches\0"
	"system_wq\0"
	"jiffies_to_timespec64\0"
	"module_layout\0"
;

MODULE_INFO(depends, "kvcommon");

MODULE_ALIAS("pci:v00001A07d0000000Dsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d0000000Esv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d0000000Fsv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000010sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000011sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000012sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000013sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000014sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000015sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000016sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000017sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000018sv*sd*bc*sc*i*");
MODULE_ALIAS("pci:v00001A07d00000019sv*sd*bc*sc*i*");

MODULE_INFO(srcversion, "22D0A0E814C1CF607EFD868");
