# ### 函数名的使用
"""
python中的函数可以像变量一样,动态创建,销毁,当做参数传递,作为值返回,叫第一类对象,其他语言功能有限
"""
def func():
	print("我是func函数")

# (1)动态创建
a = 1
print(a)
a = func()
a()


# (2)动态销毁
del a
# a()
# func()


# (3)当做参数传递
def func2():
	return "我是func2函数"

def func1(f):
	return f()	# "我是func2函数"

res = func1(func2)
print(res)


# (4)作为值返回
def func3():
	print("我是func3函数")

def func4(f):
	return f
res = func4(func3)
print(res)
res()


# (5)函数名可以作为容器类型数据的元素
lst = [func,func3]
for i in lst:
	i()


# ### __doc__ 或者 help查看文档
def big_chang_cishen(something):
	"""
	功能: 教你怎么吃大肠
	参数: 吃的内容
	返回值: 是否满意
	"""
	print("把{}洗一洗".format(something))
	print("直接找肠子头,放嘴里,吸一下")
	print("擦擦嘴,满意的放下肠子头")
	return "吃完了,真好吃~"

big_chang_cishen("生肠子")
# 方法一
res = big_chang_cishen.__doc__
print(res)
# 方法二
help(big_chang_cishen)














