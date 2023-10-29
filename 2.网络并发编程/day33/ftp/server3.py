import hashlib
import socketserver
import json
import os
import struct

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

	@classmethod
	def login(cls, opt_dic):
		# 打开文件检测账号密码是否一致,如果成功直接返回,终止函数
		with open(userinfo, mode="r", encoding="utf-8") as fp:
			for line in fp:
				username, password = line.strip().split(":")
				if username == opt_dic["user"] and password == cls.md5(opt_dic["user"], opt_dic["passwd"]):
					return {"result": True, "info": "登录成功"}

		return {"result": False, "info": "登录失败"}

	@classmethod
	def myexit(cls, opt_dic):
		return {"result": "myexit"}


class FTPServer(socketserver.BaseRequestHandler):
	def handle(self):
		while True:
			opt_dic = self.myrecv()
			# {'user': 'wangwen', 'passwd': '111', 'operate': 'register'}
			print(opt_dic)
			# 判断Auth类中是否含有register成员
			if hasattr(Auth, opt_dic["operate"]):
				# 简写: res = getattr(Auth,"register")(opt_dic)
				# 反射方法
				func = getattr(Auth, opt_dic["operate"])
				# print(register) # <bound method Auth.register of <class '__main__.Auth'>>
				res = func(opt_dic)		# 执行方法
				if res["result"] == "myexit":
					# 终止当前这个线程和客户端的连接
					return
				self.mysend(res)	# 发送状态

				if res["result"]:
					while True:
						opt_dic = self.myrecv()
						# 如果接收的数据是myexit,直接退出,终止链接
						if opt_dic["operate"] == "myexit":
							return
						# 通过download方法进行下载
						if hasattr(self, opt_dic["operate"]):
							# download()	upload()
							getattr(self, opt_dic["operate"])(opt_dic)
			else:
				dic = {"result": False, "info": "没有该操作"}
				# 发送状态
				self.mysend(dic)

	def myrecv(self):
		# 字节流
		opt_bytes = self.request.recv(1024)
		# 字典
		opt_dic = json.loads(opt_bytes.decode())
		return opt_dic

	def mysend(self, send_info, sign=False):
		# 转换字节流
		send_info = json.dumps(send_info).encode()
		if sign == True:
			# 计算大小(文件的大小就是字节的个数)
			res = struct.pack("i", len(send_info))
			self.request.send(res)
		self.request.send(send_info)

	def download(self, opt_dic):
		# {'operate': 'download', 'filename': 'studey_info.mp4'}
		print(opt_dic)
		# 获取文件名
		filename = opt_dic["filename"]
		# 要下载的文件绝对路径
		file_abs = os.path.join(base_path, "video", filename)
		# print(file_abs) # /mnt/hgfs/python32_gx/day33/ftp/video/studey_info.mp4
		# 判断文件是否存在,存在的情况下发数据
		if os.path.exists(file_abs):
			# 1.告诉用户,文件存在,可以操作
			dic = {"result": True, "info": "文件可以下载"}
			self.mysend(dic, sign=True)
			# 2.把对应的文件名和文件大小发过去
			"""# ***额外增加功能 , 如果文件不存在 , 执行else分支 , 在文件存在的情况下发送数据 ***"""
			# 文件的大小
			filesize = os.path.getsize(file_abs)
			dic = {"filename": filename, "filesize": filesize}
			self.mysend(dic, sign=True)
			# 3.真实文件内容发送
			with open(file_abs, mode="rb") as fp:
				while filesize:
					content = fp.read(1024)
					self.request.send(content)
					filesize -= len(content)
			print("服务端传输完毕~")
		else:
			# 增加额外功能
			dic = {"result": True, "info": "文件不存在"}
			self.mysend(dic, sign=True)


ftpserver = socketserver.ThreadingTCPServer(("127.0.0.1", 9003), FTPServer)
ftpserver.serve_forever()









