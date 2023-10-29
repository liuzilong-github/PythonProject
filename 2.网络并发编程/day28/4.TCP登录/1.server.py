# ### 服务端
# from collections import Iterator,Iterable
import socketserver
import hashlib
import json


class MyServer(socketserver.BaseRequestHandler):

	# 默认没有登录
	sign = False

	def get_md5_code(self, usr, pwd):
		hs = hashlib.md5(usr.encode())
		hs.update(pwd.encode())
		return hs.hexdigest()

	def login(self):
		conn = self.request
		# 接受客户端发过来的数据,通过decode反解成字符串
		res = conn.recv(1024).decode()
		# 通过json把字符串转换成字典
		dic = json.loads(res)
		# {'username': 'caijingguan', 'password': '8888', 'operate': 'login'}
		print(dic)
		with open("userinfo.data", mode="r", encoding="utf-8") as fp:	# fp文件对象是迭代器,一行一行返回数据
			for i in fp:
				# 文件中解析出的用户名和密码
				usr, pwd = i.strip().split(":")
				if usr == dic["username"] and pwd == self.get_md5_code(dic["username"], dic["password"]):
					# 自定义返回的字典数据
					dic_msg = {"code": 1, "msg": "登录成功"}
					# 把字典 => 字符串
					json_str = json.dumps(dic_msg)
					# 把字符串 => 字节流,发送给客户端
					conn.send(json_str.encode())
					# 把sign标记从False改为True,代表登录成功
					self.sign = True
					break

			# 没有找到对应合法的用户名和密码,登录失败
			if self.sign == False:
				dic_msg = {"code": 0, "msg": "登录失败"}
				res = json.dumps(dic_msg).encode()
				conn.send(res)

	def handle(self):
		self.login()


server = socketserver.ThreadingTCPServer(("127.0.0.1", 9001), MyServer)
# 开启让一个端口绑定多个程序;	模块.类.属性 = True
socketserver.TCPServer.allow_reuse_address = True
server.serve_forever()

"""
作业:完成FTP服务器
(1)登录 (2)注册 (3)上传 (4)下载
"""




















