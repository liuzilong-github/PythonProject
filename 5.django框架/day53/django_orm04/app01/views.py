from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.urls import reverse
from django.db.models import F, Q

from app01 import models


# Create your views here.
def books(request):
    print(reverse('books'))     # /books/ reverse('别名名称')来反向解析别名对应的路径
    print(reverse('add_book'))     # /add_book/
    # 当url用的是无名分组参数时,reverse反向解析路径用args传参
    print(reverse('edit_book', args=(3, )))    # /edit_book/3/
    # 当url用的是有名分组参数时,reverse反向解析路径用kwargs传参
    print(reverse('del_book', kwargs={'book_id': 3,}))     # /del_book/3/
    books_objs = models.Book.objects.all()
    print(books_objs)
    return render(request, 'books.html', {'books_objs': books_objs})


class AddBook(View):
    def get(self, request):
        publish_objs = models.Publish.objects.all()
        author_objs = models.Author.objects.all()
        return render(request, 'add_book.html', {'publish_objs': publish_objs, 'author_objs': author_objs})

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
    def get(self, request, book_id):
        old_book_obj = models.Book.objects.get(id=book_id)
        publish_objs = models.Publish.objects.all()
        author_objs = models.Author.objects.all()
        return render(request, 'edit_book.html', {'old_book_obj': old_book_obj, 'publish_objs': publish_objs, 'author_objs': author_objs})

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
    def get(self, request, book_id):
        models.Book.objects.filter(id=book_id).delete()
        return redirect('books')


def query(request):
    # F查询
    # 查询一下点赞数大于评论数的所有书籍
    books = models.Book.objects.all()
    book_list = []
    for book in books:
        if book.dianzan > book.comment:
            book_list.append(book)

    books = models.Book.objects.filter(dianzan__gt=F('comment'))    # F('属性名称)
    print(books.values('title'))

    # 所有书籍价格上调10元
    books = models.Book.objects.all()
    for book in books:
        book.price += 10
        book.save()

    models.Book.objects.all().update(price=F('price') + 10)   # 支持四则运算

    # Q查询   | -- or    & -- and    ~ -- not
    # 查询一下点赞数大于10并且评论数大于10的所有书籍
    models.Book.objects.filter(Q(dianzan__gt=10) & Q(comment__gt=10))
    models.Book.objects.filter(dianzan__gt=10, comment__gt=10)

    # 查询一下点赞数大于10或者评论数大于10的所有书籍
    ret = models.Book.objects.filter(Q(dianzan__gt=10) | Q(comment__gt=10)).values('title')
    print(ret)

    # 查询一下点赞数大于10或者评论数大于10的并且价格大于30的
    ret = models.Book.objects.filter(Q(Q(dianzan__gt=10) | Q(comment__gt=10)), price__gt=30).values('title')
    ret = models.Book.objects.filter(Q(Q(dianzan__gt=10) | Q(comment__gt=10)) & Q(price__gt=30)).values('title')
    print(ret)

    # 查询一下点赞数大于10或者评论数大于10的并且价格小于等于30的
    ret = models.Book.objects.filter(Q(Q(dianzan__gt=10) | Q(comment__gt=10)) & ~Q(price__gt=30)).values('title')
    print(ret)

    return HttpResponse('ok')