# ### 服务端
import socket
import time

"""
黏包现象:
	(1)发送端,数据小,时间间隔短,造成黏包
	(2)接收端,没有及时接收数据,可能把多次发送的数据当成一条截取
"""

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(("127.0.0.1", 9001))
sk.listen()
conn, addr = sk.accept()

# 收发数据的逻辑
conn.send("word".encode())
time.sleep(1)
conn.send("hello".encode())

conn.close()
sk.close()
