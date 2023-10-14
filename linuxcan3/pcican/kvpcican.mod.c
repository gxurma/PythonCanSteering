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
	{ 0xa78af5f3, "ioread32" },
	{ 0x84f5e0d0, "pci_enable_device" },
	{ 0x4a453f53, "iowrite32" },
	{ 0x1eaab143, "vCanAddCardChannel" },
	{ 0x22af591a, "pci_iomap" },
	{ 0xc5b6f236, "queue_work_on" },
	{ 0x30372d96, "queue_release" },
	{ 0x828398ff, "vCanFlushSendBuffer" },
	{ 0xdbef4a92, "__pci_register_driver" },
	{ 0x1229cb50, "vCanInit" },
	{ 0x4896ad3, "pci_request_regions" },
	{ 0x37a0cba, "kfree" },
	{ 0x166163ff, "vCanGetCardInfo" },
	{ 0xf72e8c06, "pcpu_hot" },
	{ 0xe2964344, "__wake_up" },
	{ 0x34db050b, "_raw_spin_lock_irqsave" },
	{ 0xba8fbd64, "_raw_spin_lock" },
	{ 0x9ec8f984, "pci_unregister_driver" },
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x65487097, "__x86_indirect_thunk_rax" },
	{ 0x122c3a7e, "_printk" },
	{ 0x848d372e, "iowrite8" },
	{ 0xfd06f019, "packed_EAN_to_BCD_with_csum" },
	{ 0x8ddd8aad, "schedule_timeout" },
	{ 0xa19b956, "__stack_chk_fail" },
	{ 0xec8d96be, "vCanGetCardInfo2" },
	{ 0xb5385e3c, "vCanInitData" },
	{ 0x87a21cb3, "__ubsan_handle_out_of_bounds" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0x220f6eb0, "queue_pop" },
	{ 0xe6cf5658, "queue_wakeup_on_space" },
	{ 0x4a379bbf, "set_capability_value" },
	{ 0x9ed12e20, "kmalloc_large" },
	{ 0xd35cce70, "_raw_spin_unlock_irqrestore" },
	{ 0x86ffe54a, "pci_iounmap" },
	{ 0xffd473e4, "vCanDispatchEvent" },
	{ 0xb19b445, "ioread8" },
	{ 0xfaa20ff6, "queue_front" },
	{ 0xfb578fc5, "memset" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0xafec5d3, "vCanRemoveCardChannel" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0x84f435c1, "vCanTime" },
	{ 0xb560f28, "pci_release_regions" },
	{ 0xeae3dfd6, "__const_udelay" },
	{ 0x2aca3546, "pci_disable_device" },
	{ 0x850e6a88, "kmalloc_trace" },
	{ 0xb5b54b34, "_raw_spin_unlock" },
	{ 0x86204941, "vCanCleanup" },
	{ 0xeb233a45, "__kmalloc" },
	{ 0xad6d045f, "kmalloc_caches" },
	{ 0x2d3385d3, "system_wq" },
	{ 0x453e7dc, "module_layout" },
};

MODULE_INFO(depends, "kvcommon");


MODULE_INFO(srcversion, "C4B01DAE9FCB05D1E82B66B");
