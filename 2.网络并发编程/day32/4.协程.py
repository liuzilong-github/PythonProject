# ### 协程
"""
进程是资源分配的最小单位
线程是程序调度的最小单位
协程是线程实现的具体方式

总结:
在进程一定的情况下,开辟多个线程
在线程一定的情况下,开辟多个协程
以便提高最大的并行并发
"""

# (1) 用协程改写生产者消费者模型
def producer():
	for i in range(1000):
		yield i

def consumer(gen):
	for i in range(10):
		print(next(gen))

gen = producer()
consumer(gen)
print("<========>")
consumer(gen)
print("<========>")
consumer(gen)
print("<========>")

# (2) greenlet 协程的最早版本
from greenlet import greenlet
import time
"""switch 可以切换任务,但需要手动切换"""
def eat():
	print("eat1")
	g2.switch()
	time.sleep(3)
	print("eat2")

def play():
	print("play1")
	time.sleep(3)
	print("play2")
	g1.switch()

g1 = greenlet(eat)
g2 = greenlet(play)
g1.switch()

# (3) 升级到gevent版本
"""自动进行任务上的切换,但是不能识别阻塞"""
import gevent

def eat():
	print("eat1")
	gevent.sleep(3)
	# time.sleep(3)
	print("eat2")

def play():
	print("play1")
	gevent.sleep(3)
	# time.sleep(3)
	print("play2")

# 利用gevent.spawn创建携程对象g1
g1 = gevent.spawn(eat)
# 利用gevent.spawn创建携程对象g2
g2 = gevent.spawn(play)

# 如果不加join,主线程直接结束任务,不会默认等待协程任务
# 阻塞,必须等待g1任务完成之后再放行
g1.join()
# 阻塞,必须等待g2任务完成之后再放行
g2.join()

print("主线程执行结束 ... ")

# (4) 协程的终极版本
from gevent import monkey;monkey.patch_all()
"""引入猴子补丁,可以实现所有的阻塞全部自动识别"""

import time
import gevent

def eat():
	print("eat1")
	time.sleep(3)
	print("eat2")

def play():
	print("play1")
	time.sleep(3)
	print("play2")

# 利用gevent.spawn创建携程对象g1
g1 = gevent.spawn(eat)
# 利用gevent.spawn创建携程对象g2
g2 = gevent.spawn(play)

# 如果不加join,主线程直接结束任务,不会默认等待协程任务
# 阻塞,必须等待g1任务完成之后再放行
g1.join()
# 阻塞,必须等待g2任务完成之后再放行
g2.join()

print("主线程执行结束 ... ")


"""
# 拓展
# 分号: 利用分号可以把多行代码放在一行进行编写;
a = 1
b = 2
a = 1;b = 2
"""













