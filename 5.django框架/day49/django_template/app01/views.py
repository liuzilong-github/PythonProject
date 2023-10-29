from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    name = '赵万里'
    age = 16
    number = 101
    hobby = ['打游戏', '快乐风男', '嫖', 'look']
    hobby2 = {'xx': [11, 22, 33], 'oo': ['aa', 'bb', 'cc']}
    d1 = {'a': 'b', 'c': 'd'}
    d2 = {'items': [11, 22, 33]}

    file_size = 10283408
    xx = [11, ]

    class A:
        def __init__(self):
            self.username = '万里'

        def my_hobby(self):
            return '张宇'

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
    # 模板渲染完成之后, 才返回给浏览器, 浏览器再进行页面渲染, 生成效果
    return render(request, 'index.html', dd)

def csrf(request):
    if request.method == "GET":
        return render(request, "csrf.html")
    else:
        print(request.POST)
        return HttpResponse("ok")

def t1(request):
    return render(request, "t1.html")

def t2(request):
    return render(request, "t2.html")

def t3(request):
    return render(request, "t3.html")

def zujian(request):
    number = 100
    name = "chao"
    return render(request, "home.html", locals())

def tan(request):
    return render(request, "tan.html")

def bb(request):
    return render(request, "bb.html")

def basic(request):
    # if user.type == "admin":
    #     menu_list = [11, 22, 33, 44, 55, 66]
    # else:
    menu_list = [22, 33]
    return render(request, "basic.html", {"menu_list": menu_list})
