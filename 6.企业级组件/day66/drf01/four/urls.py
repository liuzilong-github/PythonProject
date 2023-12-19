
from django.contrib import admin
from django.urls import path, re_path, include
from four import views

urlpatterns = [
    path('students/', views.StudentView.as_view()),
    # re_path('students/', views.StudentView.as_view())
]