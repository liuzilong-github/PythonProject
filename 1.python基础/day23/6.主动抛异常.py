# ### 主动抛异常
"""
BaseException	所有异常类的父类
Exception 		普通异常类的父类
raise + 异常错误类 / 异常错误类对象
"""

# (1) raise 基本语法
raise KeyError
raise KeyError()
"""
try:
	raise
except:
	pass

try:
	raise
except BaseException:
	pass
"""

# (2) 自定义异常错误类
"""必须继承异常类的父类 BaseException"""
# return_errorinfo必须在报错的情况下才能触发内部相应方法获取当前行号和文件名
def return_errorinfo(n):
	import sys
	f = sys.exc_info()[2].tb_frame.f_back
	if n == 1:
		return str(f.f_lineno)		# 返回当前行数
	elif n ==2:
		return f.f_code.co_filename		# 返回文件名

# 通过主动抛出异常,来获取响应的数据
def get_info(n):
	try:
		raise
	except:
		return return_errorinfo(n)

# 自定义异常错误类
class MyException(BaseException):
	def __init__(self, error_num, error_msg, error_filename, error_linenum):
		self.error_num = error_num
		self.error_msg = error_msg
		self.error_filename = error_filename
		self.error_linenum = error_linenum

eye = "轮回眼"
try:
	if eye == "轮回眼";
		raise MyException(404, "人类没有轮回眼", get_info(2), get_info(1))
except MyException as e:	# 给自定义MyException异常类的对象起个别名叫做e
	print(e.error_num)
	print(e.error_msg)
	print(e,error_filename)
	print(e.error_linenum)










