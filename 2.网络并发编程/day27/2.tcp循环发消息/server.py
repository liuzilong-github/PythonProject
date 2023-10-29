# ### 服务端
import socket

# 1.创建socket对象
sk = socket.socket()

# 一个端口绑定多个程序(仅在测试时使用)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 2.在网络中注册该主机(绑定ip和端口号)
sk.bind(("127.0.0.1", 9000))

# 3.监听端口
sk.listen()

# 4.三次握手
# conn, addr = sk.accept()

# 5.收发数据的逻辑
"""
print(conn)
print(addr)
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9000), raddr=('127.0.0.1', 50176)>
('127.0.0.1', 50176)
"""
while True:
	conn, addr = sk.accept()
	while True:
		# 接收数据
		res = conn.recv(1024)
		print(res.decode())

		# 发送数据
		strvar = input("[服务端]请输入您要发送的数据>>>")
		conn.send(strvar.encode())

		# 退出
		if strvar == "q":
			break

	# 6.四次挥手
	conn.close()

# 7.退还端口
sk.close()



