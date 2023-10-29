# ### 协程例子
"""
# (1) spawn(函数,参数1,参数2,参数 .... ) 启动协程
# (2) join 阻塞,直到某个协程在任务执行完毕之后在放行
# (3) joinall 等待所有协程任务执行完毕之后放行;
	  g1.join()  g2.join() <=> gevent.joinall( [g1,g2..] )
# (4) value 获取协程任务中的返回值 g1.value  g2.value
"""
from gevent import monkey ; monkey.patch_all()
import gevent
import time
import requests

"""
def eat():
	print("eat1 开始吃 ... ")
	time.sleep(1)
	print("eat2 继续吃 ... ")
	return "吃完了"	
	
def play():
	print("play1 开始玩 ... ")
	time.sleep(1)
	print("play2 继续玩 ... ")
	return "玩完了"

# 创建协程对象g1
g1 = gevent.spawn(eat)
# 创建协程对象g2
g2 = gevent.spawn(play)
# 等待所有协程任务执行完毕之后放行
gevent.joinall( [g1,g2] )
print("主线程执行结束 ... ")
# 获取协程任务中的返回值
print(g1.value)
print(g2.value)
"""

# (2) 利用协程爬取数据
"""
HTTP 状态码
	200 ok
	400 bad request
	404 not found
"""

"""
import requests
response = requests.get("http://www.baidu.com")
# print(response ,type(response) )

# 获取状态码
print(response.status_code)
# 获取网页中的字符编码
res = response.apparent_encoding
print(res) # utf-8
# 设置编码集,防止乱码
response.encoding = res
# 获取网页内容
res = response.text
print(res)
"""


url_lst = [
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/",
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/",
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/",
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/",
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/",
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/",
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/",
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/",
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/",
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/",
	"http://www.baidu.com",
	"http://www.jd.com/",
	"http://www.taobao.com/",
	"http://www.amazon.cn/",
	"http://www.pinduoduo.com/",
	"http://www.4399.com/"
]


def get_url(url):
	response = requests.get(url)
	if response.status_code == 200:
		# print(response.text)
		pass
		
# (1) 正常爬取
"""
startime = time.time()
for i in url_lst:
	get_url(i)
endtime = time.time()
print(endtime-startime) # 12.648817539215088
"""
# (2) 用协程的方法爬取数据
lst = []

startime = time.time()
for i in url_lst:
	g = gevent.spawn(get_url , i)
	lst.append(g)
	
gevent.joinall( lst )
endtime = time.time()
print("主线程执行结束 ... 时间{}".format(endtime-startime)) # 1秒



















