
from rest_framework import serializers
from ser import models


class StudentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = "__all__"
        extra_kwargs = {
            "id": {'read_only': True},
        }


class StudentModelSerializer2(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = ['name', 'age']