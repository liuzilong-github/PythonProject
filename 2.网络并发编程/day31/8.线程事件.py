# ### 事件 Event
from threading import Thread, Event
import time, random

"""
wait	: 动态加阻塞(True => 放行, False => 阻塞)
is_set	: 获取内部成员属性值是True 还是 False
set  	: 把False => True
clear	: 把True => False
"""

# (1) 基本语法
"""
e = Event()
print(e.is_set())
e.set()
print(e.is_set())
e.wait()
e.clear()
# 最多阻塞三秒,放行
e.wait(3)
print("代码执行中 ... ")
"""

# (2) 模拟链接远程数据库
"""最多连接三次,如果三次都连接不上,直接报错"""

def check(e):
	print("目前正在检测您的账号和密码 ... ")
	# 模拟延迟的场景
	time.sleep(random.randrange(1, 7))
	# 把成员属性值从False => True
	e.set()

def connect(e):
	sign = False
	for i in range(1, 4):
		# 最多阻塞一秒
		e.wait(1)
		if e.is_set():
			print("数据库连接成功 ... ")
			sign = True
			break
		else:
			print("尝试连接数据库第{}次失败了 ... ".format(i))

	# 三次都不成功,报错
	if sign == False:
		# 主动抛出异常(超时错误)
		raise TimeoutError

# if __name__ == "__main__":
e = Event()
t1 = Thread(target=check, args=(e,))
t1.start()

t2 = Thread(target=connect, args=(e,))
t2.start()








