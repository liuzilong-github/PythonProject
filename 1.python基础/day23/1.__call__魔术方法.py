# ### __call__ 魔术方法
"""
	触发时机: 把对象当作函数调用的时候自动触发
	功能: 模拟函数化操作
	参数: 参数不固定,至少一个self参数
	返回值: 看需求
"""

# (1) 基本语法
class MyClass():
	def __call__(self):
		print("__call__魔术方法被触发")

obj = MyClass()
obj()

# (2) 利用 __call__ 魔术方法做统一调用
class Wash():
	def __call__(self, something):
		print("我要洗{}".format(something))
		self.step1(something)
		self.step2()
		self.step3()
		return "洗完了"

	def step1(self, something):
		print("放水,把{}扔进去".format(something))

	def step2(self):
		print("倒洗衣粉,洗衣液,蓝夜两,金纺,立白")

	def step3(self):
		print("洗一洗,晾干,穿上")

obj = Wash()
# obj.step1()
# obj.step2()
# obj.step3()
res = obj("袜子")
print(res)

# (3) 模拟整型强转操作
# bool int float 纯数字字符串
import math
class MyInt():
	def __call__(self, num):
		if isinstance(num, bool):
			if num == False:
				return 0
			else:
				return 1

		elif isinstance(num, int):
			return num

		elif isinstance(num, float):
			# 方法一
			a, b = str(num).split(".")
			return eval(a)

			# 方法二
			"""
			if num >= 0:
				return math.floor(num)
			else:
				return math.ceil(num)
			"""
			# 简写
			return math.floor(num) if num >= 0 else math.ceil(num)

		elif isinstance(num, str):
			if (num[0] == "+" or num[0] == "-") and num[1:].isdecimal():
				# 获取当前字符串的正负值
				if num[0] == "+":
					sign = 1
				elif num[0] == "-":
					sign = -1
				# 截取符号后面的字符串传递
				return self.calc(num[1:], sign)

			elif num.isdecimal():
				return self.calc(num)
			else:
				return "这个算不了"

	# 计算最后的数值
	def calc(self, num, sign=1):
		# 去掉前面的"0"字符串
		num = num.lstrip("0")
		# print(num, type(num))
		if num == "":
			return 0
		return eval(num) * sign


myint = MyInt()
res = myint(-6.75)
print(res, type(res))
res = myint("-0000000003242")
print(res, type(res))
res = myint("addsdasdas")
print(res, type(res))
print(myint("+000000000000"))

# int(3.78) => 3
# print(int(-3.78))
# import math
# print(math.floor(0)) => 0
# print(math.ceil(0))

"""
print(    int("00000000000001223")   )  # 1223
print(    int("-00000000000001223")   ) # -1223
print(    int("+00000000000001223")   ) # 1223
print(    int("+0000000000000")   ) # 0
"""

# print(    int("asdfasdfasdfasdf")   ) # error
# print(  eval("00000000000001223")   )
# print(  eval("+00000000000001223")   )
# print(  eval("-00000000000001223")   )
# print(  eval("-00000000000001223abc")   )






























