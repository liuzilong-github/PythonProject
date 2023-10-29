from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def books(request):
    books_list = models.Book.objects.all()
    return render(request, 'books.html', {'books_list': books_list})


def add_book(request):
    if request.method == "GET":
        return render(request, 'add_book.html')
    elif request.method == "POST":
        # dict()将querydict类型数据转化为普通字典类型数据
        data = request.POST.dict()
        models.Book.objects.create(
            **data
        )
        return redirect('/books/')


def edit_book(request, book_id):
    if request.method == "GET":
        old_obj = models.Book.objects.get(id=book_id)
        return render(request, 'edit_book.html', {'old_obj': old_obj})
    elif request.method == "POST":
        data = request.POST.dict()
        models.Book.objects.filter(id=book_id).update(
            **data
        )
        return redirect('/books/')


def del_book(request, book_id):
    models.Book.objects.filter(id=book_id).delete()
    return redirect('/books/')