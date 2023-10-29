"""django_url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),     # 匹配根路径的写法
    url(r'^index/$', views.index),
    url(r'^index/xx/xx', views.index2),
    # url(r'^books/$', views.books),
    # url(r'^books/(\d+)/', views.books),     # /books/2019/  # 2019
    # url(r'^books/(\d+)/(\d+)/', views.books),   # 无名分组,位置参数,注意参数位置固定
    # url(r'^books/(?P<year>\d+)/', views.books2),
    url(r'^books2/(?P<year>\d+)/(?P<month>\d+)/', views.books2)     # /books2/2019/ #year:2019 # 有名分组,关键字参数
    # def books2(request, year, month)  函数参数必须和有名分组的名称相同,不在乎参数位置
]

"""
import re

request.path == "/index/"
for url in urlpatterns:
    # url[0] -> ^index/
    if re.match(url[0], request.path):
        url[1](request,)
        break
else:
    print("找不到路径")
"""