# ### 文件校验
"""
mode = "r"	fp.read(3) 3个字符
mode = "rb" fp.read(3) 3个字节
"""
import hashlib
import os
# 1.针对于小文件进行校验
def check_md5(filename):
	hs = hashlib.md5()
	with open(filename, mode="rb") as fp:
		hs.update(fp.read())
		# return fp.read()	仅适用于小文件
	return hs.hexdigest()

res1 = check_md5("lianxi1.py")
res2 = check_md5("lianxi2.py")
print(res1 == res2)

# 2.针对大文件进行校验
"""
updata 可以分批次进行加密 等价于一次性加密的结果
"""
# update的使用
strvar = "今天是周五,明天自习"
hs = hashlib.md5()
hs.update(strvar.encode())
res1 = hs.hexdigest()
print(res1)

strvar2 = ",周一上午考试,小人射击+计算器"
hs.update(strvar2.encode())
res2 = hs.hexdigest()
print(res2)	# 0163aa435c2eea52fac354ba7e6c84da

strvar = "今天是周五,明天自习,周一上午考试,小人射击+计算器"
hs2 = hashlib.md5()
hs2.update(strvar.encode())
print(hs2.hexdigest())	# 0163aa435c2eea52fac354ba7e6c84da

# 方法一
def check_md5(filename):
	hs = hashlib.md5()
	with open(filename, mode="rb") as fp:
		while True:
			# 最多读取5个字节
			content = fp.read(5)
			# 判断读取的字节如果是空,终止循环
			if content:
				hs.update(content)
			else:
				break
		return hs.hexdigest()

res1 = check_md5("lianxi1.py")
res2 = check_md5("lianxi2.py")
print(res1, res2)

# 方法二
def check_md5(filename):
	hs = hashlib.md5()
	filesize = os.path.getsize(filename)
	print(filesize)
	with open(filename, mode="rb") as fp:
		# filesize 如果为空,循环终止
		while filesize:
			content = fp.read(100)
			hs.update(content)
			# 减去实际读取的长度
			filesize -= len(content)

		return hs.hexdigest()

res1 = check_md5("lianxi1.py")
res2 = check_md5("lianxi2.py")
print(res1, res2)















