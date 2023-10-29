# ### struct 模块使用
import struct

"""
pack	打包
	把任意长度的数字转换成具有固定4个字节长度的字节流
unpack	解包
	把4个字节长度的值恢复成原来的数字,返回元组
"""

# pack
# i => int	要转换的当前类型是整型
"""范围: -21亿~21亿左右,控制在1.8G之内"""
res = struct.pack("i", 999999998)
print(res, len(res))

res = struct.pack("i", 1111111119)
print(res, len(res))

res = struct.pack("i", 3)
print(res, len(res))

res = struct.pack("i", 2000000000)
print(res, len(res))

# unpack
# i => int	把对应的数据转换成整型
tup = struct.unpack("i", res)
print(tup)	# (2000000000,)
print(tup[0])


"""
解决黏包的场景:
	应用场景在实时通讯时,需要阅读此次发的消息是什么
不需要解决黏包的场景:
	下载或者上传文件的时候,最后要把包都结合在一起,黏包无所谓
"""