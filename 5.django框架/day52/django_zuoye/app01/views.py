from django.shortcuts import render, redirect
from django.views import View

from app01 import models


# Create your views here.
def books(request):
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
        return redirect('/books/')


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
        return redirect('/books/')


class DelBook(View):
    def get(self, request, book_id):
        models.Book.objects.filter(id=book_id).delete()
        return redirect('/books/')