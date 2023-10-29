# ### 1.集合的相关操作(交叉并补)

set1 = {"易烊千玺","王一博","刘某PDD","王文"}
set2 = {"倪萍","赵忠祥","金龟子大风车","小龙人","王文"}
# intersection()	交集
res = set1.intersection(set2)
print(res)

# 简写 &
res = set1 & set2
print(res)

# difference()	差集
res = set1.defference(set2)
print(res)

# 简写 -
res = set1 - set2
print(res)

# union()	并集
res = set1.union(set2)
print(res)

# 简写 |
res = set1 | set2
print(res)

# symmetric_difference()	对称差集(补集情况涵盖其中)
res = set1.symmetric_differenc(set2)
print(res)

# 简写 ^
res = set1 ^ set2
print(res)


# issubset()	判断是否是子集
set1 = {"刘德华","郭富城","张学友","王文"}
set2 = {"王文"}
res = set2.issubset(set1)
print(res)

# 简写
res = set2 < set1
print(res)

# issuperset()	判断是否是父集
set1 = {"刘德华","郭富城","张学友","王文"}
set2 = {"王文"}
res = set1.issuperset(set2)
print(res)

# 简写
res = set1 > set2
print(res)

# isdisjoint()	检测两集合是否不相交	不相交 True 相交 False
set1 = {"刘德华","郭富城","张学友","王文"}
set2 = {"王文"}
res = set1.isdisjoint(set2)
print(res)


# ### 2.集合的相关函数
# 增
# add()		向集合中添加元素
# 一个一个加
set1 = {"王文"}
set1.add("王伟")
print(set1)

# update()	迭代着添加
# 一次加一堆
set1 = {"王文"}
lst = ["a", "b", "c"]
lst = "ppp"		# 迭代着添加,无序,会去重
set1.update(lst)
print(set1)


# 删
setvar = {'刘某PDD', '小龙人','倪萍', '赵忠祥'}
# clear()	清空集合
setvar.clear()
print(setvar)

# pop()		随机删除集合中的一个数据
res = setvar.pop()
print(res)
print(setvar)

# discard()		删除集合中指定的值(不存在的不删除 推荐使用) ***
setvar.discard("刘某PDD1111111")		# success
# setvar.discard("刘某PDD")
print(setvar)

# remove()		删除集合中指定的值(不存在则报错)	了解
setvar.remove("刘某PDD111")	# error
setvar.remove("刘某PDD")
print(setvar)


# ### 3.冰冻集合(额外了解)
"""frozenset 单纯的只能做交叉并补操作,不能做添加或者删除的操作"""
lst = ["王文","宋健","何旭彤"]
fz1 = frozenset(lst)
print(fz1, type(fz1))

# 不能再冰冻集合中添加或者删除元素
fz1.add(1)
fz1.update("abc")
fz1.discard("王文")

# 冰冻集合只能做交叉并补
lst2 = ["王文","王同培","刘一缝"]
fz2 = frozenset(lst2)
print(fz2, type(fz2))

# 交集
res = fz1 & fz2
print(res)

# 遍历冰冻集合
for i in fz2:
	print(i)















