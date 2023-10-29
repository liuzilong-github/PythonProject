# ### 1.同步主进程和子进程: join
"""必须等待当前的这个子进程执行结束之后,再去执行下面的代码;用来同步子父进程"""

form multiprocessing import Process
import time

# (1) join 的基本使用
def func():
	print("发送第一封邮件: 我的亲亲领导,你在吗?")

if __name__ == "__main__":
	p = Process(target=func)
	p.start()
	time.sleep(0.1)
	p.join()
	print("发送第二封邮件: 我想说,工资一个月给我涨到6万")

# (2) 多进程场景中的join
def func(i):
	time.sleep(1)
	print("发送第一封邮件{}: 我的亲亲领导,你在吗?".format(i))

if __name__ == "__main__":
	lst = []
	for i in range(1, 11):
		p = Process(target=func, args=(i,))
		p.start()
		# join写在里面会导致程序变成同步
		lst.append(p)

	# 把所有的进程对象都放在列表中,统一使用.join进行管理
	for i in lst:
		i.join()

	print("发送第二封邮件: 我想说,工资一个月给我涨到6万")


# ### 2.使用自定义进程类,创建进程
# (1) 基本语法
import os

class MyProcess(Process):
	def run(self):
		print("1.子进程id:{},2.父进程id:{}".format(os.getpid(), os.getpid()))

if __name__ == "__main__":
	p = MyProcess()
	p.start()

# (2) 带有参数的自定义进程类
class MyProcess(Process):

	def __init__(self, name):
		# 手动调用以下父类的构造方法,完成系统成员的初始化
		super().__init__()
		self.name = name

	def run(self):
		print("1.子进程id:{},2.父进程id:{}".format(os.getpid(), os.getpid()))
		print(self.name)


if __name__ = "__main__":
	p = MyProcess("我是参数")
	p.start()












