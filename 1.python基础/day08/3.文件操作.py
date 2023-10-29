# ### 文件操作
"""
语法:
fp = open(文件,模式,编码集)
fp => 文件的io对象(文件句柄)
i => input	输入
o => output	输出

fp.read()	读取文件内容
fp.write()	写入文件的内容
"""

# 1.文件的写入操作
# (1)打开文件
fp = open("测试1.txt",mode='w',encoding='utf-8')	# 打开冰箱
# (2)写入内容
fp.write("把大象怼进去")	# 把大象怼进去
# (3)关闭文件
fp.close()	# 把冰箱门关上

# 2.文件的读取操作
# (1)打开文件
fp = open("测试1.txt",mode='r',encoding='utf-8')
# (2)读取内容
res = fp.read()
# (3)关闭文件
fp.close()
print(res)


# 3.文件存储二进制字节流
"""
二进制字节流:用于传输数据或者存储数据的一种数据格式
b"abc"	b开头的字节流要求数据只能是ascii编码中的字符,不能是中文

# 将字符串和字节流(Byte流)类型进行转换(参数写成转化的字符编码格式)
	encode() 编码 将字符串转化为字节流(Byte流)
	decode() 解码 将Bytes流转化为字符串
"""
data = b"abc"
data = "中文".encode("utf-8")
print(data,type(data))
res = data.decode("utf-8")
print(res,type(res))

# utf-8下 一个中文占用3个字节
data = "中文".encode("utf-8")
# 计算字节总大小
print(len(data))

# 把"中"字这个字节流进行反解恢复成原来的字符"中"
res = b"\xe4\xb8\xad".decode()
print(res)

# 4.文件存储二进制字节流
"""
如果存储的是二进制字节流,指定模式wb,不要指定encoding编码集,否则报错
"""
fp = open("测试2.txt",mode="wb")
strvar = "红鲤鱼绿鲤鱼与驴".encode("utf-8")
fp.write(strvar)
fp.close()

# 5.文件读取二进制的字节流
fp = open("测试2.txt",mode="rb")
res = fp.read()
fp.close()
print(res)
print(res.decode())

# 6.复制文件
"""
所有的图片,音频,视频都需要通过二进制字节流来进行存储传输

先把原文件的二进制字节流独取出来
相对路径找集合.png		相对于当前3.py这个文件
fp = open("集合.png",mode="rb")
绝对路径找集合.png		从最底层一级一级往上找
"""
fp = open(r"/Users/liuzilong/Documents/个人/PythonProject/day08.png",mode="rb")
res = fp.read()
fp.close()
# 计算文件中的字节个数 => 文件大小
print(len(res))

# 在把二进制字节流写入到另一个文件中,相当于复制
fp = open("集合2.png",mode="wb")
fp.write(res)
fp.close()









