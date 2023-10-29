# ### 异常处理

# IndexError		索引超出序列的范围
# lst = [1,2,3]
# lst[1000]


# KeyError			字典中查找了一个不存在的关键字
# dic = {"a":1, "b":2}
# dic["c"]


# NameError			尝试访问一个不存在的变量
# print(liuzilong)


# IndentationError	缩进错误
# if 5 == 5:
	# print(1)
  # print(2)


# AttributeError	尝试访问未知的对象属性
# class MyClass():
	# a = 100
# 
# obj = MyClass()
# obj.abc


# StopIteration		迭代器没有更多的值
# it = iter(range(3))
# res = next(it)
# res = next(it)
# res = next(it)
# res = next(it)


# AssertionError	断言语句(assert)失败
"""
assert 猜的意思,叫断言
如果正确的话没有任何反应,代码正常执行
如果是错误的直接报错,终止程序
"""
# assert 5 < 3
# print(111)






