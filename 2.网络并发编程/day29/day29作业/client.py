import socket
from multiprocessing import Process


def tcp_process():
	sk = socket.socket()
	sk.connect(("127.0.0.1", 9000))
	sk.send("biubiubiu~".encode())
	res_msg = sk.recv(1024).decode()
	print(res_msg)
	sk.close()


if __name__ == "__main__":
	for i in range(1, 21):
		p = Process(target=tcp_process)
		p.start()

	print("模拟TCP并发场景结束~")
