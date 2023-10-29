
import socket
import time
from threading import Thread
from urls import urlpatterns

def run():
	server = socket.socket()

	IP_PORT = ('127.0.0.1', 8001)
	server.bind(IP_PORT)
	server.listen()

	while True:
		conn, addr = server.accept()
		from_client_msg = conn.recv(1024)
		from_browser_msg = from_client_msg.decode()
		print(from_browser_msg)
		path = from_browser_msg.split(' ')[1]
		conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
		for item in urlpatterns:
			if item[0] == path:
				t = Thread(target=item[1],args=(conn,))
				t.start()
				data = item[1](conn)
				break

# server.close()
