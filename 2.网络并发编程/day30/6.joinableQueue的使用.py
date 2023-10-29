# ### JoinableQueue 队列
"""
put	存放
get	获取
task_done 计数器属性值-1
join 配合task_done来使用,阻塞

put	一次数据,队列的内置计数器属性值+1
get 一次数据,通过task_done让队列的内置计数器属性值-1
join: 会根据队列计数器的属性值来判断是否阻塞或者放行
	队列计数器属性是 等于0, 代码不阻塞放行
	队列计数器属性是 不等于0, 意味着代码阻塞
"""
from multiprocessing import JoinableQueue

jq = JoinableQueue()
jq.put("王通配")	# +1
jq.put("王伟")	# +2
print(jq.get())
print(jq.get())
# print(jq.get())	阻塞

jq.task_done()	# -1
jq.task_done()	# -1

jq.join()
print("代码执行结束 ... ")

# ### 2.使用JoinableQueue 改造生产者消费者模型
from multiprocessing import Process, JoinableQueue
import time, random
# 消费者模型
def consumer(jq, name):
	while True:
		# 获取队列中的数据
		food = jq.get()
		time.sleep(random.uniform(0.1, 1))
		print("{}吃了{}".format(name, food))
		# 让队列的内置计数器属性-1
		jq.task_done()

# 生产者模型
def producer(jq, name, food):
	for i in range(5):
		time.sleep(random.uniform(0.1, 1))

		# 展示生产的数据
		print("{}生产了{}".format(name, food + str(i)))
		# 存储生产的数据在队列中
		jq.put(food + str(i))

if __name__ == "__main__":
	jq = JoinableQueue()
	p1 = Process(target=consumer, args=(jq, "赵万里"))
	p2 = Process(target=producer, args=(jq, "赵沈阳", "香蕉"))

	p1.daemon = True

	p1.start()
	p2.start()

	p2.join()
	# 必须等待队列中的所有数据全部消费完毕,在执行
	jq.join()

	print("程序结束")








