#!/usr/bin/env python3

##此脚本的作用是找出指定目录下所有包含指定关键字的文件

import os
import re

def find_str(target_file, target_word):
	if ".DS_Store" in target_file:
		return
	with open(target_file, "r", encoding="utf-8") as t_file:
		line_num = 0
		try:
			for line in t_file.readlines():
				line_num += 1
				if re.search(target_word, line) is not None:
					print("Find match in %a at line %d;"%(target_file, line_num))
		except UnicodeDecodeError:
			print("Unicode decode error while readlines in file %s"%target_file)

def get_file_list(target_dir):
	
	o_list = os.listdir(target_dir)
	for item in o_list:
		item = os.path.join(target_dir, item)
		if os.path.isdir(item):
			get_file_list(item)
		else:
			file_list.append(item)
	return file_list


file_list = []
search_dir = "/Users/sss/Downloads/RTL8821CU_WiFi_linux_v5.2.15.1_27326_COEX20171114-2525.20180403/driver/rtl8821CU_WiFi_linux4.14.16_v5.2.15.1_27326.20180403_COEX20171114-2525"
search_str_1 = "continual_io_error"
search_str_2 = "vendorreq_times"
search_str_3 = "MAX_USBCTRL_VENDORREQ_TIMES"
search_str_4 = "MAX_CONTINUAL_IO_ERR"
search_str_5 = "RTW_USB_CONTROL_MSG_TIMEOUT"
search_str_6 = ""
search_str_7 = ""
search_str_8 = ""
search_str_9 = ""
#print(get_file_list(search_dir))

for item in get_file_list(search_dir):
	find_str(item, search_str_3)
