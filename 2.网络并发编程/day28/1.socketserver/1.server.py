# ### 服务端
"""
socketserver的提出,是为了允许在tcp协议下进行并发操作
"""
import socketserver


class MyServer(socketserver.BaseRequestHandler):
	def handle(self):
		print("handle这个方法被触发了 ...")

# ThreadingTCPServer( ip端口号, 自定义的类)
server = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MyServer)
# 调用内部相关函数
server.serve_forever()