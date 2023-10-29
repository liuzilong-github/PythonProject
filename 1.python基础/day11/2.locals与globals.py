# ### locals 与 globals 使用(了解)

# 一. locals 获取当前作用域所有的变量
# 1.全局空间
"""
locals 在函数外,获取的是打印之前所有的全局变量
locals 在函数内,获取的是调用之前所有的局部变量
"""
def func():
	a1 = 1
	b2 = 2

a = 1
b = 2
res = locals()
c = 3
print(res)
d = 4

# 2.局部空间
a = 1
b = 2
def func():
	a1 = 1
	b2 = 2
	res = locals()
	c3 = 3
	print(res)
	d4 = 4
c = 3
func()
d = 4


# 二.globals 只获取全局空间的全局变量
"""
globals 在函数外,获取的是打印之前所有的全局变量
globals 在函数内,获取的是调用之前所有的全局变量
"""
# 1.全局空间
def func():
	a1 = 1
	b2 = 2

a = 1
b = 2
res = globals()
c = 3
print(res)
d = 4

# 2.局部空间
a = 1
b = 2
def func():
	a1 = 1
	b2 = 2
	res = globals()
	c3 = 3
	print(res)
	d4 = 4
c = 3
func()
d = 4



# ### globals 返回的是内置系统的全局字典
dic = globals()
print(dic)

# 通过字符串可以创建全局变量
dic["wangwen"] = "18岁"
print(wangwen)

# 批量创建全局变量
def func():
	dic = globals()
	for i in range(1,5):
		# 批量在dic当中添加键值对,以创建全局变量
		dic["a%d" % (i)] = i
		"""
		dic["a1"] = 1
		dic["a2"] = 2
		dic["a3"] = 3
		dic["a4"] = 4
		"""
func()
print(a1, a2, a3, a4)










