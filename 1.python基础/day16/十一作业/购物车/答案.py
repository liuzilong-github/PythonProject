#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2022/11/21 19:59
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : 答案.py
@Software: PyCharm

'''

import time
import json
# 1. 用户先给自己的账户充钱：比如先充3000元。
# 2. 页面显示 序号 + 名称 + 价格 , 如：
# [===========有如下商品供您选择：===========]
# 序号     名称       价格
# 1 		 电脑		1999
# 2 		 鼠标		10
# 3 		 游艇		20
# 4 		 美女		998
# n或N	购物车结算
# q或Q	退出程序(如不结算购物车可直接退出)]
# [==========================================]
# 购物车结算
# 3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
# 4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 5. (1)用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价
#    (2)若充值的钱数不足则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买退出
#    (3)退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少
# 6. 用户输入Q或者q 直接退出程序。

shopping_money = 0
shopping_car = {}


def recharge():
	global shopping_money
	while True:
		shopping_money = input("欢迎光临~请输入您要充值的金额:")
		if shopping_money.isdigit():
			shopping_money = int(shopping_money)
			print("恭喜您~成功充值{}元".format(shopping_money))
			break
		else:
			print("对不起,您输入的内容不正确~")


def progress_bar():
	for i in range(1, 51):
		time.sleep(0.1)
		print("\r[%-50s] %d%%" % (i * "#", i * 2), end="")
	print()


def get_goods(filename):
	lst = []
	with open(filename, mode="r", encoding="utf-8") as fp:
		for i in fp:
			dic = json.loads(i)
			lst.append(dic)
	return lst


def show_goods(goods):
	strvar = "商品名称".center(18)
	print("序号" + strvar + "价格")
	for k,v in enumerate(goods, start=1):
		v["num"] = k
		print("{v[num]:<10}{v[name]:<12}{v[price]}".format(v=v))


def error():
	strvar = """
**************************************************
*           您输入的选项不存在 , 请重新输入          *
**************************************************
	"""
	print(strvar)
	time.sleep(0.5)


def add_car(num, goods):
	if num not in shopping_car:
		shopping_car[num] = {
			"name": goods[num - 1]["name"],
			"price": goods[num - 1]["price"],
			"account": 1
		}
	else:
		shopping_car[num]["account"] += 1


def show_car(num):
	print("*" * 50)
	print("您当前选择的商品具体信息为:")
	print("*-商品名称为: {}".format(shopping_car[num]["name"]))
	print("*-商品价格为: {}".format(shopping_car[num]["price"]))
	print("*-商品数量为: {}".format(shopping_car[num]["account"]))
	print("已成功加入购物车,请继续选择商品或进行结账")
	print("*" * 50)


def balance():
	total_price = 0
	for k, v in shopping_car.items():
		v["num"] = k
		v["total_price_of_goods"] = v["price"] * v["account"]
		total_price += v["total_price_of_goods"]
		print("序号: {v[num]} 商品名称: {v[name]} 商品单价: {v[price]} 商品数量: {v[account]} 此商品总价: {v[total_price_of_goods]}".format(v=v))
	return total_price


def settlement_succeed(total_price, shopping_money):
	print("正在结算中,请稍后...")
	progress_bar()
	print("请稍后...")
	print("[一共: {}元]".format(total_price))
	print("[您已经成功购买以上所有商品 , 余额还剩{}元，感谢您下次光临~]".format(shopping_money - total_price))
	time.sleep(1)


def del_goods(total_price, shopping_money):
	print("余额不足,还差{}元,请忍痛割爱删除某些商品".format(total_price - shopping_money))
	del_goods_num = input("[-------------------请输入要删除的商品序号:-------------------]")
	if del_goods_num.isdecimal():
		del_goods_num = int(del_goods_num)
		if del_goods_num in shopping_car:
			shopping_car[del_goods_num]["account"] -= 1
			if not shopping_car[del_goods_num]["account"]:
				shopping_car.pop(del_goods_num)
		else:
			error()
	else:
		error()


def myexit():
	print("[============== 欢迎下次光临: ==============]")


def main():
	# 充值
	recharge()
	# 加载中
	progress_bar()
	# 获取商品
	goods = get_goods("shopping_data.json")
	# 展示商品
	show_goods(goods)
	# 结算商品
	while True:
		num = input("请输入您要购买的商品:")
		# 1.添加商品到购物车
		if num.isdecimal():
			num = int(num)
			if 1 <= num <= len(goods):
				# 把要购买的商品添加到购物车
				add_car(num, goods)
				# 展现一下购买的商品详情
				show_car(num)
			else:
				error()
		# 2.结算商品
		elif num.upper() == "N":
			while True:
				# 结算出总价格
				total_price = balance()
				if total_price > shopping_money:
					# 删除商品
					del_goods(total_price, shopping_money)
				else:
					# 正常结算
					settlement_succeed(total_price, shopping_money)
					break
			break
		# 3.退出购物
		elif num.upper() == "Q":
			myexit()
			break
		else:
			error()


main()