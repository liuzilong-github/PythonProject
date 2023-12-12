from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator

from app01 import models

# Create your views here.


def islogin(func):
    def inner(request, *args, **kwargs):
        if request.session.get('is_login'):
            ret = func(request, *args, **kwargs)
            return ret
        else:
            return redirect('login')
    return inner


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        userinfo = models.UserInfo.objects.filter(username=uname, password=pwd)
        if userinfo.exists():
            request.session['is_login'] = True
            request.session['user_id'] = userinfo.first().id
            request.session['username'] = uname

            menu_list = userinfo.first().menus.all().values('id', 'title', 'url', 'icon')
            request.session['menu_data'] = list(menu_list)
            return redirect('books')
        return redirect('login')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        data = request.POST.dict()
        data.pop('confirm_password')
        data.pop('csrfmiddlewaretoken')
        models.UserInfo.objects.create(
            **data
        )
        return redirect('login')


class Logout(View):
    @method_decorator(islogin)
    def get(self, request):
        request.session.flush()
        return redirect('login')


from app01.utils.page import Pagenation
from django.db.models import Q


@islogin
def books(request):
    param_dict = request.GET.dict()    # {'title__contains': '1', 'price': '2', 'publishs__name__contains': '3'}
    print(param_dict)    # {'title__contains': '穷爸爸', 'authors__name__contains': '苑', 'publishs__name__contains': ''}
    # models.Book.objects.filter(title__contains='穷爸爸', authors__name__contains='苑', publishs__name__contains='')
    # search_title = request.GET.get('search_title')    # xx
    # search_price = request.GET.get('search_price')    # 12
    # search_publish = request.GET.get('search_publish')    # 红浪漫

    # filter_condition = {
    #     'title__contains': search_title,
    #     'price': search_price,
    #     'publishs__name__contains': search_publish
    # }
    # Q_filter_condition = Q(**{'title__contains': search_title})

    all_book_objs = models.Book.objects.all()

    # q查询方式 2
    q = Q()
    # q.connector = 'or'    # |
    # q.connector = 'and'    # 默认是and
    cc = []
    for k,v in param_dict.items():
        if k == 'page' or not v:
            continue
        # if k != 'page':
        #     continue
        # elif not v:
        #     continue
        q.children.append(k, v)    # ===  Q(title__contains=1)
        c1 = f'{k}={v}'
        cc.append(c1)
    cc_str = '&'.join(cc)
    # q.children.append('price', 12)    # ===  Q(price=12)      #Q(title__contains=1) | Q(price=12)
    print(q)
    all_book_objs = all_book_objs.filter(q)
    # all_book_objs = all_book_objs.filter(**param_dict)

    # Q1 = Q(title__contains=search_title)
    # Q2 = Q(price=search_price)
    # Q3 = Q(publishs__name__contains=search_publish)
    #
    # models.Book.objects.filter(Q1 | Q2 | Q3)    #title__contains=search_title,price=search_price,publishs__name__contains=search_publish

    current_page = request.GET.get('page')
    try:
        current_page = int(current_page)    # 没有page参数或者不是数字字符串
    except:
        current_page = 1

    total_count = all_book_objs.count()    # 总数据量
    page_obj = Pagenation(current_page, total_count, cc_str)

    book_objs = all_book_objs[page_obj.page_data_start:page_obj.end_data_start]

    # book_objs = models.Book.objects.all()[10:20] # 2
    # book_objs = models.Book.objects.all()[20:30] # 3

    return render(request, 'books.html', {'books_objs': book_objs, 'page_obj': page_obj})


class AddBook(View):
    @method_decorator(islogin)
    def get(self, request):
        publish_objs = models.Publish.objects.all()
        author_objs = models.Author.objects.all()
        return render(request, 'add_book.html', {'publish_objs': publish_objs, 'author_objs': author_objs})

    @method_decorator(islogin)
    def post(self, request):
        authors = request.POST.getlist('authors')
        data = request.POST.dict()
        data.pop('authors')
        book_obj = models.Book.objects.create(
            **data
        )
        book_obj.authors.add(*authors)
        return redirect('books')


class EditBook(View):
    @method_decorator(islogin)
    def get(self, request, book_id):
        old_book_obj = models.Book.objects.get(id=book_id)
        publish_objs = models.Publish.objects.all()
        author_objs = models.Author.objects.all()
        return render(request, 'edit_book.html', {'old_book_obj': old_book_obj, 'publish_objs': publish_objs, 'author_objs': author_objs})

    @method_decorator(islogin)
    def post(self, request, book_id):
        authors = request.POST.getlist('authors')
        data = request.POST.dict()
        data.pop('authors')
        old_book_obj = models.Book.objects.filter(id=book_id)
        old_book_obj.update(
            **data
        )
        old_book_obj.first().authors.set(authors)
        return redirect('books')


class DelBook(View):
    @method_decorator(islogin)
    def get(self, request, book_id):
        models.Book.objects.filter(id=book_id).delete()
        return redirect('books')


class AjaxDelBook(View):
    @method_decorator(islogin)
    def get(self, request, book_id):
        try:
            models.Book.objects.filter(id=book_id).delete()
            res_data = {'status': 0, 'msg': '删除成功!'}
        except:
            res_data = {'status': 1, 'msg': '删除失败!'}
        return JsonResponse(res_data)


class Authors(View):
    @method_decorator(islogin)
    def get(self, request):
        return render(request, 'authors.html')


class Publishs(View):
    @method_decorator(islogin)
    def get(self, request):
        return render(request, 'publishs.html')
