#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
@Time    : 2023/9/17 17:54
@Author  : liuzilong
@Email   : Liuzl940914@163.com
@File    : mytag.py
@Software: PyCharm

'''

from django import template

register = template.Library()

@register.inclusion_tag('menu.html')
def menu_tag(request):
    # 当前请求路径
    current_path = request.path

    menu_data = request.session.get('menu_data')
    # [{'title':'图书管理','url':'/books/'},{'title':'作者管理','url':'/authors/','class':'menu_color'},{'title':'出版社管理','url':'/publishs/'}]
    # xx = []
    for menu in menu_data:
        if current_path == menu['url']:
            menu['class'] = 'menu_color'
    return {'menu_dict': menu_data}
