#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2022/11/9 21:37
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : 计算文件夹大小.py
@Software: PyCharm

'''
# ### 计算文件夹整体大小

import os

# (1) 找出路径,文件夹,文件

# 获取文件夹所在的路径
print(os.getcwd())  # 默认获取当前文件所在的路径
pathvar = os.path.join(os.getcwd(), "ceshi1")
print(pathvar)

# 获取文件夹中所有的文件内容
lst = os.listdir(pathvar)

# 计算里面文件大小
size = 0
for i in lst:
	# 将文件内容和路径拼接 => 绝对路径
	pathnew = os.path.join(pathvar, i)
	if os.path.isdir(pathnew):
		print(i, "[文件夹]")
	elif os.path.isfile(pathnew):
		print(i, "[文件]")
		size += os.path.getsize(pathnew)

print(size)  # 23346字节


# (2) 计算文件夹中的大小

def getallsize(pathvar):
	lst = os.listdir(pathvar)
	print(lst)
	# 设置总大小默认为0
	size = 0

	for i in lst:
		# 拼凑绝对路径
		pathnew = os.path.join(pathvar, i)
		if os.path.isdir(pathnew):
			size += getallsize(pathnew)
		elif os.path.isfile(pathnew):
			size += os.path.getsize(pathnew)
	return size


print(pathvar)
res = getallsize(pathvar)
print(res)  # 38910
# ['ceshi2', 'lianxi1.php', 'lianxi2.py']
# pathvar = "/mnt/hgfs/python32_gx/day18/ceshi1"


