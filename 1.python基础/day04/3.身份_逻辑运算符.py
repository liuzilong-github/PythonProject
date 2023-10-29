# ### 身份运算符 is 和 is not (检测两个数据在内存当中是否是同一个值)

# 整型 -5~正无穷
var1 = 100
var2 = 100
print(var1 is var2)

# 浮点型 非负数
var1 = -9.1
var2 = -9.1
print(var1 is var2)

# bool 相同即可
var1 = True
var2 = True
print(var1 is var2)

# complex 在实数+虚数不相同（只有叙述的情况下例外）
var1 = 6-8j
var2 = 6-8j
var1 = -10j
var2 = -10j
print(var1 is var2)

# 容器: 相同字符串，空元组相同 剩下的所有容器都不相同
container1 = ()
container2 = ()
print(container1 is not container2)

container1 = "你"
container2 = "你"
print(container1 is not container2)

container1 = [1,23,4]
container2 = [1,23,4]
print(container1 is not container2)


# ### 逻辑运算符: and or not
# and 逻辑与
"""全真则真，一假则假"""
res = True and True		# True
res = True and False	# False
res = False and True	# False
res = False and False	# False
print(res)

# or 逻辑或
"""一真则真，全假则假"""
res = True or True		# True
res = False or True		# True
res = True or False		# True
res = False or False	# False
print(res)

# not 逻辑非
res = not True
res = not False

# 逻辑短路
"""
无论后面的表达式是True 还是False 都已经无法改变最后的结果，那么直接短路，后面的代码不执行
(1) True or print("程序执行了 ~ 1111")
(2) False and print("程序执行了 ~ 2222")

True or print("程序执行了 ~ 1111")
True or True ==> True
True or False ==> True
False and print("程序执行了 ~ 2222")
False and True ==> False
False and False ==> False
"""

"""
计算规律：
	先脑补计算当前表达式的布尔值是True还是False
	如果出现了True or 表达式 或者False and 表达式的情况，直接返回前者，后面代码不执行
	如果没有出现段杜效果，直接返回后者
"""

res = 5 and 6 # 6
"""
True and True ==> True
True and False ==> False
"""
res = 5 or 6 # 5
res = 0 and 999 # 999
res = 0 or "abc" # "abc"
print(res)

# 逻辑运算符的优先级
# 优先级从高到低: () > not > and > or
res = 5 or 6 and 7 # 5 or 7 ==> 5
res = (5 or 6) and 7 # 5 and 7 ==> 7
res = not (5 or 6) and 7 # not 5 and 7 ==> False and 7 ==> False

res = 1<2 or 3>4 and 5<100 or 100<200 and not (700>800 or 1<-1)
"""
not （False or False）==> True
res = 1<2 or 3>4 and 5<100 or 100<200 and not (700>800 or 1<-1)
res = True or False and True or True and True
res = True or False or True
res = True or True ==> True
"""
print(res)












