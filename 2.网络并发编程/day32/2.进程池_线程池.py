# ### 进程池和线程池
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os, time, random

# 获取的是电脑的逻辑处理器
# print(os.cpu_count())

"""多条进程提前开辟,可触发多cpu的并行效果"""
# (1) 进程池 ProcessPoolExecutor
'''
def func(i):
	# print(i)
	time.sleep(random.uniform(0.1, 0.8))
	print("任务执行中 ... start ... 进程号{}".format(os.getpid()), i)
	print("任务执行中 ... end ... 进程号{}".format(os.getpid()), i)
	return i

if __name__ == "__main__":
	lst = []
	# (1) 创建进程池对象
	"""默认参数是 系统最大的逻辑核心数 4"""
	p = ProcessPoolExecutor()

	# (2) 异步提交任务
	"""submit(任务, 参数1, 参数2 ...)"""
	"""默认如果一个进程短时间内可以完成更多的任务,进程池就不会使用更多的进程来辅助完成,可以节省系统资源的损耗"""
	for i in range(10):
		obj = p.submit(func, i)
		# print(obj)
		# print(obj.result())	 不要写在这里,会导致程序同步,内部有阻塞
		lst.append(obj)

	# (3) 获取当前任务的返回值
	for i in lst:
		print(i.result(), "<===获取返回值===>")

	# (4) shutdown 等待所有进程池里的进程执行完毕之后,再放行
	p.shutdown()

	print("进程池结束 ... ")
'''

# (2) ThreadPoolExecutor
'''
from threading import currentThread as ct
# from threading import current_thread as ct

def func(i):
	print("任务执行中 ... start ... 线程号{}".format(ct().ident), i)
	time.sleep(1)
	print("任务执行中 ... end ... 线程号{}".format(ct().ident), i)
	return ct().ident	# 线程号

if __name__ == "__main__":
	lst = []
	setvar = set()
	"""默认参数是 系统最大的逻辑核心数 4 * 5 = 20"""

	# (1) 创建线程池对象
	t = ThreadPoolExecutor()  # 20

	# (2) 异步提交任务
	"""默认如果一个线程短时间内可以完成更多的任务,线程池就不会使用更多的线程来辅助完成,可以节省系统资源的损耗"""
	for i in range(100):
		obj = t.submit(func, i)
		lst.append(obj)

	# (3) 获取当前任务的返回值
	for i in lst:
		setvar.add(i.result())

	# (4) shutdown 等待所有线程池里的线程执行完毕之后,再放行
	t.shutdown()
	print("主线程执行结束 ... ")
	print(setvar, len(setvar))
'''

# (3) 线程池map
from threading import currentThread as ct
from collections.abc import Iterator, Iterable

def func(i):
	time.sleep(random.uniform(0.1, 0.7))
	print("thread ... 线程号{}".format(ct().ident), i)
	return "*" * i

if __name__ == "__main__":
	t = ThreadPoolExecutor()
	it = t.map(func, range(100))
	# 返回的数据是迭代器
	print(isinstance(it, Iterator))

	# 协调子父线程,等待线程池中所有线程执行完毕之后,再放行
	t.shutdown()

	# 获取迭代器里面的返回值
	for i in it:
		print(i)

"""
总结:
无论是进程池还是线程池,都是由固定的进程数或者线程数来执行所有的任务
系统不会额外创建多余的进程或者线程来执行任务;
"""











