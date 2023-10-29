# ### 收集参数
"""
(1) 普通收集形参:专门用来收集那些多余的没人要的普通实参
				收集之后,会把多余的实参打包成一个元组
				参数头上1个星星
	def func(*args):
		pass
	args => arguments
"""
def func(a,b,c,*args):
	print(a,b,c)	# 1 2 3
	print(args)		# (4,5,6)

func(1,2,3,4,5,6)

# 任意个数值的累加和
def mysum(*args):
	total = 0
	for i in args:
		total += i
	print(total)

mysum(1,2,3,4,5,66,10,100)


"""
(2) 关键字收集形参:专门用来收集那些多余的没人要的关键字实参
				 收集之后,会把多余关键字实参打包成一个字典
				 参数头上有2个星星
	def func(**kwargs):
		pass
	kwargs => keyword arguments
"""
def func(a,b,c,**keargs):
	print(a,b,c)
	print(kwargs)

func(c=1,a=3,b=10,f=100,e=200,z=12)

# 拼接任意个数值变成字符串
"""
班长:赵万里
班花:马春配
划水群众:赵沈阳,里胡玲,刘子涛
"""
def func(**kwargs):
	strvar1 = ""
	strvar2 = ""
	# 定义职位信息
	dic = {"monitor":"班长","classflower":"班花"}
	print(kwargs)
	# 共5次循环
	for k,v in kwargs.items():
		if k in dic:
			# 将2次循环的结果通过+=拼接在一起
			strvar1 += dic[k] + ":" + v + "\n"
		else:
			# 将3次循环的结果通过+=拼接在一起
			strvar2 += v + " , "
	print(strvar1.strip())
	print("划水群众",strvar2.strip(" , "))

	"""
	# print(k,v)
	monitor 赵万里
	classflower 马春陪
	water1 赵沈阳
	water2 李虎凌
	water3 刘子涛

	{'monitor': '赵万里', 'classflower': '马春陪', 'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	"""
func(monitor="赵万里",classflower="马春陪",water1="赵沈阳",water2="李虎凌",water3="刘子涛")






























