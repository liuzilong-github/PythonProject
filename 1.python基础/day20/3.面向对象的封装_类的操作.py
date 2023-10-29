# ### 面向对象的封装 - 类的操作

"""
使用方式:
	类.成员属性
	类.成员方法
"""

class MyCar():

	# 公有成员属性
	platenum = "京A88888"

	# 私有成员属性
	__earning = "月收入6000"

	# 公有成员方法
	def car_info():
		print("拍照信息可以公开")
		print("<=========>")
		MyCar.__money_info()

	# 私有成员方法
	def __money_info():
		print("收入信息保密", Mycar.__earning)


# (1)定义的类访问公有成员属性和方法
print(MyCar.platenum)
MyCar.car_info()

# Mycar.__money_info()	# error

# (2)定义的类动态添加公有成员属性
MyCar.oil = "1000L"
print(MyCar.oil)
print(MyCar.__dict__)

# (3)定义的类动态添加公有成员方法
# 1.无参方法
def car_light():
	print("我是造车灯的方法")

MyCar.car_light = car_light
MyCar.car_light()

# 2.有参方法:
def car_engine(name):
	print("我是造{}发动机的方法".format(name))

MyCar.car_engine = car_engine
MyCar.car_engine("三缸发动机")

# 3.lambda表达式
MyCar.luntai = lambda: print("我是造轮胎的方法")
MyCar.luntai()


# 对比: 对象和类之间的不同
"""
1.类中的无参方法默认只能类来调用,对象无法调用
2.对象可以调用类中的成员,反过来,类不能调用对象中的成员
3.每创建一个对象都会在内存中占用一份空间,对象之间是彼此独立的;
"""
obj = MyCar()
# obj.car_info	# error
MyCar.car_info()

obj.price = "10万"
print(MyCar.price)














