
from rest_framework.serializers import ModelSerializer
from app01 import models


class StudentSerializer(ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'