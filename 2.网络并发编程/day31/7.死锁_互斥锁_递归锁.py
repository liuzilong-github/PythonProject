# ### 互斥锁 死锁 递归锁
from threading import Thread, Lock, RLock
import time

# (1) 语法上的死锁
"""语法上的死锁: 是连续上锁不解锁"""
"""
lock = Lock()
lock.acquire()
# lock.acquire()	error
print("代码执行中  ... 1")
lock.release()
lock.release()
"""

"""上两把完全不同的锁"""
lock1 = Lock()
lock2 = Lock()

lock1.acquire()
lock2.acquire()
print("代码执行中 ... 2")
lock2.release()
lock1.release()

# (2) 逻辑上的死锁
noodles_lock = Lock()
kuaizi_lock = Lock()

def eat1(name):
	noodles_lock.acquire()
	print("{}抢到面条了 ... ".format(name))
	kuaizi_lock.acquire()
	print("{}抢到筷子了 ... ".format(name))

	print("开始享受香菇青菜面 ... ")
	time.slepp(0.5)

	noodles_lock.release()
	print("{}吃完了,满意的放下了面条".format(name))
	kuaizi_lock.release()
	print("{}吃完了,满意的放下了筷子".format(name))

def eat2(name):
	kuaizi_lock.acquire()
	print("{}抢到筷子了 ... ".format(name))
	noodles_lock.acquire()
	print("{}抢到面条了 ... ".format(name))

	print("开始享受香菇青菜面 ... ")
	time.slepp(0.5)

	kuaizi_lock.release()
	print("{}吃完了,满意的放下了筷子".format(name))
	noodles_lock.release()
	print("{}吃完了,满意的放下了面条".format(name))

if __name__ == "__main__":
	lst1 = ["康裕康","张宇"]
	lst2 = ["张保张","赵沈阳"]
	for name in lst1:
		Thread(target=eat1, args=(name,)).start()

	for name in lst2:
		Thread(target=eat2, args=(name,)).start()

# 使用递归锁
"""
递归锁的提出专门用来解决死锁现象
用于快速解决线上项目死锁问题
即使连续上锁,使用递归锁后也形同虚设,因为递归锁的作用在于解锁
"""
# 基本语法
"""
rlock = RLock()
rlock.acquire()
rlock.acquire()
rlock.acquire()
rlock.acquire()
print("代码执行中 ... 3")
rlock.release()
rlock.release()
rlock.release()
rlock.release()
"""

"""
noodles_lock = Lock()
kuaizi_lock = Lock()

# 让noodles_lock和kuaizi_lock 都等于递归锁
noodles_lock = kuaizi_lock = RLock()

def eat1(name):
	noodles_lock.acquire()
	print("{}抢到面条了 ... ".format(name))
	kuaizi_lock.acquire()
	print("{}抢到筷子了 ... ".format(name))

	print("开始享受香菇青菜面 ... ")
	time.slepp(0.5)

	noodles_lock.release()
	print("{}吃完了,满意的放下了面条".format(name))
	kuaizi_lock.release()
	print("{}吃完了,满意的放下了筷子".format(name))

def eat2(name):
	kuaizi_lock.acquire()
	print("{}抢到筷子了 ... ".format(name))
	noodles_lock.acquire()
	print("{}抢到面条了 ... ".format(name))

	print("开始享受香菇青菜面 ... ")
	time.slepp(0.5)

	kuaizi_lock.release()
	print("{}吃完了,满意的放下了筷子".format(name))
	noodles_lock.release()
	print("{}吃完了,满意的放下了面条".format(name))

if __name__ == "__main__":
	lst1 = ["康裕康","张宇"]
	lst2 = ["张保张","赵沈阳"]
	for name in lst1:
		Thread(target=eat1, args=(name,)).start()

	for name in lst2:
		Thread(target=eat2, args=(name,)).start()
"""

# (4) 尽量使用一把锁解决问题(少用嵌套锁,容易逻辑死锁)
lock = Lock()

def eat1(name):
	lock.acquire()
	print("{}抢到面条了 ... ".format(name))
	print("{}抢到筷子了 ... ".format(name))

	print("开始享受香菇青菜面 ... ")
	time.slepp(0.5)

	print("{}吃完了,满意的放下了面条".format(name))
	print("{}吃完了,满意的放下了筷子".format(name))
	lock.release()

def eat2(name):
	lock.acquire()
	print("{}抢到筷子了 ... ".format(name))
	print("{}抢到面条了 ... ".format(name))

	print("开始享受香菇青菜面 ... ")
	time.slepp(0.5)

	print("{}吃完了,满意的放下了筷子".format(name))
	print("{}吃完了,满意的放下了面条".format(name))
	lock.release()

if __name__ == "__main__":
	lst1 = ["康裕康","张宇"]
	lst2 = ["张保张","赵沈阳"]
	for name in lst1:
		Thread(target=eat1, args=(name,)).start()

	for name in lst2:
		Thread(target=eat2, args=(name,)).start()




















