from django.shortcuts import render
from django.views import View
from app01 import models
from django.http import JsonResponse
from student.serializer import StudentSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


# class StudentView(View):
#     def get(self, request):
#         students = models.Student.objects.all()
#         serializer_obj = StudentSerializer(instance=students, many=True)
#         print(serializer_obj.data, type(serializer_obj.data))
#         return JsonResponse(serializer_obj.data, safe=False, json_dumps_params={"ensure_ascii":False})


class StudentView(ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

