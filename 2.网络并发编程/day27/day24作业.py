"""
1.编写装饰器，为多个函数加上认证的功能（用户的账号密码）
要求只要登录成功一次，后续的函数都无需输入用户名和密码
"""

# 方法一
flag = False
def login(func):
	def inner(*args,**kwargs):
		global flag
		
		# 如果flag = True  代表已经登录
		if flag:
			res = func(*args,**kwargs)
			return res
			
		# 否则没有登录
		else:
			username = input("请输入您的用户名:")
			password = input("请输入您的密码")
			if username == "wangwen" and password == "111":
				# 登录成功
				flag = True
				res = func(*args,**kwargs)
				return res
			else:
				print("抱歉,账号或者密码输入错误~")
	return inner

@login
def buy_bao():
	print("我要买包")
	
@login
def buy_fruit():
	print("我要买水果")
	

# buy_bao()
# buy_fruit()


# 方法二
class Shopping():

	def __init__(self):
		self.flag = False

	# 装饰器
	def login(func):
		def inner(self,*args,**kwargs):
			
			
			# 如果flag = True  代表已经登录
			if self.flag:
				res = func(self,*args,**kwargs)
				return res
				
			# 否则没有登录
			else:
				username = input("请输入您的用户名:")
				password = input("请输入您的密码")
				if username == "wangwen" and password == "111":
					# 登录成功
					self.flag = True
					res = func(self,*args,**kwargs)
					return res
				else:
					print("抱歉,账号或者密码输入错误~")
		return inner

	@login
	def buy_bao(self,a):
		print("我要买包",a)
		
	@login
	def buy_fruit(self):
		print("我要买水果")
		
# obj = Shopping()
# obj.buy_bao(111111)
# obj.buy_fruit()
		
		
"""
2.编写装饰器，为多个函数加上记录调用功能，
要求 每次调用函数把调用的函数名称写入文件
"""

def log(func):
	def inner(*args,**kwargs):
		with open("log",mode="a",encoding="utf-8") as fp:
			fp.write( func.__name__ + "\n")
		res = func(*args,**kwargs)
		return res
	return inner

@log
def buy_bao():
	print("我要买包")

@log
def buy_fruit():
	print("我要买水果")


# print(buy_bao.__name__)
buy_bao()
buy_fruit()





























