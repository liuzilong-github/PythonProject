# ### 客户端
import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9000))

# 处理收发数据的逻辑

sk.close()