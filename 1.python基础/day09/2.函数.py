# ### 函数
"""
概念:功能(包含一部分代码 实现某一个功能 达成某一个目的)
特点:可以反复调用,提高代码的复用性,提高开发效率,便于维护管理
"""

# 1.函数的基本格式
"""
# 定义一个函数
def 函数名():
	code1
	code2

# 调用函数
函数名()
"""

# 定义函数
def func():
	print("我是一个函数 ...")
# 调用函数
func()

# 2.函数的命名
"""
字母数字下划线,首字符不能为数字
严格区分大小写,且不能使用关键字
函数命名有意义,且不能使用中文哦

驼峰命名法:
	(1) 大驼峰命名法:每个单词的首字符要大写(类的命名)
		mycar => MyCar
	(2) 小驼峰命名法:除了第一个单词首字符小写外,剩下单词首字符大写(函数或者变量)
		mycar => myCar
	_命名法:可以将不同的单词用_拼接在一起
		mycar => my_car
		symmetric_difference symmetricDifference SymmetricDifference
"""

# 函数定义
def cfb_99():
	for i in range(1,10):
		for j in range(i,i+1):
			print("{d}*{d}={:2d}".format(i,j,i*j),end="")
		print()
# 调用函数
for i in range(5):
	cfb_99()














