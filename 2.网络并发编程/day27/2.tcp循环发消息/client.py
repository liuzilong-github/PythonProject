# ### 客户端
import socket

# 1.创建socket对象
sk = socket.socket()

# 2.连接服务器
sk.connect(("127.0.0.1", 9000))

# 3.收发数据的逻辑
while True:
	# 发送数据
	strvar = input("[客户端]请输入您要发送的数据>>>")
	sk.send(strvar.encode())

	# 接收数据
	res = sk.recv(1024)
	if res == b"q":
		break
	print(res.decode())

# 4.关闭连接
sk.close()
