# ### Number 类型的强制转换（int float complex bool）

var1 = 13
var2 = 5.67
var3  = True
var4 = "123456"
var5 = "123abc"
var6 = 3+5j

# int 强制把数据转换成整型
"""int float bool 纯数字字符串"""
res = int(var2)
res = int(var3)		# True => 1
res = int(False)	# False => 0
res = int(var4)
# res = int(var5)	error
# res = int(var6)	error
print(res, type(res))

# float 强制把数据转换成浮点型
"""int float bool 纯数字字符串"""
res = float(var1)
res = float(var3)	# True => 1.0
res = float(False)	# False => 0.0
res = float(var4)
print(res, type(res))

# complex 强制把数据转换成复数
"""int float bool 纯数字字符串"""
res = complex(var1)
res = complex(var2)
res = complex(var3)		# True => 1 + 0j
res = complex(False)	# False => 0j
res = complex(var4)
print(res, type(res))

# bool 强制把数据转换成布尔型
"""布尔型可以强制转换一切数据类型"""
"""
布尔型为假的十种情况：
0  0.0  0j  False  ""  []  ()  set()  {}  None
"""
res = bool(var1)	# True
res = bool(var2)	# True
res = bool(var3)	# True
res = bool(var4)	# True
res = bool(var5)	# True
res = bool(var6)	# True
res = bool(None)	# False
print(res, type(res))

# 初始化变量时，不清楚用什么值，一律无脑写None
# None 代表空，代表什么也没有，一般用来初始化变量
a = None
b = None


"""
默认转换成当前数据类型的一个值
int()  float()  complex()  bools()
"""
res = bool()
print(res, type(res))






