# ### 迭代器
"""
迭代器:
	能被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator 迭代器是对象)
概念:
	迭代器指的是迭代取值的工具,迭代是一个重复的过程,每次重复都是基于上一次的结果而继续的,
	单纯的重复并不是迭代
特征:
	并不依赖索引,而是通过next指针(内存地址寻址)迭代所有数据,一次只取一个值,
	而不是一股脑的把所有数据放进内存,大大节省空间
"""

# 一.可迭代对象
setvar = {"王同培","马春配","赵万里","赵沈阳"}
# 获取当前对象的内置成员
lst = dir(setvar)
print(lst)
# 判断是否是可迭代对象
res = "__iter__" in lst
print(res)
# for i in setvar:
	# print(i)


# 二.迭代器
"""
for循环之所以可以遍历所有的数据,是因为底层使用了迭代器,通过地址寻址的方式,一个一个的找数据;
可迭代对象 -> 迭代器  实际上就是从不能够被next直接调用 -> 可以被next指针直接调用的过程

如果是可迭代对象 -> 不一定是迭代器
如果是迭代器 -> 一定是可迭代对象
"""
# 1.如何创建一个迭代器
setvar = {"王同培","马春配","赵万里","赵沈阳"}
it = iter(setvar)
print(it)

# 2.如何判断一个迭代器
print(dir(it))
res = "__iter__" in dir(it) and "__next__" in dir(it)
print(res)

# 3.如何调用一个迭代器
"""next是单向不可逆的过程,一条路走到黑"""
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)
# res = next(it)
# print(res)

# 4.重置迭代器
it = iter(setvar)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())

# 5.调用迭代器的其他方法
# for
it = iter(setvar)
for i in it:
	print(i)

# for + next
it = iter(setvar)
for i in range(2):
	print(next(it))
print(next(it))
print(next(it))
print(next(it))		# error 超出了寻址范围

# 6.判断迭代器/可迭代对象的其他方法
# 从 ... 模块 引入 ... 内容
from collections import Iterator, Iterable
"""Iterator 迭代器 Iterable 可迭代对象"""
res = isinstance(it, Iterator)
print(res)
res = isinstance(it, Iterable)
print(res)

# 7.range是迭代器吗?
print(isinstance(range(10),Iterator))	# False
print(isinstance(range(10),Iterable))	# True

# 变成迭代器
it = range(10).__iter__()
print(isinstance(range(10),Iterator))	# True
print(isinstance(range(10),Iterable))	# True

# 调用it
# next
res = next(it)
print(res)
res = next(it)
print(res)

# for + next
for i in range(3):
	print(next(it))

# for
for i in it:
	print(i)




























