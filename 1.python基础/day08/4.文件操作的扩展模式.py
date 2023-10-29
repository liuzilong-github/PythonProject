# ### 文件操作的扩展模式
"""
# utf-8编码格式下 默认一个中文三个字节 一个英文或符号 占用一个字节
	# read()	功能:读取字符的个数(里面的参数代表字符个数)
		注意:从当前光标往右读
	# seek()	功能:调整指针的位置(里面的参数代表字节个数)
		seek(0)		把光标移动到文件的开头
		seek(0,2)	把光标移动到文件的末尾
	# tell()	功能:当前光标左侧所有的字节数(返回字节数)
"""

# 1.r+ 先读后写
"""
fp = open("测试3.txt",mode="r+",encoding="utf-8")
# 先读
res = fp.read()
# 在写
fp.write("ab")
# 在读
fp.seek(0)	# 通过seek吧光标移动到开头
print(fp.read())
fp.close()
"""

# 2.r+ 先写后读
"""
fp = open("测试3.txt",mode="r+",encoding="utf-8")
# 移动光标到最后,否则r模式下,原字符会被覆盖
fp.seek(0,2)
# 先写
fp.write("cd")
# 把光标移动到文件的开头
fp.seek(0)
# 在读
res = fp.read()
print(res)
fp.close()
"""

# 3.w+可读可写,清空重写(默认可以创建新的文件)
"""
fp = open("测试4.txt",mode="w+",encoding="utf-8")
fp.write("abc")
fp.seek(0)
print(fp.read())
fp.close()
"""

# 4.a+可读可写,追加写入(默认可以创建新的文件)
"""
fp = open("测试5.txt",mode="a+",encoding="utf-8")
fp.write("def")
# 读内容
fp.seek(0)
print(fp.read())
fp.close()
"""

# 5.r+和a+的区别
"""
r+模式基于当前光标所在位置进行写入覆盖
a+模式会强制把光标放到文件末尾进行追加写入
"""
"""
fp = open("测试5.txt",mode="r+",encoding="utf-8")
fp = open("测试5.txt",mode="a+",encoding="utf-8")
fp.seek(3)	# 从头数3个字节的位置
fp.write("zxc")	# 模式会强制把光标放到文件末尾进行追加写入
print(fp.read())
fp.close()
"""

# 6.seek,tell,read之间的使用
fp = open("测试5.txt",mode="r+",encoding="utf-8")
fp.seek(4)
# tell 当前光标左边所有内容的字节数
res = fp.tell()
print(res)

# 在r+模式下 read(2),代表读取2个字符 在rb模式下,read(2)代表读取2个字节
fp.read(2)	# 当前光标往右所有的所有字符内容
print(fp.tell())
fp.close()


# 7.注意点(seek在移动时,有可能移动到某个汉字的字符中间,导致原字节无法解析)
"""
fp = open("测试6.txt",mode="r+",encoding="utf-8")
fp.seek(3)
print(fp.read())
fp.close()

# print("你".encode())
# b'\xe4\xbd\xa0'
"""

# 8.with语法 自动实现文件关闭操作
# 方法一 读取二进制字节流
"""
with open("集合2.png",mode="rb") as fp:
	res = fp.read()
with open("集合3.png",mode="wb") as fp:
	fp.write(res)
"""

# 方法二 继续简化
with open("集合3.png",mode="rb") as fp1, open("集合4.png",mode="wb") as fp2:
	res = fp1.read()
	fp2.write(res)






























