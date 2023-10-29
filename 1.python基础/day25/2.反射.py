# ### 反射
"""通过字符串操作类对象, 或者模块中的相关成员的操作"""
"""
# hasattr() 检测对象/类是否有指定的成员
# getattr() 获取对象/类成员的值
# setattr() 设置对象/类成员的值
# delattr() 删除对象/类成员的值
"""

# ### part1 通过字符串反射类对象中的成员
class Father():
	pass

class Mother():
	pass

class Children(Father, Mother):
	eye = "蓝色的"
	weight = "1吨"

	def eat(self):
		print("小孩生下会喝奶")

	def drink(self):
		print("小孩生下喜欢喝勇闯天涯...")

	def __la(self):
		print("小孩自动啦,无法控制")

obj = Children()

# (1) hasattr() 检测对象/类是否有指定的成员
# 对象
res = hasattr(obj, "eye")
print(res)

# 类
res = hasattr(Children, "eat123")
print(res)

# (2) getattr() 获取对象/类成员的值
# 对象
res = getattr(obj, "weight")
print(res)
# 如果获取的值不存在,可以设置第三个参数,防止报错
res = getattr(obj, "weight123", "抱歉,这个值不存在")
print(res)

# 类
# 通过类进行反射(反射出来的是普通方法)
func = getattr(Children, "drink")
print(func)
func(1)
# 通过对象进行反射(反射出来的是绑定方法)
func = getattr(obj, "drink")
print(func)
func()

# 综合案例
strvar = "eat11"
if hasattr(obj, strvar):
	func = getattr(obj, strvar)
	func()
else:
	print("抱歉,该成员不存在")

# (3) setattr() 设置对象/类成员的值
# 对象
setattr(obj, "skin", "黑人")
print(obj.skin)
# 类
setattr(Children, "skin", "土耳其人")
print(Children.skin)
print(obj.skin)

# (4) delattr() 删除对象/类成员的值
# 对象
delattr(obj, "skin")
print(obj.skin)

# # 类
delattr(Children, "skin")
print(Children.skin)


# ### part2 通过字符串反射模块中的成员
"""
sys.modules 返回一个系统字典,字典的键是加载的所有模块
'__main__': <module '__main__' from '/mnt/hgfs/python32_gx/day25/2.py'>
字典中的__main__这个键对应的是该文件的模块对象
"""

def func1():
	print("我是func1方法")
def func2():
	print("我是func2方法")
def func3():
	print("我是func3方法")

import sys
print(sys.modules)	# 系统字典
module = sys.modules["__main__"]
print(module)
res = getattr(module, "func1")
print(res)

# 综合案例: 通过字符串反射模块中的成员
while True:
	strvar = input("请输入您想使用的功能:")
	if hasattr(module, strvar):
		func = getattr(module, strvar)
		func()
	elif strvar.upper() == "Q":
		print("再见")
		break
	else:
		print("没有该成员~")








