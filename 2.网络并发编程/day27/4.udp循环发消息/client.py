# ### udp 客户端
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
	# 发送数据
	strvar = input("[客户端]请输入您要发送的内容>>>")
	sk.sendto(strvar.encode(), ("127.0.0.1", 9000))

	# 接收数据
	msg, addr = sk.recvfrom(1024)
	print(msg.decode())

sk.close()
