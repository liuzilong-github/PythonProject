from django.shortcuts import render
from django.views import View
from ser import models
from req.serializers import StudentModelSerializer, StudentModelSerializer2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class StudentsView(APIView):
    # 获取所有数据
    def get(self, request):
        # http://127.0.0.1:8000/req/students/?a=1&b=2&b=3  b可能为多选数据
        print(request.query_params)    # --> request.GET  <QueryDict: {'a': ['1'], 'b': ['2', '3']}>
        # print(request.GET)
        # print(request.query_params.getlist('b'))
        students = models.Student.objects.all()
        serializer_obj = StudentModelSerializer(instance=students, many=True)

        # return Response(serializer_obj.data, status=400)
        return Response(serializer_obj.data)

    # 添加单条记录
    def post(self, request):
        serializer_obj = StudentModelSerializer(data=request.data)
        if serializer_obj.is_valid():
            new_obj = models.Student.objects.create(**serializer_obj.validated_data)
            obj = StudentModelSerializer(instance=new_obj)
            return Response(obj.data, status=status.HTTP_201_CREATED)


class StudentView(APIView):
    # 获取单条数据
    def get(self, request, pk):
        student = models.Student.objects.get(pk=pk)
        serializer_obj = StudentModelSerializer(instance=student)
        return Response(serializer_obj.data)

    # 更新单条记录
    def put(self, request, pk):
        student = models.Student.objects.get(pk=pk)
        data = request.data
        serializer_obj = StudentModelSerializer(instance=student, data=data, partial=True)
        if serializer_obj.is_valid():
            instance = serializer_obj.save()
            new_serializer_obj = StudentModelSerializer(instance=instance)
            return Response(new_serializer_obj.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': '校验失败'})

    # 删除单条记录
    def delete(self, request, pk):
        models.Student.objects.get(pk=pk).delete()
        # return Response(None, )
        return Response('', status=status.HTTP_204_NO_CONTENT)


################## 基于GenericAPIView的视图接口 ##################
from rest_framework.generics import GenericAPIView


class Students2View(GenericAPIView):
    queryset = models.Student.objects.all()    # 必须写这个参数,方法中使用的self.get_queryset()方法自动获取到queryset属性数据
    serializer_class = StudentModelSerializer   # 非必填属性,self.get_serializer获取到serializer_class制定的序列化器类

    # 当视图中使用多个序列化器类时,可以使用以下方法区分
    # def get_serializer_class(self):
    #     print(">>>>>>>")
    #     if self.request.method == "GET":
    #         return StudentModelSerializer2
    #     else:
    #         return StudentModelSerializer

    # 获取所有数据
    def get(self, request):
        # http://127.0.0.1:8000/req/students/?a=1&b=2&b=3  b可能为多选数据
        # print('get', self.get_serializer())
        print(request.query_params)  # -- request.GET  <QueryDict: {'a': ['1'], 'b': ['2', '3']}>
        # print(request.GET)
        # print(request.query_params.getlist('b'))
        students = self.get_queryset()
        serializer_obj = self.get_serializer(instance=students, many=True)
        # return Response(serializer_obj.data,status=400)
        return Response(serializer_obj.data)

    # 添加单条记录
    def post(self, request):
        # print('post', self.get_serializer())
        serializer_obj = self.get_serializer(data=request.data)
        if serializer_obj.is_valid():
            new_obj = models.Student.objects.create(**serializer_obj.validated_data)
            obj = self.get_serializer(instance=new_obj)
            return Response(obj.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer_obj.errors)
            return Response({'error': '校验失败'})


class Student2View(GenericAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentModelSerializer

    # 获取单条数据
    def get(self, request, pk):
        # student = models.Student.objects.get(pk=pk)
        # student = self.get_queryset().filter(pk=pk).first()
        student = self.get_object()
        serializer_obj = self.get_serializer(instance=student)
        return Response(serializer_obj.data)

    # 更新单条记录
    def put(self, request, pk):
        student = self.get_object()
        data = request.data
        serializer_obj = self.get_serializer(instance=student, data=data, partial=True)
        if serializer_obj.is_valid():
            instance = serializer_obj.save()
            new_serializer_obj = self.get_serializer(instance=instance)
            return Response(new_serializer_obj.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': "检验失败"})

    # 删除单条记录
    def delete(self, request, pk):
        self.get_object().delete()
        # return Response(None,)
        return Response('', status=status.HTTP_204_NO_CONTENT)


################## 基于视图扩展类来写视图接口 ##################
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class Students3View(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = StudentModelSerializer

    # 获取所有数据
    def get(self, request):
        return self.list(request)

    # 添加单条记录
    def post(self, request):
        return self.create(request)


class Student3View(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = StudentModelSerializer

    # 获取单条数据
    def get(self, request, pk):
        return self.retrieve(request, pk)

    # 更新单条记录
    def patch(self, request, pk):
        return self.update(request, pk)

    # 删除单条记录
    def delete(self, request, pk):
        return self.destroy(request, pk)


################## 基于视图子类来写视图接口 ##################
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


class Students4View(ListAPIView, CreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentModelSerializer


class Student4View(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentModelSerializer


################## 体验视图集基类 ##################
from rest_framework.viewsets import ViewSet


class AA(Exception):
    pass


class Students5View(ViewSet):
    # 获取所有数据
    def get_all_students(self, request):
        students = models.Student.objects.all()
        serializer_obj = StudentModelSerializer(instance=students)
        return Response(serializer_obj.data)

    # 获取单条数据
    def get_one_student(self, request, pk):
        student = models.Student.objects.get(pk=pk)
        serializer_obj = StudentModelSerializer(instance=student)
        return Response(serializer_obj.data)

    # 添加单条记录
    def post(self, request):
        serializer_obj = StudentModelSerializer(data=request.data)
        if serializer_obj.is_valid():
            new_obj = models.Student.objects.create(**serializer_obj.validated_data)
            obj = StudentModelSerializer(instance=new_obj)
            return Response(obj.data, status=status.HTTP_201_CREATED)

    # 更新单条记录
    def gengxin(self, request, pk):
        student = models.Student.objects.get(pk=pk)
        data = request.data
        serializer_obj = StudentModelSerializer(data=data)
        if serializer_obj.is_valid():
            instance = serializer_obj.save()
            new_serializer_obj = StudentModelSerializer(instance=instance)
            return Response(new_serializer_obj.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'error': "检验失败"})

    # 删除单条记录
    def shanchu(self, request, pk):
        models.Student.objects.get(pk=pk).delete()
        # return Response(None,)
        return Response('', status=status.HTTP_204_NO_CONTENT)


################## 基于视图集基类来写视图接口 ##################
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import ViewSet


class Students6View(ViewSet, GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = models.Student.objects.all()
    serializer_class = StudentModelSerializer


################## 基于视图集基类来写视图接口 ##################
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 3
    # 127.0.0.1:8001/students/?page=5
    page_query_param = 'p'    # 127.0.0.1:8001/students/?p=5
    page_size_query_param = 'size'    # 客户端通过这个关键字可以控制每页获取多少条数据
    max_page_size = 4    # 一页最多显示多少条


class StandrdLimitOffsetPagination(LimitOffsetPagination):
    # 默认每一页查询的数据量,类似上面的page_size
    default_limit = 2    # 每页显示2条数据
    limit_query_param = 'size'
    offset_query_param = 'start'
    # http://127.0.0.1:8000/req/students7/?limit=2&offset=2  #默认
    # http://127.0.0.1:8000/req/students7/?size=2&start=2


class Students7View(ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentModelSerializer

    # pagination_class = LargeResultsSetPagination
    pagination_class = StandrdLimitOffsetPagination

    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('id', 'age')
    # students/?ordering=-id
    filter_fields = ('name', 'age')
    # students/?age=18

    # @action(methods=['get', 'post'], detail=True)    # 处理单条数据
    @action(methods=['get', 'post'], detail=False)    # 处理多条数据
    def books(self, request):
        return Response({'xx':'oo'})