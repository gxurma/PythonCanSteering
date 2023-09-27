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
	{ 0x2d3385d3, __VMLINUX_SYMBOL_STR(system_wq) },
	{ 0x5773238, __VMLINUX_SYMBOL_STR(kmalloc_caches) },
	{ 0x946d4a0c, __VMLINUX_SYMBOL_STR(vCanCleanup) },
	{ 0x672edad8, __VMLINUX_SYMBOL_STR(pv_lock_ops) },
	{ 0x63e983d0, __VMLINUX_SYMBOL_STR(_raw_write_lock_irqsave) },
	{ 0x28572964, __VMLINUX_SYMBOL_STR(vCanCardRemoved) },
	{ 0x7ae5ad74, __VMLINUX_SYMBOL_STR(sme_active) },
	{ 0x5f1af6a3, __VMLINUX_SYMBOL_STR(pci_disable_device) },
	{ 0xcdbfc112, __VMLINUX_SYMBOL_STR(seq_printf) },
	{ 0xa6f73c6f, __VMLINUX_SYMBOL_STR(pci_release_regions) },
	{ 0xe4f742fb, __VMLINUX_SYMBOL_STR(init_timer_key) },
	{ 0x97651e6c, __VMLINUX_SYMBOL_STR(vmemmap_base) },
	{ 0x91715312, __VMLINUX_SYMBOL_STR(sprintf) },
	{ 0x15ba50a6, __VMLINUX_SYMBOL_STR(jiffies) },
	{ 0x88c61c, __VMLINUX_SYMBOL_STR(_raw_write_unlock_irqrestore) },
	{ 0xbfc177bc, __VMLINUX_SYMBOL_STR(iowrite32_rep) },
	{ 0xa6682fdd, __VMLINUX_SYMBOL_STR(__init_waitqueue_head) },
	{ 0xa034bb5c, __VMLINUX_SYMBOL_STR(queue_empty) },
	{ 0xb1904934, __VMLINUX_SYMBOL_STR(wait_for_completion) },
	{ 0x4bbc293, __VMLINUX_SYMBOL_STR(pci_set_master) },
	{ 0x7e526bfa, __VMLINUX_SYMBOL_STR(__x86_indirect_thunk_r10) },
	{ 0xfb578fc5, __VMLINUX_SYMBOL_STR(memset) },
	{ 0x50614cee, __VMLINUX_SYMBOL_STR(queue_front) },
	{ 0x53ceed87, __VMLINUX_SYMBOL_STR(vCanDispatchEvent) },
	{ 0xc20826cc, __VMLINUX_SYMBOL_STR(pci_iounmap) },
	{ 0xe966901, __VMLINUX_SYMBOL_STR(_raw_spin_unlock_irqrestore) },
	{ 0x9b65a65f, __VMLINUX_SYMBOL_STR(current_task) },
	{ 0x27e1a049, __VMLINUX_SYMBOL_STR(printk) },
	{ 0x449ad0a7, __VMLINUX_SYMBOL_STR(memcmp) },
	{ 0x4c9d28b0, __VMLINUX_SYMBOL_STR(phys_base) },
	{ 0x32e94b6b, __VMLINUX_SYMBOL_STR(set_capability_value) },
	{ 0x8c8822a4, __VMLINUX_SYMBOL_STR(queue_wakeup_on_space) },
	{ 0x256a9c87, __VMLINUX_SYMBOL_STR(queue_pop) },
	{ 0x235ea4c1, __VMLINUX_SYMBOL_STR(calculateCRC32) },
	{ 0xd44e7d7d, __VMLINUX_SYMBOL_STR(add_timer) },
	{ 0x2072ee9b, __VMLINUX_SYMBOL_STR(request_threaded_irq) },
	{ 0x6f355cf1, __VMLINUX_SYMBOL_STR(pci_clear_master) },
	{ 0x7cd8d75e, __VMLINUX_SYMBOL_STR(page_offset_base) },
	{ 0x9ea2120b, __VMLINUX_SYMBOL_STR(vCanInitData) },
	{ 0x40414632, __VMLINUX_SYMBOL_STR(_raw_read_lock_irqsave) },
	{ 0x8ff4079b, __VMLINUX_SYMBOL_STR(pv_irq_ops) },
	{ 0x6ca88ed, __VMLINUX_SYMBOL_STR(vCanGetCardInfo2) },
	{ 0xdb7305a1, __VMLINUX_SYMBOL_STR(__stack_chk_fail) },
	{ 0x8ddd8aad, __VMLINUX_SYMBOL_STR(schedule_timeout) },
	{ 0xa202a8e5, __VMLINUX_SYMBOL_STR(kmalloc_order_trace) },
	{ 0x6a964a2, __VMLINUX_SYMBOL_STR(_raw_spin_lock_irq) },
	{ 0x2ea2c95c, __VMLINUX_SYMBOL_STR(__x86_indirect_thunk_rax) },
	{ 0x37624d0a, __VMLINUX_SYMBOL_STR(_raw_read_unlock_irqrestore) },
	{ 0xbdfb6dbb, __VMLINUX_SYMBOL_STR(__fentry__) },
	{ 0xcbd4898c, __VMLINUX_SYMBOL_STR(fortify_panic) },
	{ 0x124688d8, __VMLINUX_SYMBOL_STR(pci_unregister_driver) },
	{ 0xbeee391, __VMLINUX_SYMBOL_STR(kmem_cache_alloc_trace) },
	{ 0x56321ae2, __VMLINUX_SYMBOL_STR(_raw_spin_lock) },
	{ 0x7e8d43c6, __VMLINUX_SYMBOL_STR(_raw_spin_lock_irqsave) },
	{ 0x489197a6, __VMLINUX_SYMBOL_STR(set_capability_mask) },
	{ 0xfe768495, __VMLINUX_SYMBOL_STR(__wake_up) },
	{ 0xbe17bbe0, __VMLINUX_SYMBOL_STR(queue_irq_lock) },
	{ 0x24d5c1b2, __VMLINUX_SYMBOL_STR(vCanGetCardInfo) },
	{ 0x37a0cba, __VMLINUX_SYMBOL_STR(kfree) },
	{ 0x69acdf38, __VMLINUX_SYMBOL_STR(memcpy) },
	{ 0xa04d1f57, __VMLINUX_SYMBOL_STR(pci_request_regions) },
	{ 0xf41ea9f4, __VMLINUX_SYMBOL_STR(vCanInit) },
	{ 0xfcc70556, __VMLINUX_SYMBOL_STR(__pci_register_driver) },
	{ 0x99272b9f, __VMLINUX_SYMBOL_STR(dev_warn) },
	{ 0xa8177b09, __VMLINUX_SYMBOL_STR(queue_reinit) },
	{ 0x7794a5a7, __VMLINUX_SYMBOL_STR(queue_release) },
	{ 0x2e0d2f7f, __VMLINUX_SYMBOL_STR(queue_work_on) },
	{ 0x19cf472b, __VMLINUX_SYMBOL_STR(complete) },
	{ 0xe3a7ae0a, __VMLINUX_SYMBOL_STR(pci_iomap) },
	{ 0x436c2179, __VMLINUX_SYMBOL_STR(iowrite32) },
	{ 0xf19e6ee3, __VMLINUX_SYMBOL_STR(pci_enable_device) },
	{ 0xccb6663c, __VMLINUX_SYMBOL_STR(wait_for_completion_timeout) },
	{ 0xcbac4b66, __VMLINUX_SYMBOL_STR(dma_ops) },
	{ 0xe484e35f, __VMLINUX_SYMBOL_STR(ioread32) },
	{ 0xc1514a3b, __VMLINUX_SYMBOL_STR(free_irq) },
	{ 0x17fbce60, __VMLINUX_SYMBOL_STR(sme_me_mask) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=kvcommon";


MODULE_INFO(srcversion, "C2EBCBD3E027895EFC6D10C");
