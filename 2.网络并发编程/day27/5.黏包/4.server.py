# ### 服务端
import socket
import time
import struct

"""
黏包现象:
	(1)发送端,数据小,时间间隔短,造成黏包
	(2)接收端,没有及时接受数据,可能把多次发送的数据当成一条截取.
"""

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind(("127.0.0.1", 9001))
sk.listen()
conn, addr = sk.accept()

# 收发数据的逻辑
strver = input("[服务端]请输入您要发送的数据>>>")
msg = strver.encode()
length = len(msg)
res = struct.pack("i", length)

# 第一次发送数据(数据长度)
sk.send(res)

# 第二次发送数据(真实数据)
sk.send(msg)

# 第三次发送数据(真实数据)
sk.send(b"world,hello")

conn.close()
sk.close()