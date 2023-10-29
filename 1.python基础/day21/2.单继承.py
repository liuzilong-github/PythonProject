# ### 继承

"""
一个类除了自身所拥有的属性方法之外,还获取了另外一个类的成员属性和成员方法,是一种继承关系
被继承的类叫做父类(基类,超类),继承的类叫做子类(衍生类)
在python中所有类都继承object这个父类
继承: (1) 单继承	(2) 多继承
"""

# ### 单继承
class Human(object):
	eye = "黑色的"

	def jump(self):
		print("古代人类都能上树")

	def beat_animal(self):
		print("古代人类都会打猎")

	def __makefire(self):
		print("古代人类会生火")

# (1) 子父继承之后,子类可以调用父类的公有成员
class Man(Human):
	pass

obj = Man()
obj.jump()

# (2) 子父继承之后,子类不能调用父类的私有成员
class Woman(Human):
	def pub_func(self):
		self.__makefire()

obj2 = Woman()
# obj2.__makefire()		# error
# obj2.pub_func()		# error

# (3) 子父继承之后,子类可以重写父类的同名公有方法
class Children(Human):
	def beat_animal(self):
		print("小孩天生只会打豆豆")

obj3 = Children()
obj3.beat_animal()









