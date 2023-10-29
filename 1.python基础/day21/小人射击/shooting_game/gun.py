#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2022/12/1 19:24
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : gun.py
@Software: PyCharm

'''


class Gun():

	def __init__(self, magazine):
		self.magazine = magazine

	def gun(self, fire_count):
		if self.magazine.bullet_count > fire_count:
			# print(self.magazine.bullet_count, fire_count)
			self.magazine.bullet_count -= fire_count
			print("突突突!" * fire_count, "还剩{}子弹".format(self.magazine.bullet_count))
		else:
			print("子弹不足,无法射击,请填充子弹~")
