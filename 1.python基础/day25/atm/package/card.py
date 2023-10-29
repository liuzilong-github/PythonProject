#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/1/5 17:29
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : card.py
@Software: PyCharm

'''


class Card():

	def __init__(self, cardid, password, money):
		self.cardid = cardid
		self.password = password
		self.money = money
		self.islock = False