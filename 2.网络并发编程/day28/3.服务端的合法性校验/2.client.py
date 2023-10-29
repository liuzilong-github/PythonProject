# ### 客户端
"""机器和机器之间的数据直接对接"""
import socket
import hmac

sk = socket.socket()
sk.connect(("127.0.0.1", 9000))

def auth(secret_key):
	# 接受服务端发送过来的随机二进制字节流
	msg = sk.recv(32)

	# hmac.new(key(字节流), 要加密的内容(字节流))
	hm = hmac.new(secret_key.encode(), msg, digestmod="md5")

	# 返回的是具有固定32位长度的十六进制字符串
	cli_res = hm.hexdigest()

	# 把最后计算的结果发送给服务端进行校验
	sk.send(cli_res.encode())

	# 接受服务端给予的校验结果
	res = sk.recv(1024).decode()

	return res

# 处理收发数据的逻辑
secret_key = "不开不开就不开,老妈没回来"
# secret_key = "小兔儿乖乖,把门开开"
# 调用授权函数
res = auth(secret_key)

if res == "True":
	print("服务器校验通过")
else:
	print("服务器校验失败")

sk.close()
