# ### pickle 序列化/反序列化模块

import pickle
"""
序列化:
	把不能够直接存储在文件中的数据变得可存储
反序列化:
	把存储在文件中的数据拿出来恢复成原来的数据类型

所有的数据类型都可以通过pickle模块进行序列化
"""

lst = [1,2,3]
# 错误案例,文件不能直接存储容器,文件中能存储字符串和字节流
"""
with open("lianxi1.txt",mode="w",encoding="utf-8") as fp:
	fp.write(lst)
"""

# dumps 把任意对象序列化成一个bytes
res = pickle.dumps(lst)
print(res, type(res))

# 函数可以序列化吗? => 可以
def func():
	print("我是func函数")
res = pickle.dumps(func)
print(res, type(res))

# 迭代器可以序列化吗? => 可以
it = iter(range(10))
res = pickle.dumps(it)
print(res, type(res))

# loads 把任意bytes反序列化成原来的数据
res2 = pickle.loads(res)
print(res2, type(res2))


# dump 把对象序列化后写入到file-like Object(即文件对象)
lst = [1,2,3]
with open("lianxi1.txt",mode="wb") as fp:
	pickle.dump(lst, fp)

# load 把file-like Object(即文件对象)中的内容拿出来,反序列化成原来的数据
with open("lianxi1.txt",mode="rb") as fp:
	pickle.load(fp)
print(res2, type(res2))


# dumps 和 loads 对文件进行写入读取字节流操作
# 写入字节流
with open("lianxi2.txt",mode="wb+") as fp:
	res1 = pickle.dumps(lst)
	fp.write(res1)

# 读取字节流
with open("lianxi2.txt",mode="rb") as fp:
	bytes_str = fp.read()
	res = pickle.loads(bytes_str)
print(res, type(res))














