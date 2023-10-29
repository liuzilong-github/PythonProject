# ### 线程
"""
进程是资源分配的最小单元
线程是cpu执行调度的最小单元
"""

# (1) 一个进程里包含了多个线程,线程之间是一步并发
from threading import Thread
from multiprocessing import Process
import os, time, random

"""
def func(i):
	time.sleep(random.uniform(0.1, 0.9))
	print("当前进程号是: {}".format(os.getpid()), i)

if __name__ == "__main__":
	for i in range(10):
		t = Thread(target=func, args=(i,))
		t.start()

print(os.getpid())
"""

# (2) 并发的多进程和多线程之间,多线程的速度更快
# 多线程速度
def func(i):
	print("当前的进程号: {},参数是: {}".format(os.getpid(), i))

if __name__ == "__main__":
	lst = []
	starttime = time.time()
	for i in range(10000):
		t = Thread(target=func, args=(i,))
		t.start()
		lst.append(t)
	# print(lst)
	for i in lst:
		i.join()
	endtime = time.time()
	print("运行的时间是: {}".format(endtime - starttime))	 # 运行的时间是1.8805944919586182

# 多进程速度
if __name__ == "__main__":
	lst = []
	starttime = time.time()
	for i in range(10000:
		p = Process(target=func, args=(i,))
		p.start()
		lst.append(p)
	# print(lst)
	for i in lst:
		i.join()
	endtime = time.time()
	print("运行的时间是: {}".format(endtime - starttime))	 # 运行的时间是101.68004035949707

# (3) 多线程之间,数据共享
num = 100
lst = []
def func():
	global num
	num -= 1

for i in range(100):
	t = Thread(targrt=func)
	t.start()
	lst.append()

for i in lst:
	i.join()

print(num)











