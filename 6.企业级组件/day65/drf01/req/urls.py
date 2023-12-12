
from django.contrib import admin
from django.urls import path, re_path, include
from req import views

urlpatterns = [
    # path('students/', views.StudentsView.as_view()),
    # re_path('students/(?P<pk>\d+)/', views.StudentsView.as_view()),
    #
    # path('students2/', views.Students2View.as_view()),
    # re_path('students2/(?P<pk>\d+)/', views.Students2View.as_view()),
    #
    # path('students3/', views.Students3View.as_view()),
    # re_path('students3/(?P<pk>\d+)/', views.Students3View.as_view()),
    #
    # path('students4/', views.Students4View.as_view()),
    # re_path('students4/(?P<pk>\d+)/', views.Students4View.as_view()),
    #
    # path('students5/', views.Students5View.as_view({'get':'get_all_students', 'post':'post'})),
    # re_path('students5/(?P<pk>\d+)/',
    #         views.Students5View.as_view({'get':'get_one_student', 'patch':'gengxin', 'delete':'shanchu'})),
    #
    # path('students6/', views.Students6View.as_view({'get': 'list', 'post': 'create'})),
    # re_path('students6/(?P<pk>\d+)/',
    #         views.Students6View.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),
    #
    # path('students7/', views.Students7View.as_view({'get': 'list', 'post': 'create'})),
    # re_path('students7/(?P<pk>\d+)/',
    #         views.Students7View.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),
]


from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

router = DefaultRouter()
# router = SimpleRouter()
router.register('students', views.Students7View)
urlpatterns += router.urls