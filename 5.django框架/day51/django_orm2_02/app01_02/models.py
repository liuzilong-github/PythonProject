from django.db import models

# Create your models here.


# 作者表
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # django2.x版本必须手动指定on_delete=models.CASCADE级联模式
    # au = models.OneToOneField(to='AuthorDetail', to_field='id', on_delete=models.CASCADE)
    # au = models.OneToOneField('AuthorDetail')
    # au = models.IntegerField()
    au = models.OneToOneField('AuthorDetail', db_constraint=False)
    # db_constraint=False 取消foreign key的强制约束效果,还可以继续使用orm提供的属性或者方法来操作关系记录
    # foreign key + unique

# 属性是OneToOneField或者是ForeignKey,那么生成的对应字段是 属性名_id


# 作者详细信息表
class AuthorDetail(models.Model):
    birthday = models.DateField()
    # telephone = models.BigIntegerField()
    telephone = models.CharField(max_length=32)
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
    # publishs = models.ForeignKey(to='Publish', to_field='id', on_delete=models.CASCADE)
    publishs = models.ForeignKey('Publish')
    authors = models.ManyToManyField('Author')
