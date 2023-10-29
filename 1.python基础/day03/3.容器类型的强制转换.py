# ### 容器类型的强制转换（str list tuple set dict）

var1 = "hello，world"
var2 = [1,2,3]
var3 = (4,4,5)
var4 = {"陈璐","上朝气","刘子涛","合理"}
var5 = {"cl":"文质彬彬,斯文败类","szq":"学霸","lzt":"篮球少年","hl":"武大高手"}
var6 = 90
var7 = True

# str 强制转换成字符串
"""所有的数据类型都可以转换，在当前的数据类型两边套引号"""
res = str(var1)
res = str(var2)
res = str(var3)
res = str(var4)
res = str(var5)
res = str(var6)
res = str(var7)
print(res, type(res))
# repr 不转义字符原型化输出字符串
print(repr(res))


# list 强制转换成列表
"""
如果是字符串：把字符串中的每个元素单独拿出来，作为列表中的新元素
如果是字典：只保留字典中的键
如果是其他容器类型：就是单纯的在原数据类型的两边换上[]括号
"""
res = list(var1)
res = list(var3)
res = list(var4)
res = list(var5)	# 字典：只获取字典的键，忽略掉值
# res = list(var6)	error 只能是容器间的互转
print(res, type(res))


# tuple 强制转换成元组
"""
如果是字符串：把字符串中的每个元素单独拿出来，作为元组中的新元素
如果是字典：只保留字典中的键
如果是其他容器类型：就是单纯的在原数据类型的两边换上()括号
"""
res = tuple(var1)
res = tuple(var2)
res = tuple(var4)
res = tuple(var5)
print(res, type(res))


# set 强制转换成集合
"""
如果是字符串：把字符串中的每个元素单独拿出来，作为集合中的新元素
如果是字典：只保留字典中的键
如果是其他容器类型：就是单纯的在原数据类型的两边换上{}括号
"""
res = set(var1)
res = set(var2)
res = set(var3)
res = set(var5)
print(res, type(res))

# 过滤掉列表中所有重复的元素：
lst = [1,222,3,3,3,44,88,999,77,88,1]
# 先把列表转换成元组去重，然后再把去重后的元组转换为列表
res = set(lst)
res2 = list(res)
print(res2)



"""
默认不加任何值，转换成该数据类型的空值
str() list() tuple() set() dict()
"""
res = dict()
print(res)
print(type(res))







