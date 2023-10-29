#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2022/12/1 19:24
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : shooting.py
@Software: PyCharm

'''


class Shooting():

	def __init__(self, gun):
		self.gun = gun

	def replenish_bullets(self, bullet_count):
		self.gun.magazine.bullet_count += bullet_count

	def fire(self, fire_count):
		self.gun.gun(fire_count)




