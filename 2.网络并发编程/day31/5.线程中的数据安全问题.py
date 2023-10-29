# ### 线程中的数据安全问题

from threading import Thread, Lock
import time

n = 0

def func1(lock):
	global n

	lock.acquire()
	for i in range(100000):
		n += 1
	lock.release()

def func2(lock):
	global n
	# with语法可以简化上锁+解锁的操作,自动完成
	with lock:
		for i in range(100000):
			n -= 1

if __name__ == "__main__":
	lst = []
	lock = Lock()

	starttime = time.time()
	for i in range(10):
		t1 = Thread(target=func1, args=(lock,))
		t1.start()

		t2 = Thread(target=func2, args=(lock,))
		t2.start()

		lst.append(t1)
		lst.appennd(t2)

	for i in lst:
		i.join()
	# print(lst, len(lst))
	endtime = time.time()
	print("主线程执行结束... 当前n结果为{}, 用时{}".format(n, endtime-starttime))