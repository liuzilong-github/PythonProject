
from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


class Auth(BaseAuthentication):
    def authenticate(self, request):
        # request.session.get('username') = 'chao'
        # 通过条件判断登录状态,登录成功了,那么返回用户信息,失败了可以报错
        if 1 == 1:
            return 'zhaozhi', 'xx'    # request.user = zhaozhi  request.auth = xx
        else:
            raise AuthenticationFailed('认证失败')
