"""
1.请定义一个交通工具(Vehicle)的类，其中有:
属性：速度(公有speed)， 车的类型(私有type)
方法：速度(公有setSpeed)，加速(私有speedUp),减速(私有speedDown)
让公有setSpeed调用私有speedUp和私有speedDown
"""
class Vehicle():
	speed = "280km/h"
	__type = "超跑"

	def setSpeed(self):
		print("这里是公有方法速度")
		self.__speedUp()
		self.__speedDown()

	def __speedUp(self):
		print("这里是私有方法加速")

	def __speedDown(self):
		print("这里是私有方法减速")


"""
2.用类改写:猜数字游戏：
一个类有两个成员num和guess，
num有一个初值100。
定义一个方法guess，
调用guess,如果大了则提示大了，小了则提示小了。等于则提示猜测成功。
"""
class DigitalGames():
	num = 100

	def guess(self, number):
		if number.isdigit():
			number = int(number)
			if number > self.num:
				print("大了")
			elif number < self.num:
				print("小了")
			elif number == self.num:
				print("猜测成功")
		else:
			print("输入错误")

obj = DigitalGames()
number = input("请输入您要猜的数字:")
obj.guess(number)


"""
3.创建一个圆Circle类。
为该类提供一个变量r表示半径
方法一返回圆的面积,方法二返回圆的周长；
"""
import math


class Circle:
	r = 30

	def area(self):
		return "圆的面积为:{}".format(math.pi * (self.r ** 2))

	def circumference(self):
		return "圆的面积为:{}".format(math.pi * self.r * 2)



