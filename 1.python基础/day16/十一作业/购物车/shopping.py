#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2022/11/3 10:59
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : shopping.py.py
@Software: PyCharm

'''
import time
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

choice_shopping_information = """*****************************
您当前选择的商品具体信息为:
*-商品名称为: {}
*-商品价格为: {}
*-商品数量为: {}
已成功加入购物车,请继续选择商品或进行结账
*****************************"""


def query_shopping_data(file_name):
	print("商品正在加载中...")
	progress_bar()
	with open(file_name, mode="r", encoding="utf-8") as fp:
		shopping_data = [eval(i) for i in fp.readlines()]
		print("[===========有如下商品供您选择：===========]")
		print("序号      名称       价格")
		space = "      "
		for i in shopping_data:
			print(shopping_data.index(i) + 1, space, i["name"], space, i["price"])
		return shopping_data


def progress_bar():
	for i in range(1, 51):
		time.sleep(0.1)
		print("\r[%-50s] %d%%" % (i * "#", i * 2), end="")
	print()


shopping_money = input("欢迎光临~请输入您要充值的金额:")
if shopping_money.isdigit():
	print("恭喜您~成功充值{}元".format(shopping_money))
	shop_data = query_shopping_data("shopping_data.json")
	for shop in shop_data:
		shop["total"] = 0
	while True:
		shopping_no = input("请输入您要购买的商品序号,输入N进行购物车结算,输入Q结束购物:")
		shopping_no_list = [str(shop_data.index(i) + 1) for i in shop_data]
		if shopping_no in shopping_no_list:
			shop_data[int(shopping_no) - 1]["total"] += 1
			print(choice_shopping_information.format(shop_data[int(shopping_no) - 1]["name"], shop_data[int(shopping_no) - 1]["price"], shop_data[int(shopping_no) - 1]["total"]))
		elif shopping_no.upper() == "N":
			while True:
				total_price = 0
				print("[-------------您购物车的商品信息如下-------------]")
				for shop in shop_data:
					if shop["total"] != 0:
						total_price += (shop["price"] * shop["total"])
						print("序号: {} 商品名称: {} 商品单价: {} 商品数量: {} 此商品总价: {}".format(shop_data.index(shop) + 1, shop["name"], shop["price"], shop["total"], shop["price"] * shop["total"]))
				if total_price > int(shopping_money):
					print("余额不足,还差{}元,请忍痛割爱删除某些商品".format(total_price - int(shopping_money)))
					del_shop = input("您要删除的商品是: ")
					shop_data[int(del_shop) - 1]["total"] -= 1
				else:
					print("正在结算中,请稍后...")
					progress_bar()
					print("您已成功购买以上全部商品,本次总共消费{}元,余额{}元,欢迎您下次光临".format(total_price, int(shopping_money) - total_price))
					break
			break
		elif shopping_no.upper() == "Q":
			print("欢迎您下次光临~")
			break
		else:
			print("对不起,您输入的序号有误,请重新输入")
else:
	print("对不起,您输入的内容不正确~")
