# Steps to reproduce the problem

1. Build the dockertest snap with snapcraft (On development machine Ubuntu 16.04 LTS)

2. Test steps (On the development machine)
```
#install docker snap
sudo snap install docker --devmode

# Launch a container
docker run -it --name docker-test ubuntu bash

#install the test snap
sudo snap install docker-kernel-panic-test_0.0.1_amd64.snap --devmode

#Run the test snap
docker-kernel-panic-test.dockertest
```

#################################
```
Kernel panic

[ 8109.535303] BUG: unable to handle kernel paging request at fffffffffffffff3
[ 8109.535310] IP: [<ffffffff813ffce0>] strlen+0x0/0x20
[ 8109.535320] PGD 1e0d067 PUD 1e0f067 PMD 0
[ 8109.535326] Oops: 0000 [#2] SMP
[ 8109.535330] Modules linked in: overlay ip6table_filter ip6_tables veth snd_seq_dummy xt_comment rfcomm ipt_MASQUERADE nf_nat_masquerade_ipv4 xfrm_user xfrm_algo iptable_nat nf_conntrack_ipv4 nf_defrag_ipv4 nf_nat_ipv4 xt_addrtype iptable_filter ip_tables xt_conntrack x_tables nf_nat nf_conntrack br_netfilter bridge stp llc aufs bnep binfmt_misc nls_iso8859_1 pl2303 usbserial dcdbas dell_wmi sparse_keymap snd_hda_codec_realtek snd_hda_codec_generic i915_bpo intel_ips snd_hda_codec_hdmi drm_kms_helper i2c_algo_bit fb_sys_fops syscopyarea sysfillrect sysimgblt input_leds snd_hda_intel snd_hda_codec snd_hda_core arc4 snd_hwdep rtl8723be btcoexist snd_pcm rtl8723_common snd_seq_midi snd_seq_midi_event rtl_pci snd_rawmidi rtlwifi mac80211 snd_seq btusb hci_uart intel_rapl snd_seq_device x86_pkg_temp_thermal
[ 8109.535392]  intel_powerclamp coretemp btrtl btqca btbcm btintel cfg80211 bluetooth kvm_intel kvm snd_timer snd irqbypass soundcore acpi_als crct10dif_pclmul crc32_pclmul mei_me kfifo_buf ghash_clmulni_intel drm aesni_intel mei industrialio shpchp serio_raw aes_x86_64 intel_lpss_acpi intel_lpss lrw gf128mul glue_helper ablk_helper cryptd acpi_pad tpm_crb mac_hid wmi parport_pc ppdev lp parport autofs4 uas usb_storage hid_generic usbhid e1000e psmouse ptp pps_core ahci libahci video pinctrl_sunrisepoint i2c_hid pinctrl_intel hid fjes
[ 8109.535446] CPU: 3 PID: 23793 Comm: snap-confine Tainted: G      D         4.4.0-59-generic #80-Ubuntu
[ 8109.535449] Hardware name: Dell Inc. XPS 8900/0XJ8C4, BIOS 2.0.3 09/18/2015
[ 8109.535453] task: ffff880013ca0f00 ti: ffff8801b4e08000 task.ti: ffff8801b4e08000
[ 8109.535455] RIP: 0010:[<ffffffff813ffce0>]  [<ffffffff813ffce0>] strlen+0x0/0x20
[ 8109.535462] RSP: 0018:ffff8801b4e0ba20  EFLAGS: 00010246
[ 8109.535464] RAX: ffff8801b4e0bb20 RBX: fffffffffffffff3 RCX: 0000000000000000
[ 8109.535467] RDX: 000000000000015c RSI: fffffffffffffff3 RDI: fffffffffffffff3
[ 8109.535469] RBP: ffff8801b4e0ba38 R08: ffff88003409a146 R09: ffff8801b4e0ba94
[ 8109.535472] R10: 000000000000000e R11: ffff88003409a13f R12: ffff880108f97e00
[ 8109.535474] R13: ffff880013ca0f00 R14: ffffffff8139b3d0 R15: 00000000fffffff3
[ 8109.535477] FS:  00007f7360401740(0000) GS:ffff8802654c0000(0000) knlGS:0000000000000000
[ 8109.535480] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
[ 8109.535482] CR2: fffffffffffffff3 CR3: 0000000176039000 CR4: 00000000003406e0
[ 8109.535485] DR0: 0000000000000000 DR1: 0000000000000000 DR2: 0000000000000000
[ 8109.535487] DR3: 0000000000000000 DR6: 00000000fffe0ff0 DR7: 0000000000000400
[ 8109.535489] Stack:
[ 8109.535491]  ffffffff8112333a ffff880108f97e00 ffff8801b4e0bb00 ffff8801b4e0ba60
[ 8109.535496]  ffffffff8139b438 ffff880108f97e00 ffff8801b4e0bb00 ffff880013ca0f00
[ 8109.535500]  ffff8801b4e0bad8 ffffffff81370498 0000000000000000 ffff8801b4e0baf0
[ 8109.535505] Call Trace:
[ 8109.535512]  [<ffffffff8112333a>] ? audit_log_untrustedstring+0x1a/0x30
[ 8109.535519]  [<ffffffff8139b438>] audit_cb+0x68/0x3f0
[ 8109.535525]  [<ffffffff81370498>] common_lsm_audit+0x1b8/0x740
[ 8109.535530]  [<ffffffff81227676>] ? prepend_path+0xc6/0x2a0
[ 8109.535536]  [<ffffffff81382a2f>] aa_audit+0x5f/0x170
[ 8109.535541]  [<ffffffff8139b3c2>] audit_mount+0x152/0x160
[ 8109.535546]  [<ffffffff8139ba8d>] match_mnt_path_str+0x1dd/0x490
[ 8109.535552]  [<ffffffff81228978>] ? dentry_path+0x18/0x70
[ 8109.535557]  [<ffffffff8139be1a>] match_mnt+0xda/0x150
[ 8109.535562]  [<ffffffff8139c690>] aa_bind_mount+0x100/0x180
[ 8109.535566]  [<ffffffff813917f0>] wrap_apparmor_sb_mount+0x1c0/0x270
[ 8109.535571]  [<ffffffff813471c7>] security_sb_mount+0x57/0x80
[ 8109.535576]  [<ffffffff8123148b>] do_mount+0xab/0xda0
[ 8109.535582]  [<ffffffff811f0af4>] ? __kmalloc_track_caller+0x1b4/0x250
[ 8109.535587]  [<ffffffff810efa71>] ? hrtimer_try_to_cancel+0xd1/0x130
[ 8109.535593]  [<ffffffff811ad9d2>] ? memdup_user+0x42/0x70
[ 8109.535597]  [<ffffffff812324bf>] SyS_mount+0x9f/0x100
[ 8109.535604]  [<ffffffff818384f2>] entry_SYSCALL_64_fastpath+0x16/0x71
[ 8109.535606] Code: 89 f8 48 89 e5 f6 82 e0 0d a5 81 20 74 10 48 83 c0 01 0f b6 10 f6 82 e0 0d a5 81 20 75 f0 5d c3 90 66 2e 0f 1f 84 00 00 00 00 00 <80> 3f 00 55 48 89 e5 74 11 48 89 f8 48 83 c0 01 80 38 00 75 f7
[ 8109.535657] RIP  [<ffffffff813ffce0>] strlen+0x0/0x20
[ 8109.535663]  RSP <ffff8801b4e0ba20>
[ 8109.535665] CR2: fffffffffffffff3
[ 8109.535669] ---[ end trace 9d706f4ba3fad49d ]---
```
