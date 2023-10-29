# ### 服务端
# from collections import Iterator,Iterable
import socketserver
import hashlib
import json
import os


class MyServer(socketserver.BaseRequestHandler):

	# 默认没有登录
	sign = False

	def get_md5_code(self, usr, pwd):
		hs = hashlib.md5(usr.encode())
		hs.update(pwd.encode())
		return hs.hexdigest()

	def login(self):
		conn = self.request
		req_dic = json.loads(conn.recv(1024).decode())
		with open("userinfo.data", mode="r", encoding="utf-8") as fp:
			for i in fp:
				usr, pwd = i.strip().split(":")
				if usr == req_dic["username"] and pwd == self.get_md5_code(req_dic["username"], req_dic["password"]):
					res_msg = {"code": 1, "msg": "登录成功"}
					conn.send(json.dumps(res_msg).encode())
					self.sign = True
					break
			else:
				res_msg = {"code": 0, "msg": "登录失败"}
				conn.send(json.dumps(res_msg).encode())

	def register(self):
		conn = self.request
		req_dic = json.loads(conn.recv(1024).decode())
		with open("userinfo.data", mode="r+", encoding="utf-8") as fp:
			for i in fp:
				usr, pwd = i.strip().split(":")
				if usr == req_dic["username"]:
					res_msg = {"code": 1, "msg": "该账号已注册"}
					conn.send(json.dumps(res_msg).encode())
					break
			else:
				userinfo = req_dic["username"] + ":" + self.get_md5_code(req_dic["username"], req_dic["password"])
				fp.seek(0, 2)
				fp.write("\n" + userinfo)
				res_msg = {"code": 0, "msg": "注册成功"}
				conn.send(json.dumps(res_msg).encode())

	def push_file(self):
		conn = self.request
		req_dic = json.loads(conn.recv(10240000).decode())
		with open(req_dic["file_name"], mode="w", encoding="utf-8") as fp:
			fp.write(req_dic["file_msg"])
			res_dic = {"code": 1, "msg": "上传成功"}
			conn.send(json.dumps(res_dic).encode())

	def pull_file(self):
		conn = self.request
		# req_dic = json.loads(conn.recv(1024).decode())
		file_path = conn.recv(1024).decode()
		print(file_path)
		# file_path = req_dic["pullfile"].replace("//", "/")
		with open(file_path, mode="r", encoding="utf-8") as fp:
			conn.send(fp.read().encode())
		if conn.recv(1024).decode() == "True":
			res_dic = {"code": 1, "msg": "下载成功"}
			conn.send(json.dumps(res_dic).encode())

	def handle(self):
		# self.login()
		# self.register()
		# self.push_file()
		self.pull_file()


server = socketserver.ThreadingTCPServer(("127.0.0.1", 9008), MyServer)
# 开启让一个端口绑定多个程序;	模块.类.属性 = True
socketserver.TCPServer.allow_reuse_address = True
server.serve_forever()

"""
作业:完成FTP服务器
(1)登录 (2)注册 (3)上传 (4)下载
"""






