from django.shortcuts import render,HttpResponse
from app01_02 import models

# Create your views here.


def query(request):
    # 添加数据

    # 一对一关系的添加
    # 先创建作者详细信息表记录
    ret = models.AuthorDetail.objects.create(
        birthday='2000-12-12',
        telephone='122',
        addr='惠州',
    )

    models.Author.objects.create(
        name='元涛',
        age=18,
        # 如果用的是属性名称_id,那么值为关联记录的id值
        # au_id=ret.id,
        # 如果用属性名称来添加关系数据,那么值为关联记录的模型类对象
        au=ret,
    )

    # 一对多关系的添加
    pub_obj = models.Publish.objects.get(id=1)

    models.Book.objects.create(
        title='baijie2',
        price=9.9,
        publishDate='1980-07-07',
        # 如果写属性名称来添加数据,那么值为关联记录的模型类对象
        publishs=pub_obj,
        # 如果用的是属性名称_id,那么值为关联记录的id值
        publishs_id=pub_obj.id,
    )

    # 多对多关系的添加
    book_obj = models.Book.objects.get.filter(title='金鳞岂是池中物')
    author1 = models.Author.objects.get(id=1)
    author2 = models.Author.objects.get(id=2)

    book_obj.authors.add(author1, author2)
    # book_obj.authors.add(1, 2)
    # book_obj.authors.add(*[1, 2])

    return HttpResponse('ok')
