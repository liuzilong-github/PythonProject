from django.db import models

# Create your models here.


# 作者表
class Author(models.Model):
    name = models.CharField( max_length=32)
    age = models.IntegerField()

    # sex_choice = (
    #     (0, '女性'),
    #     (1, '男性')
    # )
    # sex = models.IntegerField(choices=sex_choice,default=0)
    # django2.x版本必须手动指定on_delete=models.CASCADE级联模式
    # au = models.OneToOneField(to="AuthorDetail", to_field="id", on_delete=models.CASCADE)
    # au = models.OneToOneField("AuthorDetail")
    # au = models.IntegerField()
    au = models.OneToOneField("AuthorDetail")
    # db_constraint=False取消foreign key的强制约束效果,还可以继续使用orm的提供的属性或者方法来操作关系记录
    # foreign key + unique

# 属性是OneToOneField或者ForeignKey,那么生成的对应字段是  属性名称_id


# 作者详细信息表
class AuthorDetail(models.Model):
    birthday = models.DateField()
    # telephone=models.BigIntegerField()
    telephone = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)


# 出版社表
class Publish(models.Model):
    name = models.CharField( max_length=32)
    city = models.CharField( max_length=32)


# 书籍表
class Book(models.Model):
    title = models.CharField( max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    # publishs = models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE)
    publishs = models.ForeignKey("Publish")
    authors = models.ManyToManyField('Author')

    dianzan = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)

    def get_author_name(self):
        author_name = [i.name for i in self.authors.all()]
        if author_name == []:
            return '-'
        else:
            return ','.join(author_name)


class Menu(models.Model):
    title = models.CharField(max_length=10)
    url = models.CharField(max_length=20)
    icon = models.CharField(max_length=32)


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()

    menus = models.ManyToManyField('Menu')






