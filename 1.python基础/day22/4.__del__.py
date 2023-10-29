# ### __del__ 魔术方法(析构方法)
"""
	触发时机: 当对象被内存回收的时候自动触发[1.页面执行完毕回收所有变量 2.所有对象被del的时候]
	功能: 对象使用完毕后资源回收
	参数: 一个self接受对象
	返回值: 无
"""

# (1) 基本语法
class Lion():
	def __init__(self, name):
		self.name = name

	def __del__(self):
		print("析构方法被触发...")

# 触发方式一: 页面执行完毕回收所有变量
obj1 = Lion("辛巴")

# 触发方式二: 所有对象被del的时候
obj2 = obj1
obj3 = obj1
print(obj2, obj1, obj3)
print("<======start======>")
del obj1
del obj2
del obj3
print("<=====end======>")

# (2) 模拟文件操作
import os
class ReadFile();
	# 根据文件是否存在,创建对象
	def __new__(cls, filename):
		if os.path.exists(filename):
			return object.__new__(cls)
		else:
			print("抱歉, 没有这个文件")

	# 打开文件
	def __init__(self, filename):
		self.fp = open(filename, mode="r", encoding="utf-8")

	# 关闭文件
	def __del__(self):
		self.fp.close()

	# 读取文件
	def readcontent(self):
		return self.fp.read()

obj = ReadFile("1.多态.py")
print(obj.readcontent())












