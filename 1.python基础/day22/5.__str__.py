# ### __str__ 魔术方法
"""
	触发时机: 使用print(对象)或者str(对象)的时候触发
	功能: 查看对象
	参数: 一个self接受当前对象
	返回值: 必须返回字符串类型
"""
class Cat():
	gift = "抓老鼠"

	def __init__(self, name):
		self.name = name

	def cat_gift(self):
		return "小猫叫{},小猫会{}".format(self.name, self.gift)

	def __str__(self):
		return self.cat_gift()

	__repr__ = __str__

tom = Cat("汤姆")

# 触发时机1: print(对象)
print(tom)
# 触发时机2: str(对象)
res = str(tom)
print(res)

print("<=============>")
res = repr(tom)
print(res, type(res))
print("<=============>")


# ### __repr__ 魔术方法
"""
	触发时机: 使用repr(对象)的时候触发
	功能: 查看对象,与魔术方法__str__相似
	参数: 一个self接受当前对象
	返回值: 必须返回字符串类型
"""
class Mouse():
	gift = "偷油吃"

	def __init__(self, name):
		self.name = name

	def mouse_gift(self):
		return "老鼠叫{},老鼠会{}".format(self.name, self.gift)

	def __repr__(self):
		return self.mouse_gift()

	# 系统底层默认把__repr__ 方法赋值给__str__方法,所以通过print或者str强转可以触发;
	# __str__ = __repr__

jerry = Mouse("杰瑞")
res = repr(jerry)
print(res)

# 可以触发
print(jerry)
res = str(jerry)
print(res)












