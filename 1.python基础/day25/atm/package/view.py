#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/1/5 17:30
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : view.py
@Software: PyCharm

'''
import time


class View():

	def admin_login():
		username = input("请输入管理员账号:")
		password = input("请输入管理员密码:")
		if username == "admin" and password == "123456":
			View.welcome_view()
			time.sleep(0.5)
			View.operation_view()
			return True
		else:
			print("管理员账号或密码输入错误")

	@staticmethod
	def welcome_view():
		print("*******************************************")
		print("*                                         *")
		print("*                                         *")
		print("*         Welcome To OldBoy Bank          *")
		print("*                                         *")
		print("*                                         *")
		print("*******************************************")

	@staticmethod
	def operation_view():
		print("*******************************************")
		print("*           开户(1)    查询(2)             *")
		print("*           存钱(3)    取钱(4)             *")
		print("*           转账(5)    改密(6)             *")
		print("*           锁卡(7)    解卡(8)             *")
		print("*           补卡(9)    退出(0)             *")
		print("*******************************************")


if __name__ == '__main__':
	View.admin_login()