# ### 进程队列
from multiprocessing import Process, Queue
# 引入线程模块: 为了捕捉queue.Empty异常
import queue

# 1.基本语法
"""顺序: 先进先出,后进后出"""
# 创建进程队列
q = Queue()

# put()	 存放
q.put(1)
q.put(2)
q.put(3)

# get()  获取
"""在获取不到任何数据时,会出现阻塞"""
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

# get_nowait()	拿不到数据报异常
"""[windows] 效果正常		[linux] 不兼容"""
try:
	print(q.get_nowait())
	print(q.get_nowait())
	print(q.get_nowait())
	print(q.get_nowait())
except:	 # queue.Empty
	pass


# put_nowait()	非阻塞版本的put
# 设置当前队列最大长度为3(元素个数最多是3个)
"""在指定队列长度的情况下,如果塞入过多的数据,会导致阻塞"""
# q2 = Queue(3)
# q2.put(111)
# q2.put(222)
# q2.put(333)
# q2.put(444)

"""使用put_nowait 在队列已满的情况下,塞入数据会直接报错"""
q2 = Queue(3)
try:
	q2.put_nowait(111)
	q2.put_nowait(222)
	q2.put_nowait(333)
	q2.put_nowait(444)
except:
	pass

# 2.进程间的通信IPC
def func(q):
	# 2.子进程获取主进程存放的数据
	res = q.get()
	print(res, "<22>")
	# 3.子进程中存放数据
	q.put("刘一缝")

if __name__ == "__main__":
	q3 = Queue()
	p = Process(target=func, args=(q3,))
	p.start()

	# 1.主进程存入数据
	q3.put("找凤勇")

	# 为了等待子进程把数据存入队列后,主进程在获取数据
	p.join()

	# 4.主进程获取子进程存放的数据
	print(q3.get(), "<33>")












