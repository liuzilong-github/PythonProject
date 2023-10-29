# ### 字典的相关函数
dic = {}

# 增
# 1.普通方法(推荐)
dic["top"] = "369"
dic["middle"] = "左手"
dic["bottom"] = "杰克爱"
print(dic)

# 2.fromkeys 使用一组键和默认值创建字典
tup = ("a", "b", "c")
# fromkeys(盛放键的容器,默认值)
dic = {}.fromkeys(tup, None)
print(dic)

# 注意点(字典中的三个键默认指向的是同一个列表)
dic = {}.fromkeys(tup,[])
print(dic)
dic["a"].append(1)
print(dic)

# 改造
dic = {}
dic["top"] = []
dic["middle"] = []
dic["bottom"] = []
dic["top"].append("the boy")
print(dic)


# 删
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
# 1.pop()	通过键去删除键值对(若没有改键,可设置默认值,预防报错)
res = dic.pop("middle")
print(res)
print(dic)
# 可以给pop设置第二个参数值,以防止键不存在时报错
res = dic.pop("middle123454","该键不存在")
print(res)

# 2.popitem()	删除最后一个键值对
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
res = dic.popitem()
print(res)
print(dic)

# 3.clear()		清空字典
dic.clear()
print()


# 改
# 1.update()	批量更新(有该键就更新,没有该键就添加)

# 推荐使用
# 没有该键就添加
dic_new = {"jungle":"karsa","support":"宝蓝"}
dic = {'top': '369', 'middle': '左手', 'bottom': '杰克爱'}
dic.update(dic_new)
print(dic)

# 有该键就更新
dic_new = {"top":"the bug","support":"xboyww","xiaozhang":"王思聪"}
dic.update(dic_new)
print(dic)

# (了解)
dic.update(ww="王文", zl="张磊")
print(dic)


# 查
# 1.get()	通过键获取值(若没有该键可设置默认值,预防报错)
dic = {"top":"the bug","support":"xboyww","xiaozhang":"王思聪"}
# res = dic["top123"]
# get在获取字典键时,如果不存在,不会发生任何报错,返回的是None
res = dic.get("top123")
print(res)

# 可以再获取不到该键时,给与默认只提示
res = dic.get("top123","抱歉该键不存在")
print(res)


# 其他操作
# keys()	将字典的键组成新的可迭代对象
dic = {"top":"the bug","support":"xboyww","xiaozhang":"王思聪"}
res = dic.keys()
print(res, type(res))

# values()	将字典中的值组成新的可迭代对象 ***
res = dic.values()
print(res, type(res))

# items()	将字典的键值对凑成一个个元组,组成新的可迭代对象 ***
res = dic.items()
print(res, type(res))
# for循环遍历
for k,v in res:
	print(k,v) 











