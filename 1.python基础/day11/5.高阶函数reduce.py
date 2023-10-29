# ### reduce
"""
reduce(func,iterable)
功能: 计算数据
	把iterable中的前两个数据扔到func函数中做计算,把计算的结果和iterable中第三个值在继续扔到func中做计算
	以此类推 ...
	最后返回计算的结果
参数:
	func: 自定义函数
	iterable: 可迭代对象(容器类型数据,rang对象,迭代器)
返回值:
	计算的结果
"""

# (1) [7,7,5,8]  => 7758
lst = [7,7,5,8]

# 方法一
strvar = ""
for i in lst:
	strvar += str(i)
res = int(strvar)
print(res, type(res))

# 方法二
"""
7 * 10 + 7 = 77
77 * 10 + 5 = 775
775 * 10 + 8 = 7758
"""
# 1.先变成迭代器
it = iter(lst)
# 2.取出两个值
num1 = next(it)
num2 = next(it)
print(num1, num2)
# 做计算
total = num1 * 10 + num2
print(total)
# 3.把计算的结果再和剩下的数据做计算
for num in it:
	total = total * 10 + num
# 4.返回最后的结果
print(total, type(total))

# reduce改写
"""从...functools模块, 引入...reduce方法"""
from functools import reduce
lst = [7,7,5,8]
def func(x,y):
	return x * 10 + y
res = reduce(func, lst)
print(res)

# 使用lambda进行改造
print(reduce(lambda x,y: x * 10 + y, lst))


# 把字符串"123" 处理成数字的123
def func2(n):
	dic = {}
	for i in range(10):
		dic[str(i)] = i
	return dic[n]

it = map(func2, strvar)
# res = reduce(func, it)
# print(res, type(res))

# 简写
print(reduce(lambda x,y: x * 10 + y, it))












