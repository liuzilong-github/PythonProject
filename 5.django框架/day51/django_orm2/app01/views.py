from django.shortcuts import render,HttpResponse
from app01 import models

# Create your views here.


def query(request):
    # exclude 排除
    # 返回的结果为queryset类型数据,通过objects控制器可以调用,queryset类型数据也能调用
    obj_list = models.Book.objects.exclude(id=2)
    obj_list = obj_list.filter(title__contains='少年')
    obj_list = obj_list.all()
    obj_list = models.Book.objects.exclude(id=2).filter(title__contains='少年').exclude(id=5)

    # order_by 排序
    # 返回的结果为queryset类型数据,queryset类型数据可以调用该方法
    obj_list = models.Book.objects.all().order_by('-id')    # -id: id加一个-号表示按照该字段降序排列,相当于desc
    # 相当于: select * from app01_book order_by id desc;
    obj_list = models.Book.objects.order_by('price', '-id')  # 先按照价格升序排列,价格相同的按照id降序排列

    # reverse 翻转,必须在排序数据的基础上
    # 返回的结果为queryset类型数据,queryset类型数据可以调用这个方法
    obj_list = models.Book.objects.all().order_by('-id').reverse()

    # count 计数
    # queryset类型数据可以调用此方法,返回值为数字
    obj_list = models.Book.objects.all().count()

    # first/last 第一个数据/最后一个数据
    # queryset类型数据可以调用此方法,返回值为模型类对象
    obj_list = models.Book.objects.all().first()
    obj_list = models.Book.objects.all()[0]
    obj_list = models.Book.objects.all().last()

    # exists 判断查询结果是否有数据
    # queryset类型数据可以调用此方法,返回值为Bool类型
    obj_list = models.Book.objects.all().exists()   # 判断是否有数据效率比较高,只查一条数据,相当于limit 1

    # values 获取指定字段数据
    # objects可以调用此方法,queryset类型数据也可以调用此方法,返回结果还是queryset,内容为一个个字典数据
    obj_list = models.Book.objects.values('title', 'price')
    obj_list = models.Book.objects.filter(id=5).values('title', 'price')

    # values_list 获取指定字段数据
    # 返回结果还是queryset,内容为一个个元组数据
    obj_list = models.Book.objects.values_list('title', 'price')
    obj_list = models.Book.objects.filter(id=5).values_list('title', 'price')

    # distinct 去重,一般配合values和values_list使用
    obj_list = models.Book.objects.values('price').distinct()

    print(obj_list)

    return HttpResponse('ok')
