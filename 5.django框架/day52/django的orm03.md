

# ORM


## 多表操作

### 删除

```python
# 删除 外检关联到这条作者记录的都会被删除(级联模式下)

# 一对一
models.Author.objects.get(id=1).delete()
models.AuthorDetail.objects.get(id=2).delete()

# 一对多
models.Book.objects.get(id=1).delete()
models.Publish.objects.get(id=2).delete()

# 多对多
# book_obj = models.Book.objects.get(id=6)
book_obj = models.Book.objects.filter(id=5)[0]
book_obj.authos.remove(1)	# 删除第三章表中书籍id=5,并且作者id=1的记录
book.obj.authors.clear()	# 清空第三张表中书籍为5的所有记录
book_obj.authors.remove(1, 4)	# 删除多条
book_obj.authors.remove(*[1, 4])	# 删除多条

```

### 修改

```python
# 一对一
models.Author.objects.filter(id=3).update(
	age=38,
	# au_id=models.AuthorDetail.objects.get(id=5).id,
	au=models.AuthorDetail.objects.get(id=5),
)

# 一对多
models.Book.objects.filter(id=4).update(
	title='baijie1',
	# publishs=models.Publish.objects.get(id=2),
	publishs_id=models.Publish.objects.get(id=2).id,
)

# 多对多
obj = models.Book.objects.get(id=5)
obj.authors.set(['1', '3'])		# clear + add更新,先清空book_id为5的第三张表里的记录,再添加5 1和5 3两条记录
```


### 查询

#### 基于对象的跨表查询

```python
# 一对一
# 正向查询(关系属性在哪个表里面,通过这个表的数据去查询另外一张表的数据,就是正向查询)
# 正向查询靠属性,反向查询靠表名小写
# 查询闻哥这个作者的手机号
obj = models.Author.objects.get(name='闻哥')
# obj.au  这就找到了关联的详细信息表里那个记录对象
print(obj.au.telephone)

# 查询手机号为555的作者姓名
obj = models.AuthorDetail.objects.get(telephone='555')
# obj.author 这就找到了关联的作者表里面的那个记录对象
print(obj.author.name)

# 一对多
# 正向查询, 查询baijie1这本书是哪个出版社出版的
obj = models.Book.objects.get(title='baijie1')
# obj.publishs	找到了关联的出版社记录
print(obj.publishs.name)

# 反向查询, 查询闻哥出版社出版了哪些书
# 反向查询在一对多的关系时,使用 表名小写_set
obj = models.Publish.objects.get(name='闻哥出版社')
# obj.book_set.filter()	 类似于objects控制器
books = obj.book_set.all()
for book in books:
	print(book.title)

# 多对多
# 正向查询, 查询一下baijie2这本书的作者是谁
obj = models.Book.objects.filter(title='baijie2').first()
# obj.authors.all()	类似objects控制器
objs = obj.authors.all()
for i in objs:
	print(i.name)

# 反向查询, 查询一下何导写了那些书
obj = models.Author.objects.get(name='何导')
objs = obj.book_set.all()
for i in objs:
	print(i.title)
```

#### 基于双下划线的跨表查询

```python
# 基于双下划线的夸表查询 -- 等同于mysql的连表查询

# select app01_authordetail.telephone from app01_author inner join app01_authordetail on app01_author.au_id = app01_authordetail.id;
# select app01_authordetails.telephone from app01_authordetail inner join app01_author on app01_author.au_id = app01_authordetail.id;

# 正向查询靠属性,反向查询靠表名小写

# 一对一
# 查询一下闻哥这个作者的手机号
# 正向查询
ret = models.Author.objects.filter(name='闻哥').values('au__telephone')
print(ret)	# <QuerySet [{'au__telephone': '222'}]>
# 反向查询
ret = models.AuthorDetail.objects.filter(author__name='闻哥').value('telephone')
print(ret)	# <QuerySet [{'telephone': '222'}]>

# 一对多
# 查询baijie1这本书是哪个出版社出版的
ret = models.Book.objects.filter(title='baijie1').values('publishs__name')
print(ret)	# <QuerySet [{'publishs__name': '闻哥出版社'}]>

ret = models.Publishs.objects.filter(book__title='baijie1').values('name')
print(ret)	# <QuerySet [{'name': '闻哥出版社'}]>

# 多对多
# 查询一下baijie2这本书的作者是谁
ret = models.Book.objects.filter(title='baijie2').values('authors__name')
print(ret)	# <QuerySet [{'authors__name': '闻哥'}, {'authors__name': '何导'}]>

ret = models.Author.objects.filter(boo__title='baijie2').values('name')
print(ret)	# <QuerySet [{'name': '何导'}, {'name': '闻哥'}]>
```


### 聚合查询

```python
# 查询所有书籍的平均价格
ret = models.Book.objects.all().aggregate(Avg('price'))

ret = models.Book.objects.aggregate(MAx('price'), Avg('price'))
# {'price__max': Decimal('19.00')} 字典类型数据
ret = models.Book.objects.aggregate(m=Max('price'), a=Avg('price'))
print(ret)
```


### 分组

```python
# 查询每个出版社出版书的平均价格
models.Publish.objects.annotate(a=Avg('book__price')).values('a')
models.Book.objects.values('Publishs_id').annotate(a=Avg('price'))

# 查询每个作者出版署的平均价格
models.Author.objects.annotate(a=Avg('book__price')).values('a')
models.Book.objects.values('authors__id').annotate(a=Avg('price'))

```



















