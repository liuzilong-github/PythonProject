# ### socket 服务端
"""
一收一发是一对,不匹配会导致数据异常
send 发送
recv 接收
"""
import socket

# 1.创建一个socket对象
sk = socket.socket()

# 一个端口绑定多个程序(仅在测试时使用)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2.在网络中注册该主机(绑定对应的ip和端口号)
"""
默认本地ip: 127.0.0.1 => localhost
"""
sk.bind( ("127.0.0.1", 9000) )

# 3.开启监听
sk.listen()

# 4.三次握手
conn, addr = sk.accept()

# 5.首发数据的逻辑
# 接收数据
"""一次最多接收1024个字节"""
res = conn.recv(1024)
print(res)
print(res.decode())

# 发送数据
conn.send("好好学习,天天向上".encode())

# 6.四次挥手
conn.close()

# 7.退还端口
sk.close()
