from django.shortcuts import render, HttpResponse
from app01 import models
import datetime

# Create your views here.


def query(request):
    # 添加数据 方式1
    new_book = models.Book(
        # id=2,
        title='金瓶梅',
        price=9.9,
        # pub_date=datetime.datetime.now(),  # 添加时间类型数据时,可以是时间日期类型的数据,也可以是字符串数据
        pub_date='2022-02-02',
        publish='32期红浪漫出版社'
        # 有默认值的字段,可以为空的字段,主键字段,都可以不用传值
    )
    new_book.save()

    # 添加数据 方式2 create方法添加,create方法的返回值为 新添加的数据的模型类对象
    new_book = models.Book.objects.create(
        title='金瓶梅4',
        price=19.9,
        # pub_date=datetime.datetime.now(),
        pub_date='2022-04-02',
        publish='32期红浪漫出版社'
    )
    print(new_book.title)   # 通过模型类对象,直接获取属性对应的值
    print(new_book.price)

    # 批量添加 bulk_create
    obj_list = []
    for i in range(10):
        book_obj = models.Book(
            title=f'少年阿宾{i}',
            price=10 + i,
            pub_date=f'2022-04-1{i}',
            publish='32期红浪漫出版社'
        )
        obj_list.append(book_obj)
    models.Book.objects.bulk_create(obj_list)

    # 查看所有数据
    book_objs = models.Book.objects.all()   # queryset类型数据,类似于列表
    book_objs = models.Book.objects.filter(id=3)    # <QuerySet [<Book: 金瓶梅3>]>
    book_objs = models.Book.objects.get(id=3)   # 模型类对象

    # print(book_objs)    # 金瓶梅
    # print(book_objs[0], type(book_objs[0]))     # 模型类对象
    # print(book_objs[0].title)

    book_objs = models.Book.objects.filter()    # filter没有加条件,和all的效果一样
    book_objs = models.Book.objects.filter(id=100)  # 查不到数据,不会报错,返回空的queryset类型数据
    # book_objs = models.Book.objects.get()   # 也是查所有,但是get方法的查询结果有要求,有且只能有一条,如果结果为多条,会报错
    # book_objs = models.Book.objects.get(id=100)     # 查询不到结果会报错 Book matching query does not exist.

    # 删除数据
    models.Book.objects.filter(id=3).delete()   # queryset类型数据可以调用delete方法删除查询数据
    models.Book.objects.get(id=4).delete()  # 模型类对象也可以调用delete方法删除查询数据

    # 修改数据 方式1
    models.Book.objects.filter(id=5).update(
        price=20,
        title='xxx'
    )

    # 修改数据 方式2
    # 模型类对象不能调用update方法
    # models.Book.objects.get(id=5).update(
    #     price=100
    # )
    ret = models.Book.objects.get(id=5)
    ret.price = 30
    ret.title = '少年阿宾00'
    ret.save()

    # 测试aotu_now和auto_now_add两个参数
    models.UserInfo.objects.create(
        name='xx3'
    )
    # update不能触发自动更新时间的auto_now参数的作用,如果用update来更新记录,并保存更新记录的时间,需要手动给该字段传入当前时间
    models.UserInfo.objects.filter(id=1).update(
        name='xxoo',
        b1=datetime.datetime.now()
    )
    # 通过调用save方法来触发auto_now参数自动更新修改时间的动作
    ret = models.UserInfo.objects.get(id=1)
    ret.name = 'xxoo2'
    ret.save()

    obj_list = models.Book.objects.filter(title__startswith='少年')   # 以什么开头
    obj_list = models.Book.objects.filter(title__endswith='梅')  # 以什么结尾
    obj_list = models.Book.objects.filter(title__startswith='p')    # 区分大小写
    obj_list = models.Book.objects.filter(title__istartswith='p')   # 不区分大小写
    obj_list = models.Book.objects.filter(title__contains='th')     # 包含
    obj_list = models.Book.objects.filter(title__icontains='th')    # 包含,不区分大小写

    obj_list = models.Book.objects.filter(price__gt=15)     # 大于
    obj_list = models.Book.objects.filter(price__gte=15)    # 大于等于
    obj_list = models.Book.objects.filter(price__lt=15)     # 小于
    obj_list = models.Book.objects.filter(price__lte=15)    # 小于等于

    # obj_list = models.Book.objects.filter(price=15 or price=18 or price=30)   # 不支持的写法
    obj_list = models.Book.objects.filter(price__in=[13,15,30])     # 价格等于15或者等于18或者等于30的书籍
    obj_list = models.Book.objects.filter(price__range=[15,20])     # 价格大于等于15并且小于等于20, between and

    obj_list = models.Book.objects.filter(id=10, price=15)  # 逗号连接的查询条件就是and的关系
    obj_list = models.Book.objects.filter(pub_date__year='2020')    # 2020年的书籍
    obj_list = models.Book.objects.filter(pub_date__year='2020', pub_date__month='11')  # 2020年11月份的书籍
    obj_list = models.Book.objects.filter(pub_date__year='2020', pub_date__month='11', pub_date__day='25')  # 2020年11月25号的书籍
    obj_list = models.Book.objects.filter(pub_date='2020-11-25')    # 2020年11月25号的书籍

    print(obj_list)

    return HttpResponse('ok')
