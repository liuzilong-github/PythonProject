"""
1.请定义一个交通工具(Vehicle)的类，其中有:
属性：速度(公有speed)， 车的类型(私有type)
方法：速度(公有setSpeed)，加速(私有speedUp),减速(私有speedDown)
让公有setSpeed调用私有speedUp和私有speedDown
"""
class Vehicle():
	speed = "百公里1小时"
	__type = "拖拉机小蹦蹦"
	
	def setSpeed(self):
		self.__speedUp()
		self.__speedDown()
		
	def __speedUp(self):
		print("我是加速方法,速度{}".format(self.speed))
		
	def __speedDown(self):
		print("我是减速方法,小车的类型是{}".format(Vehicle.__type))
		
obj = Vehicle()
obj.setSpeed()

"""
2.用类改写:猜数字游戏：
一个类有两个成员num和guess，
num有一个初值100。
定义一个方法guess，
调用guess,如果大了则提示大了，小了则提示小了。等于则提示猜测成功。
"""
import re
class GuessGame():
	num = 100
	def guess(self):
		while True:
			n = input("请输入要猜测的数字")
			obj = re.search(r"^\d+$",n)
			# print(obj)
			if obj:
				n = int(obj.group())
				if n > self.num:
					print("大了..")
				elif n < self.num:
					print("小了..")
				elif n == self.num:
					print("ok~ bingo")
					break
			else:
				print("输入的内容不正确")

# obj = GuessGame()
# obj.guess()

"""
3.创建一个圆Circle类。
为该类提供一个变量r表示半径
方法一返回圆的面积,方法二返回圆的周长；
"""
import math
class Circle():
	r = 3
	def area(self):
		return math.pi * self.r ** 2
	
	def perimeter(self):
		return 2 * math.pi * self.r
		
obj = Circle()
res1 = obj.area()
res2 = obj.perimeter()
print(res1,res2)

# 方法二 (推荐)
import math
class Circle():
	
	def __init__(self,r):
		self.r = r	
	
	def area(self):
		return math.pi * self.r ** 2
	
	def perimeter(self):
		return 2 * math.pi * self.r
		
obj = Circle(4)
res1 = obj.area()
res2 = obj.perimeter()
print(res1,res2)










