# ### json序列化/反序列化模块
import json
"""
json格式的数据,所有的编程语言都能识别,本身是字符串
类型有要求: int float bool str list tuple dict None

json   主要应用于传输数据,序列化成字符串
pickle 主要用于存储数据,序列化成二进制字节流
"""

# json 基本用法
# json => dumps 和 loads
"""
ensure_ascii=False 显示中文
sort_keys=True 按键排序 
"""
dic = {"name":"梁新宇","sex":"野味","age":22,"family":["爸爸","妈妈","姐姐"]}
res = json.dumps(dic,ensure_ascii=False,sort_keys=True)
print(res, type(res))

dic = json.loads(res)
print(dic, type(dic))


# json => dump 和 load
with open("lianxi3.json",mode="w",encoding="utf-8") as fp:
	json.dump(dic, fp, ensure_ascii=False)
with open("lianxi3.json",mode="r",encoding="utf-8") as fp:
	json.load(fp)
print(dic, type(dic))


# ### json 和 pickle 之间的区别
# 1.json
# json 可以连续dump数据,但不能连续load数据,是一次性获取所有内容进行反序列化
dic1 = {"a":1,"b":2}
dic2 = {"c":3,"d":4}
with open("lianxi4.json",mode="w",encoding="utf-8") as fp:
	json.dump(dic1, fp)
	fp.write("\n")
	json.dump(dic1, fp)
	fp.write("\n")

# 不能连续load,是一次性获取所有数据 error
"""
with open("lianxi4.json",mode="r",encoding="utf-8") as fp:
	dic = json.load(fp)
"""

# 解决办法 loads(分开读取)
with open("lianxi4.json",mode="r",encoding="utf-8") as fp:
	for i in range(fp):
		dic = json.loads(i)
		print(dic, type(dic))

# 2.pickle
import pickle
# pickle => dump 和 load
# pickle 可以连续dump数据,也可以连续load数据
with open("lianxi5.pkl",mode="wb") as fp:
	pickle.dump(dic1, fp)
	pickle.dump(dic2, fp)
	pickle.dump(dic1, fp)
	pickle.dump(dic2, fp)

# 方法一
with open("lianxi5.pkl",mode="rb") as fp:
	dic1 = pickle.load(fp)
	dic2 = pickle.load(fp)
	print(dic1)
	print(dic2)

# 方法二
"""
try ... except ...
把有可能报错的代码放到try代码块中,如果出现异常执行except分支,来抑制报错
"""
# 一次性拿出来所有load出来的文件数据
try:
	with open("lianxi5.pkl",mode="rb") as fp:
		while True:
			dic = pickle.load(fp)
			print(dic)
except:
	pass

"""
# json 和 pickle 两个模块的区别:
(1) json序列化之后的数据类型是身str,所有编程语言都能识别
	但是仅限于(int,float,bool,str,list,tuple,dict,None)
	json不能连续load,只能一次性拿出来所有数据
(2) pickle序列化之后的数据类型是bytes,用于数据存储
	所有数据类型都可以转化,但仅限于python之间的数据传输
	pickle可以连续load,多套数据放到同一个文件中
"""












