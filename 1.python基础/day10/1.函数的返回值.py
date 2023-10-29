# ### return 自定义函数的返回值
"""
概念:return 把函数内部的数据返回到函数的外面,返回到函数的调用处

1.return + 六大标准数据类型,除此之外还可以返回函数或者是类对象
2.return 在执行时,意味着终止函数,后面的代码不执行
3.如果不定义return返回值,默认返回None
"""

# (1) return + 六大标准数据类型
def func():
	# return 111
	# return 6.89
	# return "你好帅"
	# return [1,2,3]
	# return {"a":1, "b":2}
	return 1,2,3	# 返回元组
res = func()
print(res)

# (2) return 在执行时,意味着终止函数,后面的代码不执行
def func():
	print(1)
	print(2)
	return 3
	print(4)
res = func()
print(res)

def func():
	for i in range(5):
		if i == 3:
			return 4
		print(i)
res = func()
print(res)

# (3) 如果不定义return返回值,默认返回None
def func():
	pass

res = func()
print(res)	# None

# 注意点:打印的数据和返回的数据不是等价的,返回的数据是可以自定义的;
res = print(1234)
print(res)	# None



# 模拟一个+_*/计算器
"""
功能: 完成计算
参数: 2个数字和运算符
返回值: 计算后的结果
"""
def calc(num1, num2, sign):
	if sign == "+":
		return num1 + num2
	elif sign == "-":
		return num1 - num2
	elif sign == "*":
		return num1 * num2
	elif sign == "/":
		if num2 == 0:
			return "除数不能为零"
		return num1 / num2
	else:
		return "抱歉,超出了我的运算范围."

res = calc(3,5,"+")
res = calc(3,5,"-")
res = calc(3,5,"*")
res = calc(3,0,"/")
res = calc(3,0,"&")
print(res)















