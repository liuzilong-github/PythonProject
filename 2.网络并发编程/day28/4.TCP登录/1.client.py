# ### 客户端
import socket
import json
"""
pickle => 字节流(存储数据)
json   => 字符串(数据交互)
"""

sk = socket.socket()
sk.connect(("127.0.0.1", 9000))

# 处理收发数据的逻辑
usr = input("请输入您的用户名:")
pwd = input("请输入您的密码:")
dic = {"username": usr, "password": pwd, "operate": "login"}

# 通过json变成字符串
res = json.dumps(dic)

# 转化成二进制字节流发送给服务端
sk.send(res.encode())

# 接受服务端响应的数据
res_str = sk.recv(1024).decode()

# 字符串转化成字典
dic = json.loads(res_str)
print(dic, type(dic))
print(dic["msg"])

sk.close()
