#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2022/12/1 19:22
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : main.py
@Software: PyCharm

'''

from shooting_game.magazine import Magazine
from shooting_game.gun import Gun
from shooting_game.shooting import Shooting

obj1 = Magazine(10)
obj2 = Gun(obj1)
obj3 = Shooting(obj2)


if __name__ == '__main__':
	obj3.fire(1)
	obj3.replenish_bullets(10)
	obj3.fire(10)