from django.shortcuts import render, HttpResponse

# Create your views here.

def home(requesst):
    return HttpResponse('ok')

def index(request):
    return HttpResponse('ok')

def index2(request):
    return HttpResponse('ok')

def books(request, y, m):
    print(y, m)     # 匹配出来的都是字符串
    return HttpResponse('%s-%s所有书籍都在这,你随便看' % (y, m))

def books2(request, month, year):
    print(year, month)  # 匹配出来的都是字符串
    return HttpResponse('%s-%s所有书籍都在这,你随便看' % (year, month))