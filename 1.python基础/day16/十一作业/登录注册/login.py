#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2022/11/2 17:18
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : login.py
@Software: PyCharm

'''
import os


with open("black_list.txt", mode="r", encoding="utf-8") as fp:
	black_list = [i.strip() for i in fp.readlines()]
	username = input("请输入您的用户名:")
	if username not in black_list:
		if os.path.getsize("user_information.json"):
			with open("user_information.json", mode="r+", encoding="utf-8") as fp1:
				for i in fp1.readlines():
					if eval(i)["username"] == username:
						password = input("请输入您的密码:")
						login_total = 0
						while True:
							if eval(i)["password"] == password:
								if login_total <= 3:
									print("登录成功")
									break
							else:
								login_total += 1
								print("对不起,密码输入错误,您还剩{}次机会".format(3-login_total))
								if login_total == 3:
									with open("black_list.txt", mode="a", encoding="utf-8") as fp:
										fp.write(username + "\n")
									print("您的账户已锁定")
									break
							password = input("请重新输入您的密码:")
						break
				else:
					print("对不起,您输入的账户不存在")
	else:
		print("对不起,您的账户已锁定")


