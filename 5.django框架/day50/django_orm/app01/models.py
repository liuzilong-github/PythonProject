from django.db import models

# Create your models here.


# 属性对应的字段,默认都是不能为空的,也就是加了not null约束
# Book生成的表名称为 应用名称_模型类名小写
class Book(models.Model):
    # 如果没有指定主键字段,默认orm会给这个表添加一个名称为id的主键自增字段
    # 如果指定了主键,那以指定的为准,那么orm就不在自动创建id字段了
    # nid = models.AutoField(reimary_key=True)	#int primary_key auto_increment
    title = models.CharField(max_length=32)     # varchar书籍名称
    # price = models.FloatField()
    price = models.DecimalField(max_digits=5, decimal_places=2)	  # 999.99最大价格
    pub_date = models.DateField()   # date出版日期
    publish = models.CharField(max_length=32)   # 出版社名称
    # xx = models.CharField(max_length=18, null=True, blank=True)	  # null=True,blank=True允许该字段数据为空
    # xx = models.CharField(max_length=18, default="xx")	# null=True,blank=True允许该字段数据为空

    def __str__(self):
        return self.title

# 删表和删字段都是注释相关类或者相关属性,在执行数据库同步指令


class UserInfo(models.Model):
    name = models.CharField(max_length=12)
    b1 = models.DateTimeField(auto_now=True)    # 自动添加修改时间(第一次,也是添加记录的创建时间)
    b2 = models.DateTimeField(auto_now_add=True)    # 自动添加创建记录的时间
