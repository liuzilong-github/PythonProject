
from django.shortcuts import render, redirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin

# 登录认证中间件
# class LoginAuth(MiddlewareMixin):
# 	# 白名单
# 	white_list = ['/login/', '/register/']
#
# 	# 对请求处理用process_request, 如果请求通过了处理,就return None,如果没有通过就return HttpResponse对象
# 	def process_request(self, request):
# 		current_path = request.path
# 		if current_path not in self.white_list:
# 			status = request.session.get('is_login')
# 			if not status:
# 				return redirect('login')
# 		print('请求他来了')


class Md1(MiddlewareMixin):

	def process_request(self, request):
		print('Md1-process_request')
		# return HttpResponse('xxx')
		print(request.META['REMOTE_ADDR'])      # 127.0.0.1

	def process_view(self, request, view_func, view_args, view_kwargs):
		print('Md1-process_view')
		print(view_func, view_args, view_kwargs)
		# return HttpResponse('not ok')
		# < function login at 0x7fec55683d30 > () {}

	def process_response(self, request, response):
		print('Md1-process_response')
		return response

	def process_exception(self, request, exception):
		print(exception, type(exception))
		print('Md1-process_exception')
		# xxxxxxxxxxx <class 'ValueError'>
		# 统一做异常处理
		if isinstance(exception, ValueError):
			return HttpResponse('视图函数报错了', status=500)


class Md2(MiddlewareMixin):

	def process_request(self, request):
		print('Md2-process_request')

	def process_view(self, reuqest, view_func, view_args, view_kwargs):
		print('Md2-process_view')

	def process_response(self, request, response):
		print('Md2-process_response')
		return response

	def process_exception(self, request, exception):
		print('Md2-process_exception')
