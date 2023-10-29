#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/10/9 21:34
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : xx.py
@Software: PyCharm

'''

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_pagenation.settings")
import django
django.setup()


from app01 import models


obj_lsit = []
for i in range(100):
	book_obj = models.Book(
		title=f'白洁{i}',
		price=i,
		publishDate='2020-11-11',
		publishs_id=1,

	)
	obj_lsit.append(book_obj)

models.Book.objects.bulk_create(obj_lsit)

