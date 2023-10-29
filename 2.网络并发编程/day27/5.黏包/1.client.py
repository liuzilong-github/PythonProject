# ### 客户端
import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1", 9001))

time.sleep(2)

# 收发数据的逻辑
res1 = sk.recv(1024)
print(res1.decode(), "<===1===>")
res2 = sk.recv(1024)
print(res2.decode(), "<===2===>")

sk.close()
