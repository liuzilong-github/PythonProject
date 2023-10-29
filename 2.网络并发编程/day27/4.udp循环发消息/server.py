# ### udp 服务端
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1", 9000))

while True:
	# 接收数据
	msg, addr = sk.recvfrom(1024)
	print(msg.decode())
	print(addr)

	# 发送数据
	strvar = input("[服务端]请输入您要发送的数据>>>")
	sk.sendto(strvar.encode(), addr)

sk.close()
