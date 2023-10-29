import socketserver


class MySocket(socketserver.BaseRequestHandler):
	def handle(self):
		conn = self.request
		req_msg = conn.recv(1024).decode()
		print(req_msg)
		conn.send("I am OK~".encode())


server = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), MySocket)
server.serve_forever()