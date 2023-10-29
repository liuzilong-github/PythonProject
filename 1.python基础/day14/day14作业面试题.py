# 1.结果
"""默认参数身上的默认值会提前在内存中驻留,方便找到默认值"""
def extendList(val,list=[]):
    list.append(val)
    return list
list1 = extendList(10)
print(list1)
list2 = extendList(123, [])
print(list2)
list3 = extendList('a')
print(list3)

# 2.res是多少?
def func():
	return [lambda x : i*x for i in range(4)]
res = [m(2) for m in func()]
print(res)

# 解析:
"""
def func():
	lst = []
	for i in range(4):
		def niming(x):
			return i * x
		lst.append(niming)
	return lst
lst = func()
print(lst)

res = [m(2) for m in lst]


i为什么是3:
for i in range(4):
	print(i)
print(i)
print(i)
"""

"""
1.判断返回值到底是推导式还是匿名函数;
2.定义函数时,里面的代码一句都不走;
3.只有在调用函数时,才会执行其中的代码块,刺客去找寻当时的i,已经通过循环遍历到3了;
4.由于当时变量i与内函数发生绑定,延长了该变量的生命周期,所以内存没有释放,仍然可以找到;
5.在列表中是4个函数,通过传参 x=2,i=3 return 6,返回 [6,6,6,6]
"""



# 3.打印结果是多少?
def add(a,b):
    return a + b

def test():
    for r in range(4):
        yield r
g=test()
for n in [2,10]:
	g=(add(n,i) for i in g)
print(list(g))

# 解析:
"""
g = (add(10,i) for i in g)
g = (add(10,i) for i in (add(10,i) for i in g))
g = (add(10,i) for i in (add(10,i) for i in test()))
g = (add(10,i) for i in (add(10,i)) for i in (0,1,2,3))
g = (add(10,i) for i in (10,11,12,13))
g = (20,21,22,23)
"""

	
# 4.如何判断输入的数是质数( 1.通用方法完成 2.使用for .. else 完成 )
def prime(n):
	if isinstance(n, int):
		if n > 1:
			for i in range(2,n):
				if n % i == 0:
					return "不是质数"
			else:
				return "是质数"
		else:
			return "不是质数"
	else:
		return "输入错误,请输入大于1的整数"

res = prime(7)
print(res)

