
import socket

service = socket.socket()

IP_PORT = ('127.0.0.1', 8081)
server.bind(IP_PORT)
server.listen()

while True:
	conn, addr = server.accept()
	from_client_msg = conn.recv(1024)
	from_browser_msg = from_client_msg.decode()
	path = from_browser_msg.split(' ')[1]

	if path == '/':
		with open('beatfulpage.html', 'rb') as f:
			data = f.read()
	elif path == '/1.jpg':
		with open('1.jpg', 'rb') as f:
			data = f.read()
	elif path == '/xx.css':
		with open('xx.css', 'rb') as f:
			data = f.read()
	elif path == './xx.js':
		with open('xx.js', 'rb') as f:
			data = f.read()

	conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
	conn.send(data)

	conn.close()

	