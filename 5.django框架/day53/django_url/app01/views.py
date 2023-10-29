from django.shortcuts import render, HttpResponse
from django.urls import reverse

# Create your views here.


def index(request):
    print('app01>>>>>', reverse('app01:index'))
    return HttpResponse('app01-index')