# ### 使用类自定义线程
from threading import Thread
import os, time

# (1) 必须继承父类Thread,来自定义线程类
"""
class MyThread(Thread):

	def __init__(self, name):
		# 手动调用父类的构造方法
		supper().__init__()
		# 自定义当前类需要传递的参数
		self.name = name

	def run(self):
		print("当前的进程号是: {}, name={}".format(os.getpid(), self.name))

if __name__ == "__main__":
	t = MyThread()
	t.start()
	print("当前的进程号是: {}".format(os.getpid()))
"""

# ### 线程中的相关属性
"""
线程.is_alive()		检测线程是否仍然存在
线程.setName()		设置线程名字
线程.getName()		获取线程名字
1.currentThread().ident	 查看线程id号
2.enumerate()		返回目前正在运行的线程列表
3.activeCount()		返回目前正在运行的线程数量
"""

"""
def func():
	time.sleep(1)

if __name__ == "__main__":
	t = Thread(target=func)
	t.start()
	# 检测线程是否仍然存在
	print(t.is_alive())
	# 获取线程名字
	print(t.getName())
	# 设置线程名字
	t.setName("抓API接口")
	print(t.getName())
"""


from threading import currentThread
from threading import enumerate
from threading import activeCount

def func():
	time.sleep(0.1)
	print("当前子线程号id是: {},进程号是: {}".format(currentThread().ident, os.getpid()))

if __name__ == "__main__":
	t = Thread(target=func)
	t.start()
	print("当前子线程号id是: {},进程号是: {}".format(currentThread().ident, os.getpid()))

	for i in range(5):
		t = Thread(target=func)
		t.start()
	# 返回目前正在运行的线程列表
	lst = enumerate()
	print(lst, len(lst))
	# 返回目前正在运行的线程数量(了解)
	print(activeCount())









