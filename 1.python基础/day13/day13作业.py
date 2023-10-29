# (选做)
# 1.可滑动的序列 自定义一个函数 根据参数n的值 , 变成对应个元素的容器 （zip）
"""
listvar = [1,2,3,4,5,6,7,8,9]
n = 2
listvar = [[1,2],[3,4],[5,6],[7,8]]
n = 3
listvar = [[1,2,3],[4,5,6],[7,8,9]]
n = 4
listvar = [[1,2,3,4],[5,6,7,8]]
"""
def division(n, lst):
	return zip(*[lst[i::n] for i in range(n)])

res = division(2,[1,2,3,4,5,6,7,8,9])
print(list(map(res)))


# 2.青蛙跳台阶  (递归实现)
'''
一只青蛙要跳上n层高的台阶
一次能跳一级,也可以跳两级
请问这只青蛙有多少种跳上这个n层高台阶的方法?
'''

def leap_frog(n):
	if n <= 2:
		return n
	return leap_frog(n-1) + leap_frog(n-2)

print(leap_frog(4))


# 3.递归反转字符串 "将14235 反转成53241" (递归实现)
strvar = "14235"
# 方法一:
def func(length, lst=[]):
	if length == 0:
		return "".join(lst)
	res = strvar[length - 1]
	lst.append(res)
	return func(length - 1)

print(func(len(strvar)))


# 方法二:
def func(strvar):
	if len(strvar) == 1:
		return strvar
	return func(strvar[1:]) + strvar[0]

res = func(strvar)
print(res)

"""
方法二解析:
递:
return func(4235) + 1
return func(235) + 4
return func(35) + 2
return func(5) + 3
return 5

归:
return func(5) + 3     => 5 + 3
return func(35) + 2    => 5 + 3 + 2
return func(235) + 4   => 5 + 3 + 2 + 4
return func(4235) + 1  => 5 + 3 + 2 + 4 + 1
return 5 + 3 + 2 + 4 + 1
"""


# 4.斐波那契数列用尾递归实现

def func(n, a=0, b=1):
	if n == 1:
		return b
	return func(n-1, b, a+b)

print(func(5))




