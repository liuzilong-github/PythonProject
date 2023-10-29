# ### 客户端
import socket
import json
import os
"""
pickle => 字节流(存储数据)
json   => 字符串(数据交互)
"""

sk = socket.socket()
sk.connect(("127.0.0.1", 9008))

# 处理收发数据的逻辑
def login():
	usr = input("请输入您的用户名:")
	pwd = input("请输入您的密码:")
	req_dic = {"username": usr, "password": pwd, "operate": "login"}
	sk.send(json.dumps(req_dic).encode())
	res_dic = json.loads(sk.recv(1024).decode())
	print(res_dic["msg"])

def register():
	usr = input("请输入您的用户名:")
	pwd = input("请输入您的密码:")
	req_dic = {"username": usr, "password": pwd, "operate": "register"}
	sk.send(json.dumps(req_dic).encode())
	res_dic = json.loads(sk.recv(1024).decode())
	print(res_dic["msg"])

def push_file():
	push_file_info = input("请输入您要上传的文件路径及文件名:")
	n_pushfile = push_file_info.replace("/", "//")
	file_path, file_name = os.path.split(n_pushfile)
	with open(push_file_info, mode="r", encoding="utf-8") as fp:
		file_msg = fp.read()
		req_dic = {"file_path": file_path, "file_name": file_name, "file_msg": file_msg}
		sk.send(json.dumps(req_dic).encode())
	res_dic = json.loads(sk.recv(1024).decode())
	print(res_dic["msg"])

def pull_file():
	pull_file_path = input("请输入您要下载的文件路径及文件名:")
	sk.send(pull_file_path.encode())
	file_path, file_name = os.path.split(pull_file_path)
	with open(file_name, mode="w", encoding="utf-8") as fp:
		file_msg = sk.recv(10240000).decode()
		fp.write(file_msg)
	sk.send("True".encode())
	res_dic = json.loads(sk.recv(1024).decode())
	print(res_dic["msg"])


# login()
# register()
# push_file()
pull_file()


sk.close()
