
import socket
import time
from threading import Thread

server = socket.socket()

IP_PORT = ('127.0.0.1', 8001)
server.bind(IP_PORT)
server.listen()

def html(conn):
	now = str(time.time())
	with open('beatfulpage.html', 'r', encoding='utf-8') as f:
		data.f.read()
	data = data.replace("%xxoo%", now).endoe('utf-8')
	conn.send(data)
	conn.close()

def css(conn):
	with open('xx.css', 'rb') as f:
		data.f.read()
	conn.send(data)
	conn.close()

def jpg(conn):
	with open('1.jpg', 'rb') as f:
		data.f.read()
	conn.send(data)
	conn.close()

def js(conn):
	with open('xx.js', 'rb') as f:
		data.f.read()
	conn.send(data)
	conn.close()

def person(conn):
	with open('person.html', 'rb') as f:
		data.f.read()
	conn.send(data)
	conn.close()

urlpatterns = [
	('/', html),
	('/xx.css', css),
	('/1.jpg', jpg),
	('/xx.js', js),
	('/person', person),

]


while True:
	conn, addr = server.accpet()
	from_client_msg = conn.recv(1024)
	from_browser_msg = from_client_msg.decode()
	print(from_browser_msg)
	path = from_browser_msg.split(" ")[1]
	conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
	for item in urlpatterns:
		if item[0] == path:
			t = Thread(target=item[1], args=(conn,))
			t.start()
			data = item[1](conn)
			break

server.close()