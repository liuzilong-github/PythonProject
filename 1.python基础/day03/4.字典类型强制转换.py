# ### 二级容器（list tuple set dict）

# 二级列表
lst = [1,2,3,[4,5,6]]
# 二级元组
tup = (1,2,(10,11))
# 二级集合
setvar = {1,2,("a","b")}
# 二级字典
dic = {"a":1,"b":{"c":10}}
print(dic["b"]["c"])

# 四级容器
container = [1,2,3,(4,5,6,{"a":1,"b":[11,"bingo"]})]
res1 = container[-1]	# (4,5,6,{"a":1,"b":[11,"bingo"]})
res2 = res1[-1]			# {"a":1,"b":[11,"bingo"]}
res3 = res2["b"]		# [11,"bingo"]
res4 = res3[-1]			# "bingo"
print(res4)

# 一步简写
res = container[-1][-1]["b"][-1]
print(res)

# 等长的二级容器
"""外面是容器，里面的元素也是容器，且元素个数相同"""
lst = [(1,2,3),[4,5,6],{7,8,9}]


# ### dict 字典类型的强制转换
"""
要求：必须是等长的二级容器，并且里面的元素个数是2个；
外层是列表，元组，集合，里层是列表或者元组的等长二级容器
"""

# 1.外层是列表，里层是列表或元组
lst = [["a",1], ("b",2)]
dic = dict(lst)
print(dic, type(dic))

# 2.外层是元组，里层是列表或元组
tup = (["a",1], ["b",2])
dic = dict(tup)
print(dic, type(dic))

# 3.外层是集合，里层是元组
setvar = {("a",1), ("b",2)}
dic = dict(setvar)
print(dic, type(dic))

# 例1：外层是列表/元组，里层放集合
"""可以实现，不推荐使用，因为达不到想要的目的，集合无序，不推荐使用"""
lst = [["a",1], {"b","250"}]
dic = dict(lst)
print(dic, type(dic))

# 例2：外层是列表/元组，里层放字符串
lst = ["a1", "a2"]
# lst = ["a11", "a22"]	error
dic = dict(lst)
print(dic)









