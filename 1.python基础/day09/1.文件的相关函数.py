# ### 刷新缓冲区
"""
刷新缓冲区 flush
	# 当文件关闭的时候自动刷新缓冲区
	# 当整个程序运行结束的时候自动刷新缓冲区
	# 当缓冲区写满了 会自动刷新缓冲区
	# 手动刷新缓冲区
"""
"""
fp = open("ceshi1.txt",mode="a",encoding="utf-8")
fp.write("abc")

# 手动刷新缓冲区,直接把内容写入到文件
fp.flush()

while True:
	pass

fp.close()
"""

# ### 文件相关的函数
"""
fp这个对象本身是迭代器,可以把文件中的内容按照换行一行一行遍历出来"""
fp = open("ceshi1.txt",mode="r",encoding="utf-8")
# readable()	功能: 判断文件对象是否可读
print(fp.readable())
# writable()	功能: 判断文件对象是否可写
print(fp.writable())
# 遍历fp文件对象:
for i in fp:
	print(i)

# 1.readline()	功能:读取一行文件内容
with open("ceshi1.txt",mode="r",encoding="utf-8") as fp:
	res = fp.readline()
	print(res)
	res = fp.readline()
	print(res)
	res = fp.readline()
	print(res)
	res = fp.readline()
	print(res)
# (1)一次把所有内容都读取出来
with open("ceshi1.txt",mode="r",encoding="utf-8") as fp:
	# 先读取一行
	res = fp.readline()
	# 判断是否为空,不是空再循环
	while res:
		print(res)
		# 在读取一行,放到循环中判断
		res = fp.readline()
# (2)注意点:readline(读取的字符数)
with open("ceshi1.txt",mode="r",encoding="utf-8") as fp:
	"""
	读取的字符数量 > 实际当前行字符数量的时候 => 按照当前行读取
	读取的字符数量 < 实际当前行字符数量的时候 => 按照实际数量来读取
	"""
	res = fp.readline(300)
	print(res)

# 2.readlines()	功能:将文件中的内容按照换行读取到列表当中
lst_new = []
with open("ceshi1.txt",mode="r+",encoding="utf-8") as fp:
	lst = fp.readlines()
	for i in lst:
		lst_new.append(i.strip())
print(lst_new)

# 3.writelines()	功能:将内容是字符串的可迭代型数据写入文件中,参数:内容为字符串类型的可迭代数据
lst = ['床前明月光', '疑是地上霜', '举头望明月', '低头想家乡']
with open("ceshi2.txt",mode="w+",encoding="utf-8") as fp:
	fp.writelines(lst)

# ### 实现效果:加入换行效果,并且插入一句话,小伙真帅,插在低头想家乡前面
lst_new = []
# 先把内容插入到原列表中
lst.inster(-1, "小伙真帅呀")
# 循环原列表,把每一个元素拼接\n,放到新列表
for i in lst:
	lst_new.append(i + "\n")
print(lst_new)
with open("ceshi2.txt",mode="w+",encoding="utf-8") as fp:
	fp.writelines(lst_new)

# 注意点:内容必须是字符串,不能是整型
"""
lst = [1,2,3]
with open("ceshi2.txt",mode="w+",encoding="utf-8") as fp:
	fp.writelines(lst)
"""


# 4.truecate()	功能:把要截取的字符串提取出来,然后清空内容将提取的字符串重新写入文件中(字节)
with open("ceshi2.txt",mode="r+",encoding="utf-8") as fp:
	fp.truecate(3)

"""
seek(字节)
truecate(字节)
read(字符/字节)
readline(字符/字节)
"""












