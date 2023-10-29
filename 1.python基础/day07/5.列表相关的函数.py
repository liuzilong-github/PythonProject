# ### 列表相关的函数
# ### 增
# 1.append 向列表的末尾添加新的元素
lst = ["赵沈阳"]
lst.append("沈思雨")
print(lst)

# 2.insert 在指定索引之前插入元素
lst = ["赵沈阳", "沈思雨"]
lst.insert(1,"王伟")
print(lst)

# 3.extend 迭代追加所有元素
# 迭代追加的数据是可迭代性数据(容器类型数据,range对象,迭代器)
lst = ["赵沈阳","沈思雨"]
tup = (1,2,3)
lst.extend(tup)
print(lst)

strvar = "abc"
lst.extend(strvar)
print(lst)

lst.append(range(3))
print(lst)

# ### 删
# 1.pop 通过指定索引删除元素,若没有索引移除最后那个(推荐)
lst = ["曹静怡","王志国","邓鹏","合理"]
# 不指定下标,默认删除最后一个
res = lst.pop()
print(res)
print(lst)

# 指定下标,删除具体某个元素
res = lst.pop(1)
print(res)
print(lst)


# 2.remove 通过给与的值来删除,如果多个相同元素,默认删除第一个
lst = ["曹静怡","王志国","合理","邓鹏","合理"]
res = lst.remove("合理")
print(res)
print(lst)

# 3.clear 清空列表
lst = ["曹静怡","王志国","合理","邓鹏","合理"]
lst.clear()
print(lst)

# ### 改查参考4.py


# ### 列表的其他相关函数
# index 获取某个值在列表中的索引
lst = ["曹静怡","王志国","合理","邓鹏","合理","邓鹏辉","邓鹏蓝","合理","邓鹏绿"]
res = lst.index("合理")
res = lst.index("合理",3)
res = lst.index("合理",3,6)
# res = lst.index("合力达")		# error
print(res)

# count 计算某个元素出现的次数
res = lst.count("合理")
print(res)

# sort 对列表排序
lst = [-90,-100,-1,90,78]
# 从小到大进行排序
lst.sort()
# 从小到大进行排序
lst.sort(reverse=True)

# 对字符串进行排序(按照ascii编码)
lst = ["kobi","james","jordon","yaoming","yi"]
lst.sort()
print(lst)

# 是否可以对中文排序(了解 无规律可循)
lst = ["王文","蔡徐坤"]
lst.sort()
print(lst)

# reverse 列表反转操作
lst = [1,2,"a","财讯坤","易烊千玺"]
lst.reverse()
print(lst)














































