#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2022/11/2 17:18
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : register.py
@Software: PyCharm

'''
import os
import json


def query_username(file_name, username):
	if os.path.getsize(file_name):
		with open(file_name, mode="r", encoding="utf-8") as fp1:
			for i in fp1.readlines():
				if eval(i)["username"] == username:
					break
			else:
				return True
	else:
		return True


def save_user_information(file_name, username, password):
	with open(file_name, mode="a", encoding="utf-8") as fp:
		fp.write(str({"username": username, "password": password}) + "\n")


while True:
	username = input("请输入您的用户名:")
	if query_username("user_information.json", username):
		password = input("请输入您的密码:")
		while True:
			confirm_password = input("请再次输入您的密码:")
			if password != confirm_password:
				print("两次输入的密码不一致")
			else:
				save_user_information("user_information.json", username, password)
				break
		break
	else:
		print("对不起,用户名已存在,请重新输入")