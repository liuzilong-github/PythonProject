# ### UDP协议 客户端
import socket

# 1.创建udp对象
sk = socket.socket(type=socket.SOCK_DGRAM)

# 2.收发数据的逻辑
# 发送数据
msg = "你喜欢我吗~"
# sendto(二进制字节流, ip端口号)
sk.sendto(msg.encode(), ("127.0.0.1", 9000))

# 接收数据
msg, addr = sk.recvfrom(1024)
print(msg.decode())
print(addr)

# 3.关闭连接
sk.close()