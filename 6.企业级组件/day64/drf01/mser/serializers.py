
from rest_framework import serializers
from ser import models


class StudentModelSerializer(serializers.ModelSerializer):
    # serializers.CharField(validators=)
    # r_password = serializer.CharField()
    password = serializers.CharField(max_length=5)

    class Meta:
        model = models.Student
        # fields = "__all__"
        fields = ['name', 'age', 'password', 'class_null', 'sex', 'description']
        # exclude = ['name', 'age']   # 排除某些字段,注意不能和fields属性同时使用
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {
                'max_length': 5,
                # 定制错误信息
                'error_message': {
                    'max_length': '太长了'
                },
                # 自定义校验函数
                # 'validators':[]
            },
        }

    # 局部钩子
    def validate_name(self, data):
        if '666' in data:
            raise serializers.ValidationError('不能光喊6')
        return data

    # 全局钩子
    def validate(self, data):
        return data

    '''
    id = ..
    name = models.CharField(max_length=100,verbose_name="姓名", help_text='提示文本：不能为空')
    sex = models.BooleanField(default=1,verbose_name="性别")  #1:男
    age = models.IntegerField(verbose_name="年龄")
    class_null = models.CharField(max_length=5,verbose_name="班级编号")
    description = models.TextField(max_length=1000,verbose_name="个性签名")
    '''