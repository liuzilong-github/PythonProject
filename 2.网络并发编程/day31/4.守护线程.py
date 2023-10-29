# ### 守护线程: 等待所有线程全部执行完毕之后,自己在终止程序,守护所有线程
from threading import Thread
import time

def func1():
	while True:
		time.sleep(1)
		print("我是函数func1")

def func2():
	print("我是func2 start ... ")
	time.sleep(3)
	print("我是func2 end ... ")

def func3():
	print("我是func3 start ... ")
	time.sleep(3)
	print("我是func3 end ... ")

if __name__ == "__main__":
	t1 = Thread(target=func1)
	t2 = Thread(target=func2)
	t3 = Thread(target=func3)

	# 设置守护线程(启动前设置)
	t1.setDaemon(True)

	t1.start()
	t2.start()
	t3.start()

	print("主线程执行结束 ... ")