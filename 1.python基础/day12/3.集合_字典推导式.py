# ### 集合推导式
"""
案例:
	满足年龄在18到21,存款大于等于5000,小于等于5500的人
	开卡格式为:尊贵VIP卡老x(姓氏),否则开卡格式为:抠脚大汉卡老x(姓氏)	
	把开卡的种类统计出来
"""
lst = [
    {"name":"赵沈阳","age":18,"money":3000},
    {"name":"赵万里","age":19,"money":5200},
    {"name":"赵蜂拥","age":20,"money":100000},
    {"name":"赵世超","age":21,"money":1000},
    {"name":"王志国","age":18,"money":5500},
    {"name":"王永飞","age":99,"money":5500}
]

setvar = set()
for i in lst:
	print(i)	# {'name': '赵沈阳', 'age': 18, 'money': 3000}
	if 18 <= i["age"] <= 21 and 5000 <= i["money"] <= 5500:
		res = "尊贵VIP卡老{}".format(i["name"][0])
	else:
		res = "抠脚大汉卡老{}".format(i["name"][0])
	setvar.add(res)
print(setvar)

# {三元运算符 + 推导式}
setvar = {"尊贵VIP卡老{}".format(i["name"][0]) if 18 <= i["age"] <= 21 and 5000 <= i["money"] <= 5500 else "抠脚大汉卡老{}".format(i["name"][0]) for i in lst}
print(setvar)



# ### 字典推导式
### 1.enumerate
"""
enumerate(iterable, [start=0])
功能:
	枚举,将索引号和iterable中的值,一个一个拿出来配对组成元组,通过迭代器返回
参数:
	iterable: 可迭代性数据(常用:迭代器,容器类型数据,可迭代对象range)
	start:可以选择开始索引号(默认从0开始索引)
返回值:
	迭代器
"""

# 基本语法
from collections import Iterator,Iterable
lst =["王文","吕洞宾","何仙姑","铁拐李","张国老","曹国舅","蓝采和","韩湘子"]
it = enumerate(lst)
it = enumerate(lst, start=100)
print(isinstance(it, Iterator))

# next
print(next(it))

# for + next (推荐,数据量较大时使用)
for i in range(3):
	print(next(it))

# for
for i in it:
	print(i)

# list强转迭代器
print(list(it))

# (1) 字典推导式 配合enumerate来实现
dic = {k:v for k,v in enumerate(lst,start=100)}
print(dic)
"""
(100, '王文')
(101, '吕洞宾')
(102, '何仙姑')
(103, '铁拐李')
(104, '张国老')
(105, '曹国舅')
(106, '蓝采和')
(107, '韩湘子')
"""


# ### 2.zip
"""
特点:
	按照索引配对
语法:
	zip(Iterable,Iterable,...)
功能:
	将多个Iterable中的值,一个一个拿出来配对组成元组,通过迭代器返回
	Iterable: 可迭代性数据(常用:迭代器,容器类型数据,可迭代对象range)
返回:
	迭代器
"""

# 基本语法
# lst1 = ["孙开启","王永飞","于朝志"]
# lst2 = ["薛宇健","韩瑞晓","上朝气"]
# lst3 = ["刘文博","历史园","张光旭"]

# 在索引下标同时存在时,才会进行配对,否则舍弃
lst1 = ["孙开启","王永飞","于朝志"]
lst2 = ["薛宇健","韩瑞晓"]
lst3 = ["刘文博"]

it = zip(lst1,lst2,lst3)
print(list(it))

# (1) 字典推导式 配合 zip使用
lst_key = ["ww","axd","yyt"]
lst_value = ["王维","安晓东","杨元涛"]

# ('ww', '王维'), ('axd', '安晓东'), ('yyt', '杨元涛')
dic = {k:v for k,v in zip(lst_key,lst_value)}
print(dic)

# (2) 使用dict强转迭代器,瞬间得到字典
dic = dict(zip(lst_key, lst_value))
print(dic)










