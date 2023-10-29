# ### 服务端
"""机器和机器之间的数据直接对接"""
import socketserver
import hmac
import os


class MyServer(socketserver.BaseRequestHandler):

	secret_key = "小兔子乖乖,把门开开"

	def auth(self):
		conn = self.request()
		# 创建一个随机的32位字节流
		msg = os.urandom(32)

		# 把字节流发送给客户端
		conn.send(msg)

		# 服务端进行数据校验
		hm = hmac.new(self.secret_key, msg)
		ser_res = hm.hexdigest()

		# 服务端接受客户端发送过来的数据结果
		cli_res = conn.recv(1024).decode()

		# 进行对比,如果OK,返回True,反之亦然
		return True if ser_res == cli_res else False

	def handle(self):
		if self.auth():
			self.request.send("True".encode())
		else:
			self.request.send("False".encode())

server = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MyServer)
# 开启让一个端口绑定多个程序;	模块.类.属性 = True
socketserver.TCPServer.allow_reuse_address = True
server.serve_forever()