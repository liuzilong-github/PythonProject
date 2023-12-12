
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from student import views

urlpatterns = [
    # path('students/', views.StudentView.as_view()),
]

url_obj = DefaultRouter()
url_obj.register('students', views.StudentView)
urlpatterns += url_obj.urls