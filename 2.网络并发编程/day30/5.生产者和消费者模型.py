# ###生产者和消费者模型
"""
爬虫案列:
1号进程负责抓取其他多个网站中的关键字信息,正则匹配到队列中存储(mysql)
2号进程负责把队列中的内容拿取出来,将经过修饰后的内容布局到自己的网站中

1号进程可以理解为生产者
2号进程可以理解为消费者

从程序上来看
	生产者负责存储数据(put)
	消费者负责获取数据(get)

生产者和消费者比较理想的模型:
	生产多少,消费多少,生产数据的速度和消费数据的速度应该要相对一致
"""

# 1.基础版生产者消费者模型
"""问题: 当前模型,程序不能正常终止"""
"""
from multiprocessing import Process, Queue
import time, random
# 消费者模型
def consumer(q, name):
	while True:
		# 获取队列中的数据
		food = q.get()
		time.sleep(random.uniform(0.1, 1))
		print("{}吃了{}".format(name, food))

# 生产者模型
def producer(q, name, food):
	for i in range(5):
		time.sleep(random.uniform(0.1, 1))

		# 展示生产的数据
		print("{}生产了{}".format(name, food + str(i)))
		# 存储生产的数据在队列中
		q.put(food + str(i))

if __name__ == "__main__":
	q = Queue()
	p1 = Process(target=consumer, args=(q, "赵万里"))
	p2 = Process(target=producer, args=(q, "赵沈阳", "香蕉"))

	p1.start()
	p2.start()

	p2.join()
"""

# 2.优化模型
"""特点: 手动在队列的最后,加入标识None,终止消费者模型"""
"""
from multiprocessing import Process, Queue
import time, random
# 消费者模型
def consumer(q, name):
	while True:
		# 获取队列中的数据
		food = q.get()
		# 如果最后一次获取的数据时None, 代表队列已经没有更多的数据可以获取了,终止循环;
		if food is None:
			break
		time.sleep(random.uniform(0.1, 1))
		print("{}吃了{}".format(name, food))

# 生产者模型
def producer(q, name, food):
	for i in range(5):
		time.sleep(random.uniform(0.1, 1))

		# 展示生产的数据
		print("{}生产了{}".format(name, food + str(i)))
		# 存储生产的数据在队列中
		q.put(food + str(i))

if __name__ == "__main__":
	q = Queue()
	p1 = Process(target=consumer, args=(q, "赵万里"))
	p2 = Process(target=producer, args=(q, "赵沈阳", "香蕉"))

	p1.start()
	p2.start()

	p2.join()
	q.put(None)		# 香蕉0 香蕉1 香蕉2 香蕉3 香蕉4 None
"""

# 3.多个生产者和消费者
"""问题: 虽然可以解决问题,但是需要加入多个None,代码冗余"""
from multiprocessing import Process, Queue
import time, random
# 消费者模型
def consumer(q, name):
	while True:
		# 获取队列中的数据
		food = q.get()
		# 如果最后一次获取的数据是None,代表队列已经没有更多的数据可以获取了,终止循环
		if food is None:
			break
		time.sleep(random.uniform(0.1, 1))
		print("{}吃了{}".format(name, food))

# 生产者模型
def producer(q, name, food):
	for i in range(5):
		time.sleep(random.uniform(0.1, 1))

		# 展示生产的数据
		print("{}生产了{}".format(name, food + str(i)))
		# 存储生产的数据在队列中
		q.put(food + str(i))

if __name__ == "__main__":
	q = Queue()
	p1 = Process(target=consumer, args=(q, "赵万里"))
	p1_1 = Process(target=consumer, args=(q, "赵世超"))

	p2 = Process(targrt=producer, args=(q, "赵沈阳", "香蕉"))
	p2_2 = Process(target=producer, args=(q, "赵凤勇", "大蒜"))

	p1.start()
	p1_1.start()

	p2.start()
	p2_2.start()

	# 等待所有数据填充完毕
	p2.join()
	p2_2.join()

	# 把None关键字放在整个队列的最后,作为跳出消费者循环的标识符
	q.put(None)	 # 给第一个消费者加一个None,用来终止
	q.put(None)	 # 给第二个消费者加一个None,用来终止











