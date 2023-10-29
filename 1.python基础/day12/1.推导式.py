# ### 推导式: 通过一行循环判断遍历出一系列数据的方法叫做推导式
"""
语法:
	val for val in iterable
"""

# 1.推导式基本语法
lst = []
for i in range(1,51):
	lst.append(i)
print(lst)

# 改写推导式
lst = [i for i in range(1,51)]
print(lst)

# 小练习
# 1.[1,2,3,4,5] => [2,4,6,8,10]
lst = [i*2 for i in range(1,6)]
print(lst)

# 2.带有判断条件的推导式
"""
注意点:for后面紧跟的判断条件只能是单项分支
"""
# [1,2,3,4,5,6,7,8,9,10] => [1,3,5,7,9 ...]
lst = [1,2,3,4,5,6,7,8,9,10]
lst_new = []
for i in lst:
	if i % 2 == 1:
		lst_new.append(i)
print(lst_new)

# 改写推导式
lst = [i for i in lst if i % 2 == 1]
print(lst)

# 3.多循环推导式	谁♡♢♤♠谁
lst1 = ["孙杰龙","陈露","曹静怡"]
lst2 = ["王志国","邓鹏","合理"]
lst_new = []
for i in lst1:
	for j in lst2:
		lst_new.append(i + "♡♢♤♠" + j)
print(lst_new)

# 改写推导式
lst = [i+"♡♢♤♠"+j for i in lst1 for j in lst2]
print(lst)


# 4.带有判断条件的多循环推导式
lst_new = []
for i in lst1:
	for j in lst2:
		if lst1.index(i) == lst2.index(j):
			lst_new.append(i+"♡♢♤♠"+j)
print(lst_new)

# 改写推导式
lst = [i+"♡♢♤♠"+j for i in lst1 for j in lst2 if lst1.index(i) == lst2.index(j)]
print(lst_new)














