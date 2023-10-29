# ### 信号量 Semaphore (线程)

"""同一时间对多个线程上多把锁"""
from threading import Thread, Semaphore
import time, random

def func(i, sem):
	time.sleep(random.uniform(0.1, 0.7))
	# with语法自动实现上锁+解锁
	with lock:
		print("我在电影院拉屎 ... 我是{}号".format(i))

if __name__ == "__main__":
	sem = Semaphore(5)
	for i in range(30):
		Thread(target=func, args=(i, sem)).start()
	print(1)

"""
创建线程是异步的,
上锁的过程会导致程序变成同步;
"""