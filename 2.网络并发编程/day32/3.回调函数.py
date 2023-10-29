# ### 回调函数
"""
回调函数: 回头调用一下函数获取最后结果
微信支付宝付款成功后,获取付款金额
微信支付宝退款成功后,获取退款金额
一般用在获取最后的状态值时,使用回调
通过add_done_callback最后调用一下自定义的回调函数
"""

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import currentThread as ct
import os, time, random

"""进程任务"""
def func1(i):
	time.sleep(random.uniform(0.1, 0.9))
	print("进程任务执行中 ... start ... 进程号{}".format(os.getpid()), i)
	print("进程任务执行中 ... end ... 进程号{}".format(os.getpid), i)
	return i

def call_back1(obj):
	print("<==回调函数的进程号是:{}==>".format(os.getpid()))
	print(obj.result())

"""线程任务"""
def func2(i):
	time.sleep(random.uniform(0.1, 0.9))
	print("线程任务执行中 ... start ... 线程号{}".format(ct().ident), i)
	print("线程任务执行中 ... end ... 线程号{}".format(ct().ident), i)
	return i

def call_back2(obj):
	print("<==回调函数的线程号是:{}==>".format(ct().ident))
	print(obj.result())

if __name__ == "__main__":
	# (1) 进程池 结果: 进程池的回调函数由主进程执行
	p = ProcessPoolExecutor()	# os.cpu_count() => 4
	for i in range(1, 11):
		obj = p.submit(func1, i)
		# 使用add_done_callback在获取最后返回值的时候,可以异步并行
		obj.add_done_callback(call_back1)
		# 直接使用result获取返回值的时候,会变成同步程序,速度慢
		# obj.result()

	p.shutdown()
	print("主进程执行结束 ... 进程号:{}".format(os.getpid()))

	print("<===========================================>")

	# (2) 线程池 结果: 线程池的回调函数由子线程执行
	t = ThreadPoolExecutor()
	for i in range(1, 11):
		obj = t.submit(func2, i)
		# 使用add_done_callback在获取最后返回值的时候,可以异步并行
		obj.add_done_callback(call_back2)
		# 直接使用result获取返回值的时候,会变成同步程序,速度慢
		# obj.result()

	t.shutdown()
	print("主线程执行结束 ... 线程号{}".format(ct().ident))

"""
# 原型:
class Ceshi():
	def add_done_callback(self, func):
		print("系统执行操作1 ... ")
		print("系统执行操作2 ... ")
		# 回头调用一下
		func(self)

	def result(self):
		return 112233

def call_back(obj):
	print(obj.result())

obj = Ceshi()
obj.add_done_callback(call_back)
"""
























