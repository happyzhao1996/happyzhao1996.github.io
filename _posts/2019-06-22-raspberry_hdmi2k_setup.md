---
layout: post
title: "树莓派3B+实现HDMI 2k分辨率输出"
date: 2019-06-22 23:48:22 +0800
tags: [Raspberry Pi]
categories: [Raspberry Pi]
description: 树莓派3B+实现HDMI的2k分辨率60Hz输出所需要的一些设置
---

首先使用nano或者vi（管理员权限）打开文件/boot/config.txt

	sudo vi /boot/config/txt

<center>or</center>

	sudo nano /boot/config.txt

假设树莓派当前已经可以实现HDMI输出，为了实现2560x1440分辨率的60Hz输出，我们只需要添加如下一些代码在文件末尾：

	hdmi_group = 2	
	hdmi_mode = 82                    #这两步是为了启用自定义参数输出
	hdmi_cvt = 2560 1440 60 3 0 0 0 1 #设置输出的分辨率、帧率等参数
	max_framebuffer_width = 2560
	max_framebuffer_height = 1440
	hdmi_pixel_freq_limit = 400000000

然后保存并重启。这时树莓派应该就可以实现2560x1440分辨率的60Hz输出了。

如果出现屏幕时亮时灭的情况，可能是因为HDMI输出信号强度不够或者是HDMI连接线损耗较大，这时可以在刚刚的文件最后加上这个命令：

	config_hdmi_boost = 11	#(数字表示信号强度相对值，为1~11)
	
然后保存并重启，应该就不会再有什么问题了。