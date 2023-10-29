"""
1.编写装饰器，为多个函数加上认证的功能（用户的账号密码）
要求只要登录成功一次，后续的函数都无需输入用户名和密码
"""
# 方法一
# flag = False
# def login(_func):
# 	def newfunc(*args, **kwargs):
# 		global flag
# 		if flag:
# 			return _func(*args, **kwargs)
# 		else:
# 			username = input("请输入您的用户名:")
# 			password = input("请输入您的密码:")
# 			if username == "admin" and password == "123456":
# 				flag = True
# 				return _func(*args, **kwargs)
# 			else:
# 				print("对不起,账号或者密码输入错误")

# 	return newfunc


# @login
# def buy_bao():
# 	print("我要买包")

# @login
# def buy_fruit():
# 	print("我要买水果")

# buy_bao()
# buy_fruit()

# 方法二:
# class Shopping:

# 	def __init__(self):
# 		self.flag = False

# 	def login(_func):
# 		def newfunc(self, *args, **kwargs):
# 			if self.flag:
# 				return _func(self, *args, **kwargs)
# 			else:
# 				username = input("请输入您的用户名:")
# 				password = input("请输入您的密码:")
# 				if username == "admin" and password == "123456":
# 					self.flag = True
# 					return _func(self, *args, **kwargs)
# 				else:
# 					print("对不起,账号或者密码输入错误")

# 		return newfunc

# 	@login
# 	def buy_bao(self):
# 		print("我要买包")

# 	@login
# 	def buy_fruit(self):
# 		print("我要买水果")


# obj = Shopping()
# obj.buy_bao()
# obj.buy_fruit()


"""
2.编写装饰器，为多个函数加上记录调用功能，
要求每次调用函数都将被调用的函数名称写入文件
"""
def kuozhan(_func):
	def newfunc(*args, **kwargs):
		with open("log.txt", mode="a", encoding="utf-8") as fp:
			fp.write(_func.__name__ + "\n")
		return _func(*args, **kwargs)
	return newfunc

@kuozhan
def func():
	print("test")

func()

