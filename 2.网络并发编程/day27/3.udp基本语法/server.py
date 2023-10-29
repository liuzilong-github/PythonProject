# ### UDP协议 服务端
import socket

# 1.创建udp对象
sk = socket.socket(type=socket.SOCK_DGRAM)

# 2.在网络中注册该主机(绑定ip和端口号)
sk.bind(("127.0.0.1", 9000))

# 3.收发数据的逻辑
"""
udp协议下,默认第一次只能接收数据(没有三次握手,不清楚对方的ip和端口号)
"""
# 接收数据
msg, addr = sk.recvfrom(1024)
print(msg.decode())
print(addr)

# 发送数据
sk.sendto("我喜欢你个锤子".encode(), addr)

# 4.关闭连接
sk.close()
