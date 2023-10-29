from django.shortcuts import render
from app01.utils.page import Pagenation

# Create your views here.
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


@islogin
def books(request):
    current_page = request.GET.get('page')
    try:
        current_page = int(current_page)
    except:
        current_page = 1
    all_books_objs = models.Book.objects.all()
    total_count = all_books_objs.count()
    page_objs = Pagenation(current_page, total_count)

    books_objs = models.Book.objects.all()[page_objs.page_data_start:page_objs.page_data_end]
    return render(request, 'books.html', {'books_objs': books_objs, 'page_objs': page_objs})


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
        print(data)
        data.pop('authors')
        data.pop('csrfmiddlewaretoken')
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
