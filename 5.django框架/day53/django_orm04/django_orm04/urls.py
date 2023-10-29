"""django_orm04 URL Configuration

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
    url(r'^books/', views.books, name='books'),     # 给路径起别名
    url(r'^add_book/', views.AddBook.as_view(), name='add_book'),
    url(r'^edit_book/(\d+)/', views.EditBook.as_view(), name='edit_book'),
    url(r'^del_book/(?P<book_id>\d+)/', views.DelBook.as_view(), name='del_book'),

    url(r'^query/', views.query)
]
