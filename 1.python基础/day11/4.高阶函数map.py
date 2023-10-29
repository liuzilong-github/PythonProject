# ### 高阶函数: 能够把函数当成参数传递的就是高阶函数(map, filter, reduce, sorted)
# map
"""
map(func, iterable)
功能: 处理数据
	把iterable中的数据一个一个拿出来,扔到func做处理,通过调用迭代器来获取返回值
参数:
	func: 函数(内置函数,自定义函数)
	iterable: 可迭代性对象(容器类型数据,range对象,迭代器)
返回值:
	迭代器
"""
# (1) 把列表中的元素都变成整型
lst = ["1","2","3","4"]
lst_new = []
for i in lst:
	lst_new.append(int(i))
print(lst_new)

# 用map改写
from collections import Iterator,Iterable
it = map(int, lst)
print(isinstance(it, Iterator))
"""
代码解析:
	第一次调用迭代器
		先把列表中的第一个元素"1"拿出来扔到int中做强转,变成整型1返回出来
	第二次调用迭代器
		先把列表中的第二个元素"2"拿出来扔到int中做强转,变成整型2返回出来
	第三次调用迭代器
		先把列表中的第三个元素"3"拿出来扔到int中做强转,变成整型3返回出来
	第四次调用迭代器
		先把列表中的第四个元素"4"拿出来扔到int中做强转,变成整型4返回出来	
"""
# 1.调用迭代器 next
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))	# error

# 2.调用迭代器 for
it = map(int, lst)
for i in it:
	print(i)

# 3.调用迭代器 for + next
it = map(int, lst)
for i in range(3):
	print(next(it))

# 4.强转迭代器 => 列表
it = map(int, lst)
print(list(it))

# (2) [1,2,3,4] => [2,8,24,64]

print(1 * 2 ** 1)
print(2 * 2 ** 2)
print(3 * 2 ** 3)
print(4 * 2 ** 4)

# 1 << 1
# 2 << 2
# 3 << 3
# 4 << 4

lst = [1,2,3,4]
lst_new = []
for i in lst:
	lst_new.append(i << i)
print(lst_new)

# map改写
def func(n):
	return n << n

it = map(func, lst)
print(list(it))
"""
只有在调用迭代器的时候,才会真正触发map函数中的所有内容;不调用不触发;
强转迭代器时,把可以调用的所有数据都放到列表中
第一次调用时:
	把1拿出来,扔到func当中做处理,返回2
第二次调用时:
	把2拿出来,扔到func当中做处理,返回2
第三次调用时:
	把3拿出来,扔到func当中做处理,返回2
第四次调用时:
	把4拿出来,扔到func当中做处理,返回2
到此列表[2,8,24,64]

注意点: 形参和返回值必须写
"""

# (3) 给你一个列表["a","b","c"] => [97,98,99]
# 字典的键值反转操作
dic = {97:"a",98:"b",99:"c"}
dic_new = {}
for k,v in dic:
	dic_new[v] = k	# dic_new["a"] = 97
print(dic_new)

lst = ["a","b","c"]
lst_new = []
for i in lst:
	lst_new.append[dic_new[i]]
print(lst_new)

# map改写
def func(n):
	dic = {97:"a",98:"b",99:"c"}
	dic_new = {}
	for k,v in dic:
		dic_new[v] = k
	return dic_new[n]

it = map(func, lst)
print(list(it))












