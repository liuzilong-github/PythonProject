from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from ser import models
# from ser.serializer import StudentSerializer, StudentSerializer2
from ser.serializers import StudentSerializer3
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
        serializer_obj = StudentSerializer3(data=request.data, context={'request':request})
        # s = serializer_obj.is_valid(raise_exception=True)   # return JsonResponse(错误信息, status=400)
        if serializer_obj.is_valid():    # 所有字段都校验没有问题,返回True, 但凡有一个字段校验失败,返回False
            print("校验成功之后的数据", serializer_obj.validated_data)
            # 方式1
            # new_obj = models.Student.objects.create(**serializer_obj.validated_data)
            # obj = StudentSerializer3(instance=new_obj)

            # 方式2
            new_obj = serializer_obj.save()    # 会自动触发serializer_obj对应的StudentSerializer3中的create方法
            obj = StudentSerializer3(instance=new_obj)
            # 然后保存数据
            # return JsonResponse(serializer_obj.validated_data)
            return JsonResponse(obj.data)
        else:
            print(serializer_obj.errors)
            return JsonResponse({'error': '校验失败'}, status=400)

    def put(self, request):
        objs = models.Student.objects.filter(id=request.data.get('id'))
        obj = objs.first()

        serializer_obj = StudentSerializer3(data=request.data, partial=True, instance=obj)
        # 实例化序列化器类的对象时,如果传递了isntance=模型类对象参数,那么将来通过serializer_obj.save() 会触发执行类中的update方法
        # 实例化序列化器类的对象时,如果没有传递instance=模型类对象参数,那么将来通过serializer_obj.save() 回触发执行类中的create方法

        # partial=True 进行部分字段校验,也就是说,传递过来哪个字段数据,就校验哪个字段数据,没有传递过来的不校验
        # {'name': 'xxx', "age": 18} 只校验name和age的数据,其他数据不校验(即使是序列化类中要求必填额数据,也是直接忽略的)
        # 这个参数一般是在更新时使用的
        if serializer_obj.is_valid():
            # validated_date
            # id = request.data.get('id')   # 由于id值不需要校验,所以在validated_data里面没有id数据,所以我们通过request.data来获取
            # print('id>>>', id)
            # 方式1
            # objs = models.Student.objects.filter(id=id)
            # print(objs.values('id', 'name', 'age'))
            # objs.update(**serializer_obj.validated_data)
            # new_obj = objs.update()
            # obj = StudentSerializer3(instance=new_obj)

            # 方式2 save方法更新
            new_obj = serializer_obj.save()
            obj = StudentSerializer3(instance=new_obj)

            return JsonResponse(obj.data)
        else:
            return JsonResponse({'error':'校验失败'}, status=400)