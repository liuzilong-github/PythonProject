# ### socket 客户端
import socket

# 1.创建一个socket对象
sk = socket.socket()

# 2.与服务器建立连接
sk.connect( ("172.0.0.1", 9000) )

# 3.收发数据的逻辑
"""
发送的数据类型是二进制字节流
b开头的字符串是二进制字节流格式,要求字符类型必须是ascii编码
"""
# 发送数据
sk.send("今天我们学习网络编程".encode())

# 接收数据
res = sk.recv(1024)
print(res.decode())

# 4.关闭连接
sk.close()
