
from django.contrib import admin
from django.urls import path, re_path, include
from ser import views

urlpatterns = [
    path('students/', views.StudentsView.as_view()),  #ser/students/
]

