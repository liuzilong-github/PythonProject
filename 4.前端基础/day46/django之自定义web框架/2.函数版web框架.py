
import socket

server = socket.socket()

IP_PORT = ('127.0.0.1', 8001)
server.bind(IP_PORT)
server.listen()

def html():
	with open('beatfulpage.html', 'rb') as f:
		data = f.read()
	return data

def css():
	with open('xx.css', 'rb') as f:
		data = f.read()
	return data

def jpg():
	with open('1.jpg', 'rb') as f:
		data = f.read()
	return data

def js():
	with open('xx.js', 'rb') as f:
		data = f.read()
	return data

urlpatterns = [
	('/', html),
	('/xx.css', css),
	('/1.jpg', jpg),
	('/xx.js', js)
]


while True:
	conn, addr = server.accpet()
	from_client_msg = conn.recv(1024)
	from_browser_msg = from_client_msg.decode()
	print(from_browser_msg)
	path = from_browser_msg.split(' ')[1]

	for item in urlpatterns:
		if item[0] == path:
			data = item[1]()
			break

	conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
	conn.send(data)

	conn.close()

# server.close()