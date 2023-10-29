# ### sorted
"""
sorted(iterable,key=函数,reverse=False)
功能:排序数据
参数:
	iterable: 可迭代对象(容器类型数据 range对象 迭代器)
	key: 指定函数(自定义/内置)
	revseer: 是否倒序
返回值:
	列表
"""

tup = (-90,89,78,3)
# 1.从小到大
res = sorted(tup)
print(res, type(res))

# 2.从大到小
res = sorted(tup, reverse=True)
print(res, type(res))

# 3.按照绝对值进行排序
tup = (-90,-100,1,2)
res = sorted(tup, key=abs)
print(res)
"""
1 => abs(1) => 1
2 => abs(2) => 2
-90 => abs(-90) => 90
-100 => abs(-100) => 100
"""

# 4.按照自定义函数进行排序
tup = (19,23,42,87)
"""
42 % 10 2 => 42
23 % 10 3 => 23
87 % 10 7 => 87
19 % 10 9 => 19
"""
def func(n):
	return n % 10
lst = sorted(tup, key=func)
print(lst)

# 5.任意的容器类型数据都可以通过sorted排序
container = "abc"
container = [1,2,3]
container = (1,2,3)
container = {"你好","王文","你真帅"}
container = {"caixukun","xiaozhan","zhaoshenyang","wangyibo"}
container = {"ww":"英俊帅气","zxy":"猥琐抠脚","zwl":"斯文败类"} 	# 排的是字典的键
print(sorted(container))


"""
总结:
sorted (推荐使用sorted)
	(1) 可以排序所有的容器类型数据
	(2) 返回一个新的列表
sort
	(1) 只能排序列表
	(2) 基于原来的列表进行排序
"""

