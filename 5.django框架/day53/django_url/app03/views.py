from django.shortcuts import render, HttpResponse
from django.urls import reverse

# Create your views here.


def index(request):
    print('app03>>>>>', reverse('app03:index'))
    return HttpResponse('app03-index')