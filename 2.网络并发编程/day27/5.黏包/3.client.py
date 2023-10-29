# ### 客户端
import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1", 9001))

time.sleep(2)

# 收发数据的逻辑
# 第一步,先接收接下来要发送的数据的总大小
res = sk.recv(8)
num = int(res.decode())

# 第二步,再接收真实的数据
res1 = sk.recv(num)
print(res1.decode(), "<===1===>")
res2 = sk.recv(num)
print(res2.decode(), "<===2===>")

sk.close()