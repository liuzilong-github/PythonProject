
from rest_framework import serializers
from ser import models

'''
class Student(models.Model):
    # 模型字段
    id = AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name="姓名", help_text='提示文本：不能为空')
    sex = models.BooleanField(default=1,verbose_name="性别")  #1:男
    age = models.IntegerField(verbose_name="年龄")
    class_null = models.CharField(max_length=5,verbose_name="班级编号")
    description = models.TextField(max_length=1000,verbose_name="个性签名")
'''

# all = models.Student.objects.all()  # queryset[模型类对象1、模型类对象2.。。。]
# StudentSerializer(all)   # 模型类对象1--id和name字段都去取出来  -- [{'id':1,'name':'chao'},{'id':2,'name':'chao2'}...]


# class StudentSerializer(serializers.Serializer):
#     """序列化对应字段数据时,需要在序列化器类中声明和模型类中对应字段相同名称的属性字段"""
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     sex = serializers.BooleanField()
#     age = serializers.IntegerField()
#     class_null = serializers.CharField()
#     description = serializers.CharField()
#
#
# # StudentSerializer2(request.POST).is_valid()    # {'name':'chao'，'sex':1, 'age':18, 'class_null':32, 'description':'xxx','sss':'xxx'}
# class StudentSerializer2(serializers.Serializer):
#     """序列化对应字段数据时,需要在序列化器类中声明和模型类中对应字段相同名称的属性字段"""
#     name = serializers.CharField(max_length=8, error_messages={'max_length': '太长了,受不了', 'required': '也不能没有哦'})
#     sex = serializers.BooleanField()    # 默认约束required=True,这个数据要求必须要有
#     age = serializers.IntegerField(max_value=10)
#     # class_null = serializers.CharField(allow_blank=True, allow_null=True)
#     class_null = serializers.CharField(required=False, default="222")
#     description = serializers.CharField()
#     # sss = serializers.CharField(max_length=32)


# class StudentSerializer3(serializers.Serializer):
#     '''序列化对应字段数据时，需要在序列化器类中声明和模型类中对应字段相同名称的属性字段'''
#     id = serializers.IntegerField(read_only=True)    # 序列化阶段需要,反序列化阶段不需要验证
#     name = serializers.CharField(max_length=8, error_messages={'max_length': '太长了,受不了', 'required': '也不能没有哦'})
#     sex = serializers.BooleanField()
#     age = serializers.IntegerField(max_value=18)
#     class_null = serializers.CharField(required=False)
#     description = serializers.CharField(write_only=True)    # 该字段数据序列化阶段不会被提取出来,反序列化时,必须要传过来进行校验
#     共同点: write_only=True  required=True (要求提取的数据必须包含该字段数据)
#     不同点: write_only=True 该字段数据序列化阶段不会被提取出来,反序列化时,必须要传过来进行校验,required=True 该字段数据序列化阶段也会被提取出来


import re

def check_name(val):
    if not re.match('a', val):   # val: xxllaa
        raise serializers.ValidationError('不是以a开头的,不行')
    return val


class StudentSerializer3(serializers.Serializer):
    '''序列化对应字段数据时，需要在序列化器类中声明和模型类中对应字段相同名称的属性字段'''
    id = serializers.IntegerField(read_only=True)    # 序列化阶段需要,反序列化阶段不需要验证
    name = serializers.CharField(validators=[check_name,])
    sex = serializers.BooleanField()
    age = serializers.IntegerField(max_value=18)
    class_null = serializers.CharField(required=False)
    # p1 = serializers.CharField()
    # p2 = serializers.CharField()
    description = serializers.CharField(write_only=True)

    # 局部钩子(参数校验完成之后,只要定义了局部钩子,那么局部钩子就会自动调用执行)
    # def validate_属性名(self, data):   data参数就是该属性对应的数据

    def validate_name(self, data):
        if '666' in data:
            raise serializers.ValidationError('光喊6不行')
        return data    # 校验成功之后,一定要返回该字段数据,不然validated_data属性是没有该值的

    def validate_age(self, data):
        return data

    # 反序列化时的校验顺序: 字段1的参数校验,字段1的局部钩子,字段2的参数校验,字段2的局部钩子...最后执行全局钩子

    # 全局钩子
    def validate(self, data):   # data时有序字典,并且是经过所有校验之后的结果数据
        print('额外参数>>>>', self.context.get('request').path)
        print('data', data)
        p1 = data.get('p1')
        p2 = data.get('p2')
        if p1 != p2:
            raise serializers.ValidationError('两次密码输入不一致,你怕不是傻子吧')
        return data

    def create(self, validated_data):
        # validated_data 校验成功之后的数据
        print('create>>>', validated_data)
        new_obj = models.Student.objects.create(**validated_data)
        return new_obj

    def update(self, instance, validated_data):
        # instance 老的模型类对象
        print('update>>>', instance)
        print(validated_data)
        '''
        update Student object (1)
        {'name': 'axxoo2'}
        '''
        instance.name = validated_data.get('name')
        instance.save()
        return instance