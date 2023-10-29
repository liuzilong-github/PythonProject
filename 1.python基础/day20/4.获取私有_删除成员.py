# ### 1.如何在类外访问私有成员

class Plane():
	# 公有成员
	captian = "赵沈阳"

	# 私有成员
	__air_sister = "3名空姐"

	# 公有绑定方法
	def fly(self):
		print("飞机要飞在平流层,才能减少震动". self.__air_sister)

	# 私有绑定方法
	def __age(self):
		print("空姐的年龄保密")

	# 公有无参方法
	def fly2():
		print("航天飞机要飞到太空层,翱翔太空")

	# 私有无参方法
	def __earn():
		print("机长的收入保密")

	def pub_get1(self):
		print(self.__air_sister)
		self.__age()

	def pub_get2():
		print(Plane.__air_sister)
		Plane.__earn()

# 实例化对象
obj = Plane()

# 方法一: 访问私有成员(不推荐)
# python私有化: 采取了改名策略 => _类名 + __air_sister
# print(obj.__air_sister)
print(obj._Plane__air_sister)
print(Plane.__dict__)
"""
{
'__module__': '__main__', 
'captian': '赵沈阳', 
'_Plane__air_sister': '3名空姐', 
'fly': <function Plane.fly at 0x7fe475693790>, 
'_Plane__age': <function Plane.__age at 0x7fe475693820>, 
'fly2': <function Plane.fly2 at 0x7fe4756935e0>, 
'_Plane__earn': <function Plane.__earn at 0x7fe475693550>, 
'pub_get1': <function Plane.pub_get1 at 0x7fe475693700>, 
'pub_get2': <function Plane.pub_get2 at 0x7fe47566af70>, 
'__dict__': <attribute '__dict__' of 'Plane' objects>, 
'__weakref__': <attribute '__weakref__' of 'Plane' objects>, 
'__doc__': None}
"""

# 方法二: 访问私有成员(使用类中的公有方法,间接访问私有成员) 推荐
obj = Plane()
obj.pub_get1()
Plane.pub_get2()


# ### 2.使用类对象删除相应的成员
"""
1.对象可以访问类中的公有成员,但是无权修改或者删除该类中的成员
2.对象在访问成员时,优先访问该对象自己的成员,如果没有在访问类的,类如果也没有直接报错
"""
# 删除对象成员属性
obj.captian = "赵世超"
del obj.captian
print(obj,captian)

# 删除对象成员方法
obj.basketball = lambda: print("我的私人飞机可以在天上打篮球")
print(obj.__dict__)
obj.basketball()
del obj.basketball
print(obj.__dict__)
# obj.basketball()	# error

# 删除类中成员属性
del Plane.captian
print(Plane.__dict__)
# Plane.captian		# error
# print(obj.caption)	# error

# 删除类中成员方法
del Plane.fly2
# Plane.fly2()	# error

# 注意: 对象无法调用无参方法!!
# 反过来,类可以调用对象的绑定方法吗? -- 可以
Plane.fly(obj)













