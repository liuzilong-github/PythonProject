from django.shortcuts import render, HttpResponse
from app01 import models

# Create your views here.


def query(request):
    ### 删除 外键关联到这条作者记录的都会被删除(级联模式下)
    # 一对一
    # models.Author.objects.get(id=1).delete()
    # models.AuthorDetail.objects.get(id=2).delete()

    # # 一对多
    # models.Book.objects.get(id=1).delete()
    # models.Publish.objects.get(id=2).delete()

    # # 多对多
    # book_obj = models.Book.objects.get(id=6)
    # book_obj = models.Book.objects.filter(id=5)[0]
    # book_obj.authors.remove(1)  # 删除第三张表中id为5的并且作者id为1的记录
    # book_obj.authors.clear()    # 清空第三张表中id为5的所有记录
    # book_obj.authors.remove(1, 4)   # 删除多条
    # book_obj.authors.remove(*[1, 4])    # 删除多条


    ### 修改
    # 一对一
    # models.Author.objects.filter(id=3).update(
    #     age=38,
    #     # au_id=models.AuthorDetail.objects.get(id=5).id
    #     au=models.AuthorDetail.objects.get(id=5)
    # )
    #
    # # 一对多
    # models.Book.objects.filter(id=4).update(
    #     title='baijie',
    #     # publishs=models.Publish.objects.get(id=2),
    #     publishs_id=models.Publish.objects.get(id=2).id
    # )
    #
    # # 多对多
    # obj = models.Book.objects.get(id=5)
    # obj.authors.set(['1', '3'])    # clear + add 更新,先清空book_id为5的第三张表里的记录,再添加5 1和5 3


    ### 基于对象的跨表查询
    # 一对一
    # 正向查询(关系属性在哪个表里,通过这张表的数据去查另外一张表的数据,就是正向查询)
    # 正向查询靠属性,反向查询靠表名小写

    # 查询一下闻哥这个作者的手机号
    obj = models.Author.objects.get(name='子龙')
    # obj.au    这就找到了关联的详细信息表里面的那个记录对象
    print(obj.au.telephone)

    # 查询手机号是18518753334的作者姓名
    obj = models.AuthorDetail.objects.get(telephone='18518753334')
    # obj.author    这就找到了关联的作者表里面的那个记录对象
    print(obj.author.name)

    # 一对多
    # 正向查询
    # 查询白洁1这个本书是哪个出版社出版的
    obj = models.Book.objects.get(title='白洁1')
    # obj.publishs    找到了关联的出版社记录
    print(obj.publishs.name)

    # 查询闻哥出版社出版了哪些书
    # 反向查询 反向查询在一对多的关系时,使用 表名_set
    obj = models.Publish.objects.get(name='闻哥出版社')
    obj.book_set.filter()   # 类似于objects控制器
    books = obj.book_set.all()
    for book in books:
        print(book.title)

    # 多对多
    # 查询一下白洁1这本书的作者是谁
    # 正向查询
    obj = models.Book.objects.filter(title='白洁1').first()
    # obj.authors.all()   类型与objects控制器
    objs = obj.authors.all()
    for obj in objs:
        print(obj.name)

    # 查询一下子龙写了哪些书
    # 反向查询
    obj = models.Author.objects.get(name='子龙')
    objs = obj.book_set.all()
    for obj in objs:
        print(obj.title)


    ### 基于双下划线的跨表查询 -- mysql的连表查询
    # select app01_authordetail.telephone from app01_author inner join app01_authordetail on app01_author.au_id = app01_authordetail.id;
    # select app01_authordetail.telephone from app01_authordetail inner join app01_author on app01_authordetail.id = app01_author.au_id

    # 正向查询靠属性,反向查询靠表名小写

    # 一对一
    # 查询一下子龙这个作者的手机号
    ret = models.Author.objects.filter(name='子龙').values('au__telephone')
    # < QuerySet[{'au__telephone': '222'}] >
    # 反向查询
    ret = models.AuthorDetail.objects.filter(author__name='子龙').values('telephone')
    print(ret)  # <QuerySet [{'telephone': '222'}]>

    # 一对多
    # 查询白洁1这本书是哪个出版社出版的
    ret = models.Book.objects.filter(title='白洁1').values('publishs__name')
    # < QuerySet[{'publishs__name': '闻哥出版社'}] >
    ret = models.Publish.objects.filter(book__title='白洁1').values('name')
    print(ret)  # <QuerySet [{'name': '何导'}, {'name': '闻哥'}]>

    # 多对多
    # 查询一下白洁1这本书的作者是谁
    ret = models.Book.objects.filter(title='白洁1').values('authors__name')
    print(ret)  # <QuerySet [{'authors__name': '闻哥'}, {'authors__name': '何导'}]>
    ret = models.Author.objects.filter(book__title='白洁1').values('name')
    print(ret)  # <QuerySet [{'name': '何导'}, {'name': '闻哥'}]>


    ### 聚合查询
    from django.db.models import Avg, Max, Min, Sum, Count

    # 查询所有书籍的平均价格
    ret = models.Book.objects.all().aggregate(Avg('price'))
    ret = models.Book.objects.aggregate(Max('price'), Avg('price'))
    # {'price__max': Decimal('19.00')}    字典类型数据
    ret = models.Book.objects.aggregate(m=Max('price'), a=Avg('price'))
    print(ret)

    ### 分组查询 -- group by
    # 查询一下每个出版社出版书的平均价格
    # 默认是用Publish的id字段作为分组依据,自动会找Book表里面的publishs_id去分组
    ret = models.Publish.objects.annotate(a=Avg('book__price')).values('a', 'name', 'city')
    # select t1.name,t1.city,avg(t2.price) from app01_publish as t1 inner join app01_book as t2 on t1.id = t2.publishs_id group by t1.id;
    print(ret)  # <QuerySet [{'name': '32期桔色成人出版社', 'city': '沙河', 'a': 12.5}, {'name': '闻哥出版社', 'city': '松兰堡', 'a': 14.0}, {'name': '牡丹花出版社', 'city': '洛阳', 'a': 13.75}]>

    ret = models.Book.objects.values('publishs_id').annotate(a=Avg('price'))
    # select avg(price) from book group by publishs_id
    print(ret)

    # 查询每个作者出版书的最高价格
    ret = models.Author.objects.annotate(m=Max('book__price')).values('name', 'm')
    print(ret)  # <QuerySet [{'name': '苑昊', 'm': None}, {'name': '何导', 'm': Decimal('17.00')}, {'name': '闻哥', 'm': Decimal('19.00')}]>

    ret = models.Book.objects.values('authors__id').annotate(m=Max('price'))
    print(ret)  # <QuerySet [{'authors__id': '苑昊', 'm': 123}
    # 注意:一定要起别名,结果为publish模型类对象,对象中有本表疑点数据


    ### 作业
    # 1 查询每个作者的姓名以及出版的书的最高价格
    ret = models.Author.objects.annotate(m=Max('book__price')).values('name', 'm')
    print(ret)
    # 2 查询作者id大于2作者的姓名以及出版的书的最高价格
    ret = models.Author.objects.filter(id__gt=2).annotate(m=Max('book_price')).values('name', 'm')
    # 3 查询作者id大于2或者作者年龄大于等于20岁的女作者的姓名以及出版的书的最高价格

    # 4 查询每个作者出版的书的最高价格 的平均值
    ret = models.Author.objects.annotate(m=Max('book__price')).values('name', 'm').aggregate(a=Avg('m'))



    return HttpResponse('ok')