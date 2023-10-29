# ### 装饰器: 在不改变原有代码的基础前提下,为原函数扩展新功能
"""
@符号 装饰器的标识符:
	(1) 自动把下面修饰的原函数当成参数传递给装饰器
	(2) 用返回的新函数去替换原函数
"""

# (1) 装饰器的原型

def kuozhan(_func):
	def newfunc():
		print("厕所前 ... 干净整齐")
		_func()
		print("厕所后 ... 臭气熏天")
	return newfunc

def func():
	print("我是屌丝...")

func = kuozhan(func)	# func = newfunc	func() <=> newfunc()
func()


# (2) @符号的使用
print("<===================>")
def kuozhan(_func):
	def newfunc():
		print("厕所前 ... 干净整齐")
		_func()
		print("厕所后 ... 臭气熏天")
	return newfunc

@kuozhan
def func():
	print("我是高富帅")

func()


# (3) 装饰器的嵌套
def kuozhan1(_func):
	def newfunc():
		print("厕所前 ... 人模狗样1")
		_func()
		print("厕所后 ... 牛头马面2")
	return newfunc

def kuozhan2(_func):
	def newfunc():
		print("厕所前 ... 面黄肌瘦3")
		_func()
		print("厕所后 ... 红光满面4")
	return newfunc


@kuozhan2
@kuozhan1
def func():
	print("我是白富美...5")

func()


# (4) 带有参数的装饰器
"""原函数和新函数的参数和返回值要保持一一对应"""
print("<===================>")
def kuozhan(_func):
	def newfunc(who, where, eat):
		print("厕所前 ... 文质彬彬")
		_func(who, where, eat)
		print("厕所后 ... 兽性大发")
	return newfunc

@kuozhan
def func(who, where, eat):
	print("{who}在{where}吃{eat}".format(who=who, where=where, eat=eat))

func("假率先", "浴缸", "榴莲") # <=> newfunc()


# (5) 带有参数返回值的装饰器
print("<===================>")

def kuozhan(_func):
	def newfunc(*args, **kwargs):
		print("手工更同学向下面拉屎的同学们致敬 ~")
		res = _func(*args, **kwargs)
		print("请使用我的自动便便称重器")
		return res
	return newfunc

@kuozhan
def func(*args, **kwargs):
	dic = {"liuwenbo":"刘文波","zhanglei":"张磊","songjian":"宋健"}
	lst = []
	try:
		i = 0
		for k,v in kwargs.items():
			# 键在dic中,再去拼凑字符串
			if k in dic:
				# 人名 + 地点 + 拉的重量
				strvar = dic[k] + "在" + args[i] + "拉了" + v
				lst.append(strvar)
				i += 1
	except:
		# print(i)	# 2
		# print(list(dic.values()))	# ['刘文波', '张磊', '宋健']
		# print(list(dic.values())[i])
		print("{}找不到拉屎的地点而错,请传入拉屎地点".format(list(dic.values())[i]))

	return lst
	# return ["刘文博在电线杆子下面拉了15吨" , "张磊拉了15斤","宋健拉了15克"]

res = func("电线杆子下面","电影院",liuwenbo="15吨",zhanglei="15斤",songjian="15克")
print(res)


# (6) 使用类装饰器
class KuoZhan():
	def __call__(self, _func):
		return self.kuozhan2(_func)

	def kuozhan1(func):
		def newfunc():
			print("厕所前 ... 饥肠辘辘")
			func()
			print("厕所后 ... 酒足饭饱")
		return newfunc

	def kuozhan2(self, func):
		def newfunc():
			print("厕所前 ... 蓬头垢面")
			func()
			print("厕所后 ... 衣衫褴褛")
		return newfunc

# 方式一
@KuoZhan.kuozhan1
def func():
	print("厕所进行时...")

func()

# 方式二
@KuoZhan()
def func():
	print("厕所进行时...")

func()


# (7) 带有参数的函数装饰器
def outer(num):

	def kuozhan(_func):

		def newfunc1(self):
			print(self)
			print("厕所前 ... 老实巴交")
			_func(self)
			print("厕所后 ... 浑身哆嗦")

		def newfunc2(self):
			print(self)
			print("厕所前 ... 狂送人头")
			_func(self)
			print("厕所后 ... 让二追三")

		if num == 1:
			return newfunc1
		elif num == 2:
			return newfunc2
		elif num == 3:
			return "厕所前,洗洗手,厕所后,漱漱口"

	return kuozhan


class MyClass():

	@outer(1)	# (1)@outer(1) => @KuoZhan 	  (2)@kuozhan => func1 = newfunc1 => 	(3)obj.func1() <=> obj.newfunc1(self)
	def func1(self):
		print("向前一小步,文明一大步")

	@outer(2)
	def func2(self):
		print("不冲就打包带走")

	@outer(3)
	def func3(self):
		print("请瞄准后发射,尿到外面,说明你短")

print("<==============>")
obj = MyClass()
obj.func1()	  # <=> obj.newfunc1(self)

print("<==============>")
obj.func2()
print("<==============>")
print(obj.func3)


# (8) 带有参数的类装饰器
"""
参数1: 给修饰的类添加成员属性和方法
参数2: 把类中的run方法变成属性
"""

class KuoZhan():

	ad = "贵族茅厕,茅厕中的百岁山"

	def money(self):
		print("贵族茅厕,包月1100,一小时200元")

	def __init__(self, num):
		self.num = num

	def __call__(self, cls):
		print(cls)	# Myclass
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)

	# 参数1的情况: 添加成员属性和方法
	def kuozhan1(self, cls):
		def newfunc():
			# MyClass.ad = "贵族茅厕,茅厕中的百岁山"
			cls.ad = KuoZhan.ad
			cls.money = KuoZhan.money
			return cls()
		return newfunc

	# 参数2的情况: 把方法变属性
	def kuozhan2(self, cls):
		def newfunc():
			if "run" in cls.__dict__:
				cls.run = cls.run()
				return cls()
		return newfunc

# 方式一:
@KuoZhan(1)	   # => @obj => MyClass = obj(MyClass)
class MyClass():
	def run(self):
		return "亢龙有悔"

obj = MyClass()
print(obj.ad)
obj.money()

# 方式二:
@KuoZhan(2)
class MyClass():
	def run(self):
		return "亢龙有悔"

obj = MyClass()
print(obj.run)


"""
扩展:
虽然MyClass2这个名字被替换掉了,但是内存中的该类仍然存在;
class MyClass2():
	a = 200

print(id(Myclass2), "111111")

def func(cls):
	cls.ad = 90
	print(id(cls), "222222")
	return cls()

obj = func(MyClass2)

Myclass2 = 100
print(MyClass)
print(obj.a)	# 200
print(obj.ad)	# 90
"""











