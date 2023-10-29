from django.conf.urls import url
from app03 import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
]