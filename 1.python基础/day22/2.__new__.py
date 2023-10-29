# ### __new__ 魔术方法
"""
	触发时机: 实例化类生成对象的时候触发(触发时机在__init__之前)
	功能: 控制对象的创建过程
	参数: 至少一个cls接收当前的类,其他根据情况决定
	返回值: 通常返回对象或None
"""

# (1) 基本使用
class MyClass2():
	a = 100

obj2 = MyClass2()
print(obj2)

class MyClass1():
	def __new__(cls):
		# print(cls)
		# 1.返回本类对象
		"""类.成员方法(类)"""
		# return object.__new__(cls)
		# 2.返回其他类的对象
		# return obj2
		# 3.不返回对象,返回None
		return None

obj = MyClass1()
# print(obj.a)
print(obj)

# (2) __new__ 触发时机要快于 __init__
"""
__new__ 创建对象
__init__ 初始化对象
"""
class MyClass():

	def __new__(cls):
		print(1)
		return object.__new__(cls)

	def __init__(self):
		print(2)

obj = MyClass()

# (3) __new__ 的参数要和 __init__ 参数一一对应
class Boat():
	def __new__(cls, name):
		return object.__new__(cls)

	def __init__(self, name):
		self.name = name

obj = Boat("万里阳光号")
print(obj.name)

# 使用收集参数进行改造
class Boat():
	# *args, **kwargs 可以收集多余的所有参数
	def __new__(cls, *args, **kwargs):
		return object.__new__(cls)

	def __init__(self, name, type):
		self.name = name
		self.type = type

obj = Boat("万里阳光号", "破木头做的")
print(obj.name, obj.type)

# (4) __new__ 和 __init__ 之间的注意点
"""
如果__new__没有返回对象或者返回的是其他类的对象,不会调用构造方法
只有在返回自己本类对象的时候,才会调用构造方法
"""
class Children():
	def __new__(cls, *args, **kwargs):
		return obj2
		# pass

	def __init__(self, name, skin):
		print("构造方法被触发")
		# self.name = name
		# self.skin = skin

obj = Children("灭霸", "紫薯")

# print(obj.name)	# error
# print(obj.skin)	# error













