# ### 异常处理的语法
"""
try ... except ... 来抑制错误
把有可能报错的代码放到try这个代码块当中,
如果有报错,直接执行except这个代码块
如果没有报错,不执行except这个代码块

在异常处理当中,所有的异常类都继承 BaseException Ecxeption为普通异常的父类
类型上的子父关系
from collections import Iterator, Iterable
print(issubclass(Iterator, Iterable))
"""

# 1.基本语法
class MyClass():
	a = 6

try:
	lst = [1,2,3]
	lst[1000]
except:
	pass

try:
	lst = [1,2,3]
	lst[1000]
except BaseException:
	pass


# 2.带有分支的异常处理
try:
	# lst = [1,2,3]
	# lst[1000]

	# dic = {"a":1, "b":2}
	# dic["c"]

	# print(lisi)

	MyClass.abc()
except IndexError:
	print("下标越界")
except KeyError:
	print("字典的键不存在")
except NameError:
	print("这个变量不存在")
except:
	print("有异常错误")


# 3.处理生成器的异常报错
def mygen():
	yield 1
	yield 2
	yield 3
	return [1,2,3]

try:
	gen = mygen()
	print(next(gen))
	print(next(gen))
	print(next(gen))
	print(next(gen))

	# 给StopIteration这个类创建出来的对象起一个别名叫e
	"""
	当你打印对象时,会触发内部__str__方法,通过一系列的调用,返回出最后的返回值
	"""
except StopIteration as e:
	# 可以获取返回值
	print(e)

	"""
	# 额外的扩展
	res = str(e)
	print(res, type(res))
	res2 = eval(res)
	print(res2, type(res2))
	"""


# 4.异常处理的其他方法	
"""
1.try ... except ... else ...
当try这个代码块当中没有报错的时候,执行else这个分支
如果try代码块有报错,就不执行else这个分支
"""
try:
	# lst = [1,2,3]
	# lst[1000]
	print(123)
except:
	pass
else:
	print("执行了else分支...")

"""
2.try ... finally ... 无论代码块是否报错,都必须要执行的代码写在finally这个代码块当中
场景: 应用在异常环境下,保存数据或者关闭数据库等操作,必须要在数据库程序崩溃之前执行的代码写在finally代码块中
"""
# try:
# 	lst = [1,2,3]
# 	lst[1000]
# finally:
# 	print(2345678)

"""
3.try ... except .... else ... finally ...
"""
try:
	lst = [1,2,3]
	lst[1000]
	# print(123)
except:
	print(456)
else:
	print("执行了else分支...")
finally:
	print("执行关闭数据库操作")









