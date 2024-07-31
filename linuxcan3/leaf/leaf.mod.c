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
	{ 0xe8e7edd2, __VMLINUX_SYMBOL_STR(queue_init) },
	{ 0xd2b09ce5, __VMLINUX_SYMBOL_STR(__kmalloc) },
	{ 0x5c5b963, __VMLINUX_SYMBOL_STR(vCanCleanup) },
	{ 0x672edad8, __VMLINUX_SYMBOL_STR(pv_lock_ops) },
	{ 0x43a53735, __VMLINUX_SYMBOL_STR(__alloc_workqueue_key) },
	{ 0x895680cf, __VMLINUX_SYMBOL_STR(queue_length) },
	{ 0xddeb9ae8, __VMLINUX_SYMBOL_STR(usb_kill_urb) },
	{ 0x4add9142, __VMLINUX_SYMBOL_STR(convert_vcan_to_hydra_cmd) },
	{ 0x132a679, __VMLINUX_SYMBOL_STR(softSyncLoc2Glob) },
	{ 0xe028aca1, __VMLINUX_SYMBOL_STR(softSyncAddMember) },
	{ 0x73e8f1a8, __VMLINUX_SYMBOL_STR(kthread_create_on_node) },
	{ 0xa306008f, __VMLINUX_SYMBOL_STR(vCanRemoveCardChannel) },
	{ 0xa6682fdd, __VMLINUX_SYMBOL_STR(__init_waitqueue_head) },
	{ 0xaad8c7d6, __VMLINUX_SYMBOL_STR(default_wake_function) },
	{ 0xa034bb5c, __VMLINUX_SYMBOL_STR(queue_empty) },
	{ 0xdc45991b, __VMLINUX_SYMBOL_STR(queue_push) },
	{ 0xb1904934, __VMLINUX_SYMBOL_STR(wait_for_completion) },
	{ 0xc2bf1f9f, __VMLINUX_SYMBOL_STR(ticks_init) },
	{ 0xfb578fc5, __VMLINUX_SYMBOL_STR(memset) },
	{ 0x50614cee, __VMLINUX_SYMBOL_STR(queue_front) },
	{ 0xd0bbfdfa, __VMLINUX_SYMBOL_STR(queue_add_wait_for_space) },
	{ 0x26928130, __VMLINUX_SYMBOL_STR(vCanDispatchEvent) },
	{ 0xe966901, __VMLINUX_SYMBOL_STR(_raw_spin_unlock_irqrestore) },
	{ 0x9b65a65f, __VMLINUX_SYMBOL_STR(current_task) },
	{ 0xbe9c7e41, __VMLINUX_SYMBOL_STR(usb_deregister) },
	{ 0x27e1a049, __VMLINUX_SYMBOL_STR(printk) },
	{ 0x7eebc343, __VMLINUX_SYMBOL_STR(ticks_to_64bit_ns) },
	{ 0x21b32ce, __VMLINUX_SYMBOL_STR(set_capability_value) },
	{ 0x9166fada, __VMLINUX_SYMBOL_STR(strncpy) },
	{ 0x8c8822a4, __VMLINUX_SYMBOL_STR(queue_wakeup_on_space) },
	{ 0x256a9c87, __VMLINUX_SYMBOL_STR(queue_pop) },
	{ 0x8c03d20c, __VMLINUX_SYMBOL_STR(destroy_workqueue) },
	{ 0xb13294d9, __VMLINUX_SYMBOL_STR(usb_free_coherent) },
	{ 0x952664c5, __VMLINUX_SYMBOL_STR(do_exit) },
	{ 0x42160169, __VMLINUX_SYMBOL_STR(flush_workqueue) },
	{ 0xd80a7183, __VMLINUX_SYMBOL_STR(softSyncHandleTRef) },
	{ 0x3aded471, __VMLINUX_SYMBOL_STR(module_put) },
	{ 0xf6671a94, __VMLINUX_SYMBOL_STR(vCanInitData) },
	{ 0x47a74c59, __VMLINUX_SYMBOL_STR(usb_submit_urb) },
	{ 0xdb7305a1, __VMLINUX_SYMBOL_STR(__stack_chk_fail) },
	{ 0x60232e27, __VMLINUX_SYMBOL_STR(usb_bulk_msg) },
	{ 0x8ddd8aad, __VMLINUX_SYMBOL_STR(schedule_timeout) },
	{ 0xa202a8e5, __VMLINUX_SYMBOL_STR(kmalloc_order_trace) },
	{ 0x803c773f, __VMLINUX_SYMBOL_STR(wake_up_process) },
	{ 0xbdfb6dbb, __VMLINUX_SYMBOL_STR(__fentry__) },
	{ 0xbeee391, __VMLINUX_SYMBOL_STR(kmem_cache_alloc_trace) },
	{ 0x56321ae2, __VMLINUX_SYMBOL_STR(_raw_spin_lock) },
	{ 0x7e8d43c6, __VMLINUX_SYMBOL_STR(_raw_spin_lock_irqsave) },
	{ 0x101634e1, __VMLINUX_SYMBOL_STR(set_capability_mask) },
	{ 0xfe768495, __VMLINUX_SYMBOL_STR(__wake_up) },
	{ 0x4106551e, __VMLINUX_SYMBOL_STR(softSyncRemoveMember) },
	{ 0x37a0cba, __VMLINUX_SYMBOL_STR(kfree) },
	{ 0xd523a284, __VMLINUX_SYMBOL_STR(vCanInit) },
	{ 0x26ea0946, __VMLINUX_SYMBOL_STR(vCanFlushSendBuffer) },
	{ 0xe88f698b, __VMLINUX_SYMBOL_STR(usb_register_driver) },
	{ 0xf3ad4fb2, __VMLINUX_SYMBOL_STR(queue_remove_wait_for_space) },
	{ 0x6d8c3aa3, __VMLINUX_SYMBOL_STR(queue_back) },
	{ 0xa8177b09, __VMLINUX_SYMBOL_STR(queue_reinit) },
	{ 0x7794a5a7, __VMLINUX_SYMBOL_STR(queue_release) },
	{ 0x2e0d2f7f, __VMLINUX_SYMBOL_STR(queue_work_on) },
	{ 0x19cf472b, __VMLINUX_SYMBOL_STR(complete) },
	{ 0x47f6aeec, __VMLINUX_SYMBOL_STR(usb_alloc_coherent) },
	{ 0x7f02188f, __VMLINUX_SYMBOL_STR(__msecs_to_jiffies) },
	{ 0xd8d6a34c, __VMLINUX_SYMBOL_STR(vCanAddCardChannel) },
	{ 0xccb6663c, __VMLINUX_SYMBOL_STR(wait_for_completion_timeout) },
	{ 0x925ad1ee, __VMLINUX_SYMBOL_STR(get_usb_root_hub_id) },
	{ 0xf81758cb, __VMLINUX_SYMBOL_STR(usb_free_urb) },
	{ 0x6d584285, __VMLINUX_SYMBOL_STR(try_module_get) },
	{ 0xd3941341, __VMLINUX_SYMBOL_STR(usb_alloc_urb) },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=kvcommon";

MODULE_ALIAS("usb:v0BFDp000Ad*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp000Bd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp000Cd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp000Ed*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp000Fd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0010d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0011d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0012d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0013d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0016d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0017d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0018d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0019d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp001Ad*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp001Bd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp001Cd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp001Dd*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0020d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0022d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0023d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0027d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0026d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0120d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0121d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0122d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0123d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0124d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0126d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0127d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v0BFDp0128d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "C9DDA238075EB40555EED6C");
