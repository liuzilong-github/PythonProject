#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/1/5 17:29
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : main.py.py
@Software: PyCharm

'''
from package.view import View
from package.operation import Operation


class Main():

	@staticmethod
	def run():
		if View.admin_login():
			obj = Operation()
			while True:
				choice = input("请选择需要办理的业务:")
				if choice == "1":
					obj.register()
				elif choice == "2":
					obj.query()
				elif choice == "3":
					obj.save_money()
				elif choice == "4":
					obj.get_money()
				elif choice == "5":
					obj.trans_money()
				elif choice == "6":
					obj.change_pwd()
				elif choice == "7":
					obj.lock()
				elif choice == "8":
					obj.unlock()
				elif choice == "9":
					obj.new_card()
				elif choice == "0":
					obj.save()
					break
				else:
					print("选择业务错误,请重新选择~")


if __name__ == '__main__':
	Main.run()