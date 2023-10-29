# ### 服务端
"""
socketserver的提出,是为了允许在tcp协议下进行并发操作
"""
import socketserver


class MyServer(socketserver.BaseRequestHandler):

	# 第五步: 处理收发数据的逻辑写在handle中
	def handle(self):
		"""
		<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9001), raddr=('127.0.0.1', 33778)>
		('127.0.0.1', 33778)
		handle这个方法被触发了 .... 
		
		print(self.request) 	   # self.request <=> conn
		print(self.client_address) # self.client_address <=> addr
		print("handle这个方法被触发了 .... ")
		"""
		conn = self.request
		while True:
			res = conn.recv(1024)
			res2 = res.decode()
			print(res2)
			conn.send(res2.upper().encode())

# ThreadingTCPServer(ip端口号, 自定义的类)
server = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MyServer)
# 调用内部相关函数
server.serve_forever()