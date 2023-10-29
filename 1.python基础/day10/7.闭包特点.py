# ### 闭包特点
"""
特点:在闭包函数中,内函数使用了外函数的局部变量,
该变量会与内函数发生绑定,延长该变量的生命周期,
持续到脚本执行结束.
"""
def outer(val):
	def inner(num):
		return val + num
	return inner

func = outer(10)
res = func(15)
print(res)


# ### 闭包的意义
"""全局变量的作用域大,容易被篡改"""
num = 0
def click_num():
	global num
	num += 1
	print(num)

click_num()
click_num()
click_num()
num = 100
click_num()
click_num()

# 改造,用闭包来实现
"""
闭包的意义:
	闭包可以优先使用外函数中的变量,并对闭包中的值起到了封装保护的作用,外部无法访问
"""
def outer():
	x = 0
	def click_num():
		nonlocal x
		x += 1
		print(x)
	return click_num

click_num = outer()
click_num()
click_num()
click_num()
x = 100
click_num()
click_num()













