# ### 连贯操作
"""
不停地通过.调用下一个对象的操作叫做连贯操作
"""
class A():
	aaa = 100

class B():
	def __init__(self, obj):
		self.pty = obj

obj1 = A()
obj2 = B(obj1)

# 如何通过obj2对象调用aaa这个属性
# obj2.pty => <__main__.A object at 0x7f256716c2b0>
print(obj2.pty.aaa)


#
class Ceshi1():
	pty1 = 10

	def func1(self):
		print("我是func1方法")

class Ceshi2():
	def __init__(self, obj):
		self.pty2 = obj

	def func1(self):
		print("我是func2方法")

class Ceshi3():
	def __init__(self, obj):
		self.pty3 = obj

	def func1(self):
		print("我是func3方法")

class Ceshi4():
	def __init__(self, obj):
		self.pty4 = obj

	def func1(self):
		print("我是func4方法")

obj1 = Ceshi1()
obj2 = Ceshi2(obj1)
obj3 = Ceshi3(obj2)
obj4 = Ceshi4(obj3)

# 如何通过调用obj4这个对象获取 Ceshi1的pty1 的属性和 Ceshi2的func2 方法
print(obj4.pty4.pty3.pty2.pty1)
obj4.pty4.pty3.func2()








