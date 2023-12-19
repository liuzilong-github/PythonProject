
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ser import models
from rest_framework.views import APIView
from rest_framework.response import Response
from four.utils.authrenzheng import Auth
from four.utils.mypermission import VIPpermission

# Create your views here.


class StudentView(APIView):
    """这是xx视图"""
    # authentication_classes = [Auth, ]
    # permission_classes = [VIPpermission, ]
    # throttle_classes = [UserRateThrottle,]
    def get(self, request):
        """

        :param request: 请求对象
        :return:笑嘻嘻
        """
        # print(request.user)    # zhaozhi
        # print(request.auth)    # xx
        return Response({'msg': 'ok'})
