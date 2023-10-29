# ### 客户端
import socket
import time
import struct

sk = socket.socket()
sk.connect(("127.0.0.1", 9001))

time.sleep(2)

# 收发数据的逻辑
# 第一季接收数据(数据长度)
num = sk.recv(4)
tup = struct.unpack("i", num)
print(tup[0])

# 第二次接收数据(真实数据)
res = sk.recv(tup[0])
print(res.decode())

# 第三次接收数据(真实数据)
res = sk.recv(1024)
print(res.decode())

sk.close()