from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from ser import models
# from ser.serializer import StudentSerializer, StudentSerializer2
from ser.serializer import StudentSerializer3
from rest_framework.views import APIView

# Create your views here.


# class StudentsView(APIView):
# # class StudentsView(View):
#     def get(self, request):
#         # queryset类型数据
#         # students = models.Student.objects.all()
#         # serializer_obj = StudentSerializer(instance=students, many=True)    # 列表套字典
#
#         # 序列化单条数据(模型类对象)
#         students = models.Student.objects.get(id=1)
#         serializer_obj = StudentSerializer(instance=students)    # 字典
#
#         print(serializer_obj.data, type(serializer_obj.data))
#         return JsonResponse(serializer_obj.data, safe=False, json_dumps_params={"ensure_ascii":False})
#
#     def post(self, request):
#         # print(">>>>>>", request.POST)    # 由于用户提交的数据有可能是JSON数据,django解析不了,所以我们借助drf来解析,就需要继承drf的APIView类
#         print(">>>>>>", request.data)    # {'name': 'chaochaochao', 'age': 18}字典类型数据
#         serializer_obj = StudentSerializer2(data=request.data)
#         if serializer_obj.is_valid():    # 所有字段都校验没有问题,返回True, 但凡有一个字段校验失败,返回False
#             print("校验成功之后的数据", serializer_obj.validated_data)
#             # 然后保存数据
#             return JsonResponse(serializer_obj.validated_data)
#         else:
#             print(serializer_obj.errors)
#             return JsonResponse({'error': '校验失败'}, status=400)


class StudentsView(APIView):
# class StudentsView(View):
    def get(self, request):
        # queryset类型数据
        students = models.Student.objects.all()
        serializer_obj = StudentSerializer3(instance=students, many=True)    # 列表套字典

        # 序列化单条数据(模型类对象)
        # students = models.Student.objects.get(id=1)
        # serializer_obj = StudentSerializer3(instance=students)    # 字典

        print(serializer_obj.data, type(serializer_obj.data))
        return JsonResponse(serializer_obj.data, safe=False, json_dumps_params={"ensure_ascii":False})

    def post(self, request):
        # print(">>>>>>", request.POST)    # 由于用户提交的数据有可能是JSON数据,django解析不了,所以我们借助drf来解析,就需要继承drf的APIView类
        print(">>>>>>", request.data)    # {'name': 'chaochaochao', 'age': 18}字典类型数据
        serializer_obj = StudentSerializer3(data=request.data)
        if serializer_obj.is_valid():    # 所有字段都校验没有问题,返回True, 但凡有一个字段校验失败,返回False
            print("校验成功之后的数据", serializer_obj.validated_data)
            # 然后保存数据
            return JsonResponse(serializer_obj.validated_data)
        else:
            print(serializer_obj.errors)
            return JsonResponse({'error': '校验失败'}, status=400)