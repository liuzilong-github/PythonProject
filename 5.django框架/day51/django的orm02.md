

## 查询(十三个查询API接口)

```python
# exclude 排除
# 返回的结果为queryset类型数据,通过objects控制器可以调用,queryset类型数据也能调用
obj_list = models.Book.objects.exclude(id=2)
obj_list = obj_list.filter(title__contains="少年")
obj_list = obj_list.all()
obj_list = models.Book.objects.exclude(id=2).filter(title__contains='少年').exclude(id=5)

# order_by 排序
# 返回结果为queryset类型数据,queryset类型数据可以调用这个方法
# -id加一个"-"号表示按照该字段降序排列, desc
# 相当于: select * from app01_book order by id desc;
obj_list = models.Book.objects.all().order_by('-id')
# 按照价格升序排列,价格相同的按照id降序排列
obj_list = models.Book.objects.all().order_by('price', '-id')

# reverse 反转
# 反转必须在排序数据的基础上
# 返回的结果为queryset类型数据,queryset类型数据可以调用这个方法
obj_list = models.Book.objects.all().order_by('-id').reverse()

# count 计数
# queryset类型数据可以调用这个方法,返回的值为数字
obj_list = models.Book.objects.all().count()

# first/last 查询第一条/最后一条数据
# queryset类型数据可以调用这个方法,返回值为模型类对象
obj_list = models.Book.objects.all().first()
obj_list = models.Book.objects.all()[0]
obj_list = models.Book.objects.all().last()

# exists 判断查询结果是否有数据
# queryset类型数据可以调用这个方法
# 判断是否有数据的时候效率比较高,它只会找一条记录 limit 1
obj_list = models.Book.objects.all().exists()

# values 可以获取指定字段的数据
# objects可以调用,queryset类型数据也可以调用,返回结果还是queryset,内容为一个个字典数据
obj_list = models.Book.objects.values('title', 'price')
obj_list = models.Book.objects.filter(id=5).values('title', 'price')

# values_list 可以获取指定字段数据
# 返回的结果还是queryset,内容为一个个元组数据
obj_list = models.Book.objects.values_list('title', 'price')
obj_list = models.Book.objects.filter(id=5).values_list('title', 'price')

# distinct 去重
# 一般配合values和values_list来使用
obj_list = models.Book.objects.values('price').distinct()

print(obj_list)
```



## 多表操作

### 表关系设计

```python
from django.db import models

# Create your models here.

# 作者表
class Author(models.Model):
	name = models.CharField(max_length=32)
	age = models.IntegerField()

	# django2.x版本必须手动指定on_delete=models.CASCADE级联模式
	# au = models.OneToOneField(to='AuthorDetail', to_field='id', on_delete=models.CASCADE)
	# au = models.OneToOneField("AuthorDetail")
	# au = models.IntegerField()
	au = models.OneToOneField("AuthorDetail", db_constraint=False)
	# db_constraint=False 取消foreign key的强制约束效果,还可以继续使用orm提供的属性或者方法来操作关系记录
	# foreign key + unique

# 属性是OnetoOneField或者ForeignKey,那么生成的对应字段是属性名称_id

# 作者详细信息表
class AuthorDetail(models.Model):
	birthday = models.DateField()
	telephone = models.BigIntegerField()
	addr = models.CharField(max_length=64)

# 出版社表
class Publish(models.Model):
	name = models.CharField(max_length=32)
	city = models.CharField(max_length=32)

# 书籍表
class Book(models.Model):
	title = models.CharField(max_length=32)
	publishDate = models.DateField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	# publishs=models.ForeignKey(to="Publish", to_field="id", on_delete=models.CASCADE)
	publishs = models.ForeignKey("Publish")
	authors = models.ManyToManyField("Author")

# models.ManyToManyField("Author")相当于如下代码
# 
# class authortobook(models.Model):
# 	book_id = models.ForeignKey('Book')
# 	author_id = models.ForeignKey('Author')
```


### 记录的增删改查操作

#### 增加

```python
# 一对一关系的添加
# 先创建作者详细信息表记录
ret = models.AuthorDetail.objects.create(
	birthday='2000-12-12',
	telephone='122',
	addr='惠州'
)

models.Author.objects.create(
	name='元涛',
	age=18,
	# 如果用的是属性名称_id,那么值为关联记录的id值
	# au_id=ret.id,
	# 如果写属性名称来添加关系数据,那么值为关联记录的模型类对象
	au=ret
)


# 一对多关系的添加
pub_obj = models.Publish.objects.get(id=1)

models.Book.objects.create(
	title='baijie',
	price=10,
	publishDate='1980-07-07',
	# 如果写属性名称来添加关系数据,那么值为关联记录的模型类对象
	# publishs=pub_obj,
	# 如果用的是属性名称_id,那么值为关联记录的id值
	publishs_id=pub_obj.id
)


# 多对多关系的添加
book_obj = models.Book.objects.get(title='金鳞岂是池中物')
author1 = models.Author.objects.get(id=1)
author2 = models.Author.objects.get(id=2)

book_obj.authors.add(author1, author2)
# book_obj.authors.add(1, 2)
# book_obj.authors.add(*[1, 2])
```






















