# ### 信号量 Semaphore 本质上就是锁,只不过是多个进程上多把锁,可以控制上锁的数量

"""Semaphore = lock + 数量"""
from multiprocessing import Semaphore, Process
import time, random

"""
# 同一时间允许多个进程上5把锁
sem = Semaphore(5)
# 上锁
sem.qcquire()
print("执行操作...")
# 解锁
sem.release()
"""

def singsong_ktv(person, sem):
	# 上锁
	sem.acquire()

	print("{}进入了唱吧ktv,正在唱歌~".format(person))
	# 唱一段时间
	time.sleep(random.randrange(4,8))
	print("{}离开了唱吧KVT,唱完了...".format(person))

	# 解锁
	sem.release()


if __name__ == "__main__":
	sem = Semaphore(5)
	person_lst = ["赵凤勇", "沈思雨", "赵万里", "张宇", "假率先", "孙杰龙", "陈璐", "王雨涵" , "杨元涛", "刘一凤"]
	process = [Process(target=singsong_ktv, args=(i, sem)) for i in person_lst]
	for p in process:
		p.start()
	for p in process:
		p.join()


"""
总结:
Semaphore 可以设置上锁的数量,同一时间上多把锁
创建进程时,是异步并发,执行任务时,是同步程序;
"""







