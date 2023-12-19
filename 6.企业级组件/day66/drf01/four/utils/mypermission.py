
from rest_framework.permissions import BasePermission


class VIPpermission(BasePermission):
    def has_permission(self, request, view):
        print('看看有没有权限')
        # request.user.role == 'vip'
        return True
        # return False