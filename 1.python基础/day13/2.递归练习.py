# ### 递归练习

# 1.使用递归实现任意数n的阶乘

# 普通实现
# 5! = 5*4*3*2*1
n = 5
total = 1
for i in range(n,0,-1):
	total *= i
print(total)

# 递归实现
def jiecheng(n):
	if n <= 1:
		return 1
	return jiecheng(n-1) * n

print(jiecheng(5))
"""
jiecheng(1) => 1
jiecheng(2) => jiecheng(1) * 2 => 1 * 2
jiecheng(3) => jiecheng(2) * 3 => 1 * 2 * 3
jiecheng(4) => jiecheng(3) * 4 => 1 * 2 * 3 * 4
jiecheng(5) => jiecheng(4) * 5 => 1 * 2 * 3 * 4 * 5
"""

"""
代码解析:
去的过程:
n = 5 return jiecheng(n-1) * n => jiecheng(4) * 5
n = 4 return jiecheng(n-1) * n => jiecheng(3) * 4
n = 3 return jiecheng(n-1) * n => jiecheng(2) * 3
n = 2 return jiecheng(n-1) * n => jiecheng(1) * 2
n = 1 return 1

回的过程:
n = 2 return jiecheng(1) * 2 => 1 * 2
n = 3 return jiecheng(2) * 3 => 1 * 2 * 3
n = 4 return jiecheng(3) * 4 => 1 * 2 * 3 * 4
n = 5 return jiecheng(4) * 5 => 1 * 2 * 3 * 4 * 5

到此程序结束
返回 1 * 2 * 3 * 4 * 5
"""

# 2.使用尾递归来实现任意数的阶乘
"""return 在哪调用,在哪返回"""
"""自己调用自己,且返回是非运算表达式,指示函数本身"""
"""
特点:
	尾递归只开辟一个空间,不会无限开启,在一个空间里面去计算最后的结果进行返回,比较节省空间,有的解释器支持尾递归的调用特点
	但是cpython解释器目前不支持
写法:
	所有运算的值都在函数的参数中计算完毕,最后返回运算的参数
"""

def jiecheng(n, endval):
	if n <= 1:
		return endval
	return jiecheng(n-1, n * endval)

res = jiecheng(5,1)
print(res)

"""
代码解析:
去的过程:
n = 5,endval = 1 return jiecheng(n-1, n * endval) => jiecheng(4,5*1) => 5*1*4*3*2
n = 4,endval = 5*1 return jiecheng(n-1, n * endval) => jiecheng(3,5*1*4) => 5*1*4*3*2
n = 3,endval = 5*1*4 return jiecheng(n-1, n * endval) => jiecheng(2,5*1*4*3) => 5*1*4*3*2
n = 2,endval = 5*1*4*3 return jiecheng(n-1, n * endval) => jiecheng(1,5*1*4*3*2) => 5*1*4*3*2
n = 1,endval = 5*1*4*3*2 if n <= 1 成立 return endval
endva1 = 5*1*4*3*2
最下层空间的返回值是 5*1*4*3*2 最上层接收到的返回值也是 5*1*4*3*2
最下层和最上层返回的结果是一致的,所以对于尾递归来说,只需要考虑去的过程,无需考虑回的过程即可完成;
"""

# 优化代码1
def jiecheng(n, endval=1):
	if n <= 1:
		return endval
	return jiecheng(n-1, n * endval)

res = jiecheng(5,100)
print(res,"<======>")

# 优化代码2(把尾递归需要的参数值隐藏起来,避免篡改)
def outer(n):
	def jiecheng(n, endval=1):
		if n <= 1:
			return endval
		return jiecheng(n-1, n * endval)
	return jiecheng(n,1)

print(outer(5))

# 优化代码3(扩展)
# 闭包实现
def outer(n):
	endval = 1
	def jiecheng(n):
		nonlocal endval
		if n <= 1:
			return endval
		endval *= n
		return jiecheng(n-1)
	return jiecheng

func = outer(5)
print(func(5), "<=====>")


# 3.使用递归完成斐波那契数列
"""1 1 2 3 5 8 13 21 34"""

def feibo(n):
	if n == 1 or n == 2:
		return 1
	return feibo(n-1) + feibo(n-2)

print(feibo(6))
"""
代码解析:
n = 5
                               feibo(5) => 3 + 2 => return 5
        	  feibo(4)             +             feibo(3)
      feibo(3)      + feibo(2)             feibo(2) + feibo(1) => 1+1 => 2
feibo(2) + feibo(1) + feibo(2) => 1+1+1 =>3
"""










