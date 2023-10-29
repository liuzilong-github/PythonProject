import socket
import json
import struct
import os

sk = socket.socket()
sk.connect(("127.0.0.1", 9003))


# 定义接收数据的方法
def myrecv(info_len=1024, sign=False):
	if sign == True:
		info_len = sk.recv(4)
		info_len = struct.unpack("i", info_len)[0]
	info = sk.recv(info_len).decode()
	dic = json.loads(info)
	return dic

# 处理收发数据的逻辑
def auth(opt):
	usr = input("username: >>>").strip()
	pwd = input("password: >>>").strip()
	dic = {"user": usr, "passwd": pwd, "operate": opt}
	str_dic = json.dumps(dic)

	# 发送数据
	sk.send(str_dic.encode())

	# 接收数据
	# info = sk.recv(1024).decode()
	# dic = json.loads(info)
	# return dic
	return myrecv()

def login():
	res = auth("login")
	return res

def register():
	res = auth("register")
	return res

def myexit():
	opt_dic = {"operate": "myexit"}
	sk.send(json.dumps(opt_dic).encode())
	exit("欢迎下次再来")

def download():
	operate_dict = {
		"operate": "download",
		"filename": "studey_info.mp4"
	}
	# 把要下载的请求发送给服务端
	sk.send(json.dumps(operate_dict).encode("utf-8"))
	# (1) 接收服务端返回的消息
	res = myrecv(sign=True)
	print(res)
	# {'result': True, 'info': '文件可以下载'}
	# print(res)
	if res["result"]:
		# 给用户创建个文件夹
		try:
			os.mkdir("mydownload")
		except:
			pass
		# (2) 接收文件大小和文件名
		dic = myrecv(sign=True)
		print(dic)

		# (3) 接收文件中的内容
		# {'filename': 'studey_info.mp4', 'filesize': 72274155}
		with open("./mydownload/" + dic["filename"], mode="wb") as fp:
			while dic["filesize"]:
				content = sk.recv(1024)
				fp.write(content)
				dic["filesize"] -= len(content)
		print("客户端下载完毕 ...")
	else:
		# 额外附加功能
		print("文件不存在,不能下载")


# 1.注册 2.登录 3.退出
operate_lst1 = [("注册", register), ("登录", login), ("退出", myexit)]
operate_lst2 = [("下载", download), ("退出", myexit)]
"""
(1, ('注册', <function register at 0x7ff1427faa60>))
(2, ('登录', <function login at 0x7ff1427fa9d8>))
(3, ('退出', <function myexit at 0x7ff1427faae8>))
"""

def main(operate_lst):
	for i, tup in enumerate(operate_lst, start=1):
		# 展示界面
		print(i, tup[0])
	# 提供操作
	num = int(input("请输入您要执行的选项").strip())
	print(num)
	# operate_lst[num-1][1] => register/login/myexit
	res = operate_lst[num-1][1]()
	return res


while True:
	# 开启第一套操作界面
	res = main(operate_lst1)
	print(res)	# {'result': True, 'info': '登录成功'}
	if res["result"]:
		while True:
			res = main(operate_lst2)

sk.close()











