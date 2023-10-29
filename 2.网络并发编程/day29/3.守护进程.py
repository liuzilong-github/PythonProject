# ### 守护进程
"""
守护进程守护的是主进程,当主进程所有代码执行完毕之后,立刻强制杀死守护进程
"""

from multiprocessing import Process
import time

# (1) 基本语法
def func():
	# time.sleep(1)
	print("strt... 当前子进程")
	print("end...  当前子进程")

if __name__ == "__main__":
	p = Process(target=func)
	# 在进程启动之前,设置守护进程
	p.daemon = True
	p.start()

	print("主进程执行结束 ...")

# (2) 多个子进程的守护场景
"""
默认主进程等待所有非守护进程,也就是子进程执行结束之后,在关闭程序,释放资源
守护进程只要在主进程代码执行结束时,就会自动关闭
"""
def func1():
	print("strt... func1 执行当前子进程")
	print("end...  func1 结束当前子进程")

def func2():
	count = 1
	while True:
		print("*" * count)
		time.sleep(1)
		count += 1

if __name__ == "__main__":
	p1 = Process(target=func1)
	p2 = Process(target=func2)

	# 把p2这个进程变成守护进程
	p2.daemon = True
	p1.start()
	p2.start()

	print("主进程执行结束 ...")

# (3) 守护进程用途: 监控报活
def alive():
	while True:
		print("3号服务器向总监控服务器发送报活信息: i am ok~")
		time.sleep(1)

def func():
	while True:
		try:
			print("3号服务器负责抗住3万用户量的并发访问...")
			time.sleep(3)

			# 主动抛出执行错误的异常,触发except分支
			raise RuntimeError

		except:
			print("3号服务器扛不住了.. 快来修理我..")
			break

if __name__ == "__main__":
	p1 = Process(target=alive)
	p2 = Process(target=func)

	p1.daemon = True
	p1.start()
	p2.start()

	# 必须等待p2这个子进程执行完毕之后,再放行主进程下面的代码
	# 下面主进程代码执行结束,立刻杀死守护进程,失去了报活功能;
	p2.join()

	print("主进程执行结束 ....")















