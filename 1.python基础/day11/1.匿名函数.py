# ### 匿名函数: lambda表达式
"""
概念: 用一句话来表达只有返回值的函数
语法: lambda 参数: 返回值
特点: 简洁,高效
"""

# (1) 无参数的lambda表达式
def fun():
	return "文哥是个帅哥"

# 改造
func = lambda : "文哥是个帅哥"
print(func())


# (2) 有参数的lambda表达式
def func(n):
	return id(n)

# 改造
func = lambda n: id(n)
print(func(100))


# (3) 带有判断条件的lambda表达式
def func(n):
	if n % 2 == 0:
		return "偶数"
	else:
		return "奇数"

# 改造
func = lambda n: "偶数" if n % 2 == 0 else "奇数"
print(func(44))

# 三元运算符
"""
语法:
	真值 if 条件表达式 else 假值
	如果条件表达式成立为True,返回if前面的真值,反之,返回else后面的假值
"""
n = 13
res = "偶数" if n % 2 == 0 else "奇数"
print(res)


# 小练习
def func(x,y):
	if x > y:
		return x
	else:
		return y

# 改造
func = lambda x,y: x if x > y else y
print(func(40,70))













