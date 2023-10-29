#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2022/9/1 19:26
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : day10作业.py
@Software: PyCharm

'''

# 1.定义函数:接收任意个参数,打印其中的最小值
# def min_value(*args):
# 	lst = []
# 	for i in args:
# 		if isinstance(i, (float, int)):
# 			lst.append(i)
# 	value = lst[0]
# 	for i in lst:
# 		if i <= value:
# 			value = i
# 	return value
#
# res = min_value(200,-100,1,2,423,"sdf")
# print(res)

def min_value(*args):
	lst = []
	for i in args:
		if isinstance(i, (float, int)):
			lst.append(i)
	return sorted(lst)[0]

res = min_value(200,-100,1,2,423,"sdf")
print(res)

# 2.定义函数:传入一个参数n，返回n的阶乘(5! = 5*4*3*2*1)
def factorial(n):
	total = 1
	for i in range(1,n+1):
		total *= i
	return total

res = factorial(3)
print(res)

def factorial(n):
	if n <= 1:
		return 1
	return factorial(n-1) * n

res = factorial(3)
print(res)

# 3.写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等)
# # 将容器中的每个元素依次添加到新的列表中返回
#例:传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
from collections.abc import Iterable

def add_lst(*args):
	lst = []
	for i in args:
		if isinstance(i, Iterable):
			for j in i:
				lst.append(j)
		else:
			continue
	return lst

res = add_lst([1,2,3],(22,33))
print(res)

# 4.写函数，用户传入要修改的文件名，与要修改的内容，执行函数，修改操作
# def modify_file(filename, old_content, new_content):
# 	with open(filename, mode="r", encoding="utf-8") as fp:
# 		res = fp.read()
# 		res.replace(old_content, new_content)
# 	with open(filename, mode="w", encoding="utf-8") as fp:
# 		fp.write(res)
#
# modify_file("ceshi2.py","外置函数","内置函数")

# 5.写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def str_count(str):
	dic = {"number":0, "letter":0, "space":0, "other":0}
	for i in str:
		if i.isdigit():
			dic["number"] += 1
		elif i.isalpha():
			dic["letter"] += 1
		elif i.isspace():
			dic["space"] += 1
		else:
			dic["other"] += 1
	return dic

res = str_count("sdkfhds1832293784328  dasdas88!@#$%^")
print(res)

# 6.写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，返回处理后的结果.
	#例:参数为:dic = {"k1": "v1v1", "k2": [11,22,33,44]}
def intercept_dic(dic):
	if isinstance(dic, dict):
		for i in dic:
			if len(dic[i]) > 2:
				dic[i] = dic[i][:2]
	else:
		return "不是字典"
	return dic

res = intercept_dic({"k1": "v1v1", "k2": [11,22,33,44]})
print(res)

# 7传入多个容器类型数据,计算所有元素的个数
def calculations_count(*args):
	total = 0
	for i in args:
		if isinstance(i, Iterable):
			total += len(i)
	return total

res = calculations_count([1,2,3],(22,33))
print(res)