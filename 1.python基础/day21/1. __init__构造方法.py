# ### __init__构造方法

"""
触发时机: 实例化对象,初始化的时候会触发
功能: 为对象添加成员
参数: 参数不固定,至少一个self参数
返回值: 无
"""

# (1) 基本语法
class MyClass():
	def __init__(self):
		print("构造方法被触发...")
		self.color = "屎黄色"

# 实例化对象
obj = MyClass()
print(obj.__dict__)
print(obj.color)

# (2) 带有多个参数的构造方法
class MyClass():
	def __init__(self, color):
		self.color = color

# 实例化对象
obj1 = MyClass("狗屎绿")
print(obj1.color)
obj2 = MyClass("粉嫩红")
print(obj2.color)

# (3) 类可以是一个,对象可以是多个,创造的对象彼此是独立的;
class Children():
	def __init__(self, name, skin):
		self.name = name
		self.skin = skin

	def cry(self):
		print("小孩一生下就哇哇哇的哭")

	def la(self):
		print("小孩一生下来就拉粑粑")

	def __eat(self):
		print("小孩一生下来就要吃奶奶")

	def info(self):
		print("小孩的名字:{},小孩的肤色{}".format(self.name,self.skin))

	def info2(self, name, skin):
		print("小孩的名字:{},小孩的肤色{}".format(name,skin))

# 实例化对象
afanda = Children("阿凡达", "深蓝色")
afanda.cry()
afanda.info()

haoke = Children("绿巨人", "绿色的")
haoke.la()
haoke.info()

wangbaoqiang = Children("王宝强", "亮绿色")
wangbaoqiang.info()
# wangbaoqiang.__eat()	# error
wangbaoqiang.info2("张保障", "黄色")









