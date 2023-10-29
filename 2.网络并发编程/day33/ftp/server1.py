import hashlib
import socketserver
import json
import os

# print(__file__)
# print(os.getcwd())
# print(os.path.dirname(__file__))
base_path = os.path.dirname(__file__)
userinfo = os.path.join(base_path, "db", "userinfo.txt")


class Auth():
	@staticmethod
	def md5(usr, pwd):
		hs = hashlib.md5(usr.encode())
		hs.update(pwd.encode())
		return hs.hexdigest()

	@classmethod
	def register(cls, opt_dic):
		# {'user': 'wangwen', 'passwd': '111', 'operate': 'register'}
		# 1.检测注册用户名是否存在
		with open(userinfo, mode="r", encoding="utf-8") as fp:
			for line in fp:
				username = line.strip().split(":")[0]
				if username == opt_dic["user"]:
					# 失败结果
					return {"result": False, "info": "用户名已存在"}
		
		# 2.当前用户可以注册
		with open(userinfo, mode="a+", encoding="utf-8") as fp:
			strvar = "{}:{}\n".format(opt_dic["user"], cls.md5(opt_dic["user"], opt_dic["passwd"]))
			fp.write(strvar)

		# 成功失败
		return {"result": True, "info": "注册成功"}


class FTPServer(socketserver.BaseRequestHandler):
	def handle(self):
		opt_dic = self.myrecv()
		# {'user': 'wangwen', 'passwd': '111', 'operate': 'register'}
		print(opt_dic)
		# 判断Auth类中是否含有register成员
		if hasattr(Auth, "register"):
			# 简写: res = getattr(Auth,"register")(opt_dic)
			# 反射方法
			register = getattr(Auth, "register")
			print(register) # <bound method Auth.register of <class '__main__.Auth'>>
			res = register(opt_dic)		# 执行方法
			self.mysend(res)	# 发送状态

	def myrecv(self):
		# 字节流
		opt_bytes = self.request.recv(1024)
		# 字典
		opt_dic = json.loads(opt_bytes.decode())
		return opt_dic

	def mysend(self, send_info):
		send_info = json.dumps(send_info).encode()
		self.request.send(send_info)


ftpserver = socketserver.ThreadingTCPServer(("127.0.0.1", 9000), FTPServer)
ftpserver.serve_forever()














