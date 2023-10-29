# ### 单态模式: 同一个类,无论实例化多少次,都有且只有一个对象
"""
每创建一个对象,就会在内存中多占用一份空间
为了节省空间,提升执行效率,使用单态模式
场景: 只是单纯调用类中的成员,而不会额外为当前对象添加成员;
"""

class Singleton():
	__obj = None

	def __new__(cls):
		if cls.__obj is None:
			cls.__obj = object.__new__(cls)
		return cls.__obj

"""
第一次,在实例化对象时触发__new__魔术方法
if cls.__obj is None 条件成立, cls.__obj = object.__new__(cls) 创建一个对象给私有成员属性__obj
return cls.__obj 用obj1接收到了该对象

第二次,在实例化对象时触发__new__魔术方法
if cls.__obj is None 不成立,因为已经在__obj属性中存放了一个对象
return cls.__obj

第三次,在实例化对象时触发__new__魔术方法
if cls.__obj is None 不成立,因为已经在__obj属性中存放了一个对象
return cls.__obj
"""
obj1 = Singleton()
obj2 = Singleton()
obj3 = Singleton()
print(obj1, obj2, obj3)

# 
class Singleton():
	__obj = None

	def __new__(cls, *args, **kwargs):
		if cls.obj is None:
			cls__obj = object.__new__(cls)
		return cls__obj

	def __init__(self, name):
		self.name = name

obj1 = Singleton("康裕康")
obj2 = Singleton("张保张")
print(obj1, obj2)
print(obj1.name)
print(obj2.name)
"""
第一次实例化对象时,
触发__new__ if cls.__obj is None: 创建一个新的对象进行返回
然后触发__init__ self.name = 康裕康

第二次实例化对象时,
触发__new__ if cls.__obj is None: 条件不满足,返回的是第一次实例化的对象,是同一个
然后触发__init__ self.name = 张保张

输出结果:
张保张,张保张

等同于定义字符串:
name = "康裕康"
name = "张保张"
print(name)
"""










