# ### 锁 lock 互斥锁
from multiprocessing import Process, Manager, Lock
# 上锁和解锁是一对,连续上锁不解锁是死锁,只有在解锁的状态下,其他进程才有机会上锁

"""
# 创建一把锁
lock = Lock()
# 上锁
lock.acquire()
# lock.acquire()	# 连续上锁,造成了死锁现象;
print("我在渺渺炊烟... 你在焦急等待...")
# 解锁
lock.release()
"""



# ### 12306 抢票软件
import json, time, random

# 1.读写数据库当中的票数
def wr_info(sign, dic=None):
	if sign == "r":
		with open("ticket", mode="r", encoding="utf-8") as fp:
			dic = json.load(fp)
		return dic

	elif sign == "w":
		with open("ticket", mode="w", encoding="utf-8") as fp:
			json.dump(dic, fp)

# dic = wr_info("w", dic={"count": 0})
# print(dic, type(dic))

# 2.执行抢票的方法
def get_ticket(person):
	# 先获取数据库中实际的票数
	dic = wr_info("r")

	# 模拟一下网络延迟
	time.sleep(random.uniform(0.1, 0.5))

	# 判断票数
	if dic["count"] > 0:
		print("{}抢到票了".format(person))
		# 抢到票后,当前票数减1
		dic["count"] -= 1
		# 更新数据库中的票数
		wr_info("w", dic)
	else:
		print("{}没有抢到票哦".format(person))

# 3.对抢票和读写票数做统一的调用
def main(person, lock):
	# 查看剩余票数
	dic = wr_info("r")
	print("{}查看票数剩余: {}".format(person, dic["count"]))

	# 上锁
	lock.acquire()
	# 开始抢票
	get_ticket(person)
	# 解锁
	lock.release()


if __name__ == "__main__":
	lock = Lock()
	person_lst = ["梁新宇", "康裕康", "张保张", "于朝志", "薛宇健", "韩瑞瑞", "假摔先", "刘子涛", "黎明辉", "赵凤勇"]
	process = [Process(target=main, args=(i, lock)) for i in person_lst]
	for p in process:
		p.start()
	for p in process:
		p.join()


"""
创建进程,开始抢票是异步并发程序
直到开始抢票的时候,变成同步程序,
先抢到锁资源的先执行,后抢到锁资源的后执行;
按照顺序依次执行,是同步程序
"""












