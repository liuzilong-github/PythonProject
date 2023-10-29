# ### 函数的传参
"""
参数: 函数运算时需要的值

参数种类:
	(1)形参:形式参数,在函数的定义处
	(2)实参:实际参数,在函数的调用处

形参的种类:
	1.普通形参(位置形参) 2.默认形参 3.普通收集形参 4.命名关键字形参 5.普通关键字形参
实参的种类:
	1.普通实参 2.关键字实参

原则:
	形参和实参要一一对应
"""

# 1.普通形参(位置形参)
# 定义函数
"""hang,lie普通形参,在函数定义处"""
def small_star(hang,lie):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			print("*",end="")
			j += 1
		print()
		i += 1
# 调用函数
# 10,10普通实参,在函数的调用处
small_star(10,10)
small_star(2,3)

# 2.默认形参
"""hang,lie默认形参,在函数定义处"""
"""
如果给与实参,那么使用实参
如果没有给与实参,那么使用参数身上的默认值
"""
def small_star(hang=10,lie=10):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			print("*",end="")
			j += 1
		print()
		i += 1

small_star(4,8)
small_star(8)
small_star()


# 3.普通形参 + 默认形参
"""普通形参必须写在默认形参的前面不能掉换位置"""
def small_star(hang,lie=10):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			print("*",end="")
			j += 1
		print()
		i += 1

small_star(5,7)
small_star(5)
# small_star()	# error


# 4.关键字实参
"""
1.如果都是关键字实参,可以任意调整实参的顺序
2.普通实参必须写在关键字实参的前面
"""
def small_star(hang,a,b,c,lie=10):
	i = 0
	while i < hang:
		j = 0
		while j < lie:
			print("*",end="")
			j +=1
		print()
		i += 1

# hang a ... lie 具体指定参数的值叫做关键字实参,在函数的调用处
# small_star(hang=3,a=4,b=5,c=6,lie=7)
# small_star(b=5,c=6,lie=7,a=4,hang=3)
small_star(3,4,b=5,c=6,lie=7)
small_star(3,4,b=5,lie=7,c=6)
# small_star(b=5,c=6,lie=7,3,4)	  # error	









