import datetime

from django.shortcuts import render
import time

# Create your views here.

def index(request):
    name = "赵万里"
    age = 18
    hobby = ['打游戏', '快乐风男', '嫖', 'look']
    d1 = {'a':'b', 'c': 'd'}
    file_size = 10283408
    xx = [11,]
    class A:
        def __init__(self):
            self.username = "万里"

        def my_hobby(self):
            return "张宇"
    now = datetime.datetime.now()
    ss = 'wanli ai zhangyu'
    a_tag = '<a href="http://www.baidu.com">百度<a/>'
    aa = 'hello ni hao'
    a = A()
    # dd = {
    # 	'name': name,
    # 	"age": age,
    # 	"hobby": hobby,
    # 	"d1": d1,
    # 	"a": a,
    # 	"xx": xx,
    # 	"file_size": file_size,
    # }
    dd = locals()
    # 'asdfasdfasdf{{hobby.0}}' --  hobby[0]
    # 模版渲染完成之后,才返回给浏览器,浏览器在进行页面渲染,生成效果
    return render(request, "index.html", dd)