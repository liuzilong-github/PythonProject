from django.shortcuts import render
from rest_framework.views import APIView
from ser import models
from mser.serializers import StudentModelSerializer
from django.http import JsonResponse

# Create your views here.


class StudentsView(APIView):

    def get(self, request):
        all_students = models.Student.objects.all()
        serializer_obj = StudentModelSerializer(instance=all_students, many=True)
        return JsonResponse(serializer_obj.data, safe=False)

    def post(self, request):
        serializer_obj = StudentModelSerializer(data=request.data)
        print(serializer_obj.is_valid())
        if serializer_obj.is_valid():
            print('>>>>>>>', serializer_obj.validated_data)
            # >>>>>>> OrderedDict([('name', '龙哥622'), ('age', 18), ('password', '66666'), ('class_null', '32'), ('sex', True), ('description', '硬气')])
            del serializer_obj.validated_data['password']    # 这样删除不行
            # serializer_obj.validated_data
            obj = serializer_obj.save()    # meta -- User(username, password) 自动删除不必要的字段
            new_obj = StudentModelSerializer(instance=obj)
            return JsonResponse(new_obj.data)
        else:
            print(serializer_obj.errors)
            return JsonResponse({'error': '校验失败'})
