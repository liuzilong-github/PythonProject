#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/1/5 17:31
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : operation.py
@Software: PyCharm

'''
import pickle
import os
import re
import random

from .card import Card
from .person import Person


class Operation():

	def __init__(self):
		self.get_user_info()
		self.get_userid_info()

	# 获取卡号=>用户信息
	def get_user_info(self):
		if os.path.exists("user.txt"):
			with open("user.txt", mode="rb") as fp:
				self.user_dict = pickle.load(fp)
				print(self.user_dict)
		else:
			self.user_dict = {}

	# 获取身份证号=>卡的信息
	def get_userid_info(self):
		if os.path.exists("user_id_dict"):
			with open("user_id_dict", mode="rb") as fp:
				self.user_id_dict = pickle.load(fp)
		else:
			self.user_id_dict = {}

	# 设置密码
	def get_pwd(self, information1, information2):
		while True:
			pwd1 = input(information1)
			if re.search(r"^\w{6}$", pwd1):
				if not pwd1.isdigit():
					pwd2 = input(information2)
					if pwd1 == pwd2:
						return pwd1
					else:
						print("对不起,两次密码输入不一致")
				else:
					print("对不起,密码不能为纯数字~")
			else:
				print("对不起,密码只能由6位数字,字母,下划线组成~")

	# 生成银行卡号
	def get_cardid(self):
		while True:
			cardid = str(random.randrange(100000, 1000000))
			if cardid not in self.user_dict:
				return cardid

	# 判断银行卡是否存在及银行卡状态
	def get_information(self, information):
		cardid = input(information)
		if cardid not in self.user_dict:
			print("对不起,您输入的卡号不存在~")
		else:
			user = self.user_dict[cardid]
			card = user.card
			if card.islock == False:
				return card
			else:
				print("对不起,您输入的卡片已锁定,无法操作~")

	# 验证银行卡密码
	def check_code(self, card):
		count = 1
		while count <= 3:
			pwd = input("请输入银行卡对应密码:")
			if pwd == card.password:
				return True
			else:
				print("密码输入错误,您还剩{}此机会".format(3 - count))
				if count == 0:
					card.islock = True
					print("对不起,密码输入错误次数超限,您的卡片已锁定,请联系管理员~")
				count += 1

	# 选择操作方式
	def get_mode(self, card, information):
		if card:
			mode = input(information)
			if mode == "1":
				old_pwd = input("请输入原密码:")
				if old_pwd == card.password:
					return True
				else:
					print("原密码输入错误~")
			elif mode == "2":
				print(card.cardid)
				user = self.user_dict[card.cardid]
				userid = input("请输入身份证号:")
				if userid == user.userid:
					return True
				else:
					print("身份证号输入错误")
			else:
				print("对不起,输入错误~")

	# 获取银行卡信息
	def get_card_information(self):
		cardid = input("请输入您的卡号:")
		if cardid not in self.user_dict:
			print("对不起,您输入的卡号不存在~")
		else:
			user = self.user_dict[cardid]
			return user.card

	# 判断输入金额是否正确
	def judge_money(self, card, information):
		if card:
			money = input(information)
			if money.isdigit():
				money = int(money)
				if money % 100 == 0:
					return money
			else:
				print("输入金额输入错误,请输入100的倍数")
		else:
			print("输入金额输入错误,请输入100的倍数")

	# 开户
	def register(self):
		while True:
			name = input("请输入您的姓名:")
			if name.isalpha():
				userid = input("请输入您的身份证号:")
				if re.search(r"^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$", userid):
					phone = input("请输入您的手机号:")
					if re.search(r"^1[3-9]\d{9}$", phone):
						password = self.get_pwd("请输入您的密码:", "请确认您的密码:")
						cardid = self.get_cardid()
						money = 10
						card = Card(cardid, password, money)
						user = Person(name, userid, phone, card)
						self.user_dict[cardid] = user
						self.user_id_dict[userid] = cardid
						print("恭喜{}开卡成功,您的卡号为:{},卡内余额{}元".format(name, cardid, money))
						break
					else:
						print("对不起,手机号不符合规则~")
				else:
					print("对不起,身份证号不符合规则~")
			else:
				print("对不起,姓名不符合规则~")

	# 查询
	def query(self):
		card = self.get_information("请输入您的卡号:")
		if card:
			if self.check_code(card):
				print("您的余额为{}元".format(card.money))

	# 存钱
	def save_money(self):
		card = self.get_information("请输入您的卡号:")
		if card:
			money = self.judge_money(card, "请输入您要存入的金额:")
			card.money += money
			print("取款成功,您的余额为{}元".format(card.money))

	# 取钱
	def get_money(self):
		card = self.get_information("请输入您的卡号:")
		if card:
			if self.check_code(card):
				money = self.judge_money(card, "请输入您要取款的金额:")
				if card.money >= money:
					card.money -= money
					print("取款成功,您的余额为{}元".format(card.money))
				else:
					print("对不起,余额不足~")

	# 转账
	def trans_money(self):
		transfer_card = self.get_information("请输入您的卡号:")
		if transfer_card:
			if self.check_code(transfer_card):
				collection_card = self.get_information("请输入您要转入的卡号:")
				if collection_card:
					money = self.judge_money(transfer_card, "请输入您要转入的金额:")
					if transfer_card.money >= money:
						transfer_card.money -= money
						collection_card.money += money
						print("转账成功,您的余额为{}元".format(transfer_card.money))
					else:
						print("对不起,余额不足~")

	# 改密
	def change_pwd(self):
		card = self.get_information("请输入您的卡号:")
		if card:
			if self.check_code(card):
				mode = self.get_mode(card, "请选择改密方式:(1)原密码改密 (2)身份证改密")
				if mode:
					new_pwd = self.get_pwd("请输入新密码:", "请确认密码:")
					card.password = new_pwd
					print("恭喜您,密码修改成功~")

	# 锁卡
	def lock(self):
		card = self.get_information("请输入您的卡号:")
		if card:
			if self.check_code(card):
				mode = self.get_mode(card, "请选择锁卡方式:(1)使用密码冻结 (2)使用身份证号冻结")
				if mode:
					card.islock = True
					print("锁卡成功~")

	# 解卡
	def unlock(self):
		card = self.get_card_information()
		if card.islock:
			if self.check_code(card):
				user = self.user_dict[card.cardid]
				userid = input("请输入身份证号:")
				if userid == user.userid:
					card.islock = False
					print("您的卡片已解除锁定,可以进行业务操作~")
				else:
					print("身份证号输入错误")
		else:
			print("您的卡片状态正常,无需进行此操作~")

	# 补卡
	def new_card(self):
		card = self.get_card_information()
		if card:
			if self.check_code(card):
				new_cardid = self.get_cardid()
				user = self.user_dict[card.cardid]
				self.user_id_dict[user.userid] = new_cardid
				self.user_dict[new_cardid] = user
				self.user_dict.pop(card.cardid)
				card.cardid = new_cardid
				print("补卡成功,请将原卡沿磁条剪开后销毁~")

	# 保存并退出atm
	def save(self):
		with open("user.txt", mode="wb") as fp:
			pickle.dump(self.user_dict, fp)

		with open("userid.txt", mode="wb") as fp:
			pickle.dump(self.user_id_dict, fp)
		print("您已退出atm,请取走您的卡片~")