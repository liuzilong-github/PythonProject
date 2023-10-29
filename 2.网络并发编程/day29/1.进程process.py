# ### 进程 process

import os, time
"""
# ps -aux 查看进程号
# ps -aux |grep 2784 过滤查找2784这个进程

# 强制杀死进程
kill -9 进程号

# 获取当前进程号
res = os.getpid()
print(res)

# 获取当前进程的父进程
res = os.getpid()
print(res)
"""

from multiprocessing import Process
# (1) 进程的使用
def func():
	# 1.子进程id:3561, 2.父进程id:3560
	print("1.子进程id:{}, 2.父进程id:{}".format(os.getpid()))

if __name__ == "__main__":
	# 创建子进程,返回进程对象
	p = Process(target=func)
	
	# 调用子进程
	p.start()

	# 3.主进程id:3560,4.父进程id:3327
	print("3.主进程id:{},4.父进程id:{}".format(os.getpid()))

# (2) 创建带有参数的进程
def func(n):
	time.sleep(1)
	for i in range(1, n+1):	  # 0 ~ n-1
		print(i)
		print("1.子进程id:{},2.父进程id:{}".format(os.getpid(), os.getppid()))

if __name__ == "__main__":
	n = 6
	# target=指定任务 args=参数元祖
	p = Process(target=func, agrs=(n,))
	p.start()

	for i in range(1, n+1):
		print("*" * i)

# (3) 进程之间的数据彼此隔离
total = 100
def func():
	global total
	total += 1
	print(total)

if __name__ == "__main__":
	p = Process(target=func)
	p.start()

	time.sleep(1)
	print(total)

# (4) 进程之间的异步性
"""
1.多个进程之间是异步的并发程序,因为cpu调度策略问题,不一定先执行哪一个任务
默认来看,主进程执行速度稍快于子进程,因为子进程创建时,要分配空间资源可能会阻塞
阻塞态:cpu会立刻切换任务,以让程序整体的速度效率最大化

2.默认主进程要等待所有的子进程执行结束之后,在统一关闭程序,释放资源
若不等待,子进程可能不停的在系统的后台占用cpu和内存资源形成僵尸进程
为了方便进程的管理,主进程默认等待子进程,在统一关闭程序
"""
def func(n):
	print("1.子进程id:{},2.父进程id:{}".format(os.getpid(), os.getpid(), n))

if __name__ == "__main__":
	for i in range(1, 11):
		p = Process(target=func, args=(i,))
		p.start()

	print("主进程执行结束了 ...", os.getpid())











