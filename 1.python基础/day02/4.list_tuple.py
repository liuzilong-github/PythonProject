# ### 列表类型 list
"""特征：可获取，可修改，有序"""
# 1.定义一个空列表
listvar = []
print(listvar, type(listvar))
# 定义普通列表
listvar = [1,2,3,4,True,"ceshi"]

# 2.获取列表中的元素
# 正向索引：从0开始，从左往右以此计算
# 逆向索引：从-1开始，从右往左以此计算

res = listvar[2]
res = listvar[-2]
print(res)

# len 获取容器类型数据中的元素个数
# 通用写法
length = len(listvar)
res = listvar[length - 1]
print(res)
# 简写
res = listvar[len(listvar) - 1]
print(res)

# python逆向索引的特点，瞬间得到列表中 的最后一个元素
print(listvar[-1])

# 3.修改列表中的元素
listvar = [1,2,3,4,True,"ceshi"]
listvar[3] = 888
print(listvar)



# ### 元组类型 tuple
"""特征：可获取，不可修改，有序"""
# 1.定义一个元组
tuplevar = (1,2,3,4,5)
print(tuplevar, type(tupletvar))

# 2.获取元组中的元素
# 正向索引：从0开始，从左往右以此计算
# 逆向索引：从-1开始，从右往左以此计算

print(tuplevar[0])
print(tuplevar[-3])

# 修改元组中的元素：元组中的值不能修改
# tuplevar[0] = 888		error

# 注意点：
"""逗号才是区分是否是元组的标识符"""
tuplevar = (8.9)
tuplevar = 8.1,
print(tuplevar, type(tuplevar))

# 定义空元组
tuplevar = set()
print(type(tuplevar))



# ### 字符串类型
"""特征：可获取，不可修改，有序"""
# 正向索引：从0开始，从左往右以此计算
# 逆向索引：从-1开始，从右往左以此计算

# 获取字符串中的元素
print(strvar[3])
print(strvar[-1])

# 不能修改字符串中的元素
#strvarp[1] = "test"		error 

strvar = ""		# 单纯的定义一个空字符串
print(strvar)
print(type(strvar))
strvar = "   "	#字符串中含有三个空格字符
print(strvar[0])
print(type(strvar))








