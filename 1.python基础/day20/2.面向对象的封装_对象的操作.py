# ### 面向对象的封装 - 对象的操作

"""
封装:
	1.私有: 在类内可以互相访问,在类外不能访问
	2.公有: 在类内或者类外都可以访问

类中成员:
	1.成员属性
	2.成员方法

绑定方法:
	1.绑定到对象: 当对象去调用类中的成员方法时,系统会默认把该对象当成参数传递给该方法
	2.绑定到类: 当对象或者类去调用类中的成员方法时,系统会默认把该类当成参数传递给该方法

使用方式:
	对象.成员属性
	对象.成员方法

"""

class MyCar():
	# 公有属性:
	logo = "布加迪威龙"

	# 私有属性:
	__price = "2000万"

	# 公有方法:
	def run(self):
		print("百公里油耗300L,logo={},prince={}".format(self.logo, self.__price))

	# 私有方法:
	def __info(self):
		print("车主信息保密,据说是某个房地产大佬的儿子")

# 实例化对象(类的实例化)
obj = MyCar()

# (1)实例化的对象访问成员属性和成员方法
# 公有:
print(obj.logo)
obj.run()

# 私有(私有成员无法在类外访问,类内可以)
# obj.__price	# error
# obj.run()
# obj.__info()	# error


# (2)实例化的对象动态添加公有成员属性
obj.color = "尿黄色"
obj.logo = "五菱宏光"
print(obj.color)
print(obj.logo)

# __dict__ 获取类对象的内部成员
print(obj.__dict__)
print(MyCar.__dict__)


# (3)实例化的对象动态添加公有成员方法

# 1.无参方法
def dahuangfeng():
	print("请叫我大黄蜂")

obj.dahuangfeng = dahuangfeng
obj.dahuangfeng()

# 2.有参方法
# 基本版
def qingtianzhu(name):
	print("请叫我一柱擎天,{}".format(name))

obj.qingtianzhu = qingtianzhu
obj.qingtianzhu("擎天柱")

# 升级版
def qingtianzhu(obj, name):
	print("请叫我一柱擎天,{},我的颜色是{}".format(name, obj.color))

obj.qingtianzhu = qingtianzhu
obj.qingtianzhu(obj, "擎天柱")

# 究极版
"""
如果要创建绑定方法,参数的顺序,self对象本身要放到第一位"""
def qingtianzhu(obj, name):
	print("请叫我一柱擎天,{},我的颜色是{}".format(name, obj.color))

import types
# 创建绑定方法,系统自动把该对象当成参数传递给方法:
# types.MethodType(方法, 对象) => 绑定方法
res = types.MethodType(qingtianzhu, obj)
print(res)

obj.qingtianzhu = types.MethodType(qingtianzhu, obj)
obj.qingtianzhu("擎天柱")

# lambda表达式
obj.weizhentian = lambda: print("我是威震天")
obj.weizhentian()






























