
from django.contrib import admin
from django.urls import path, re_path, include
from mser import views


urlpatterns = [
    path('students/', views.StudentsView.as_view())
]
