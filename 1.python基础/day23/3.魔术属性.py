# ### 魔术属性

class Man():
	pass

class Woman():
	pass

class Sasuke(Man, Woman):
	"""
	描述: 佐助这个的天生属性,技能
	成员属性: __eye skin
	成员方法: skylight __moonread
	"""
	__eay = "血轮眼=>万花筒=>轮回眼"

	skin = "白色"

	def skylight(self, myfunc):
		print("使用天照,一团黑色的火焰,恐怖如斯")
		res = myfunc.__name__
		print(res, type(res))

	def __moonread(self):
		print("使用月读,让敌人进入到幻术空间,被施法者掌控")

obj = Sasuke()
# __dict__获取对象或者类的内部成员结构
dic = Sasuke.__dict__
dic = obj.__dict__
print(dic)

# __doc__ 获取对象或类的内部文档
print(Sasuke.__doc__)
print(obj.__doc__)

# __name__ 获取类名函数名
def func():
	print("佩恩出场时,使用一手地爆天星,惊艳四座,点燃所有观众")

obj.skylight(func)

# __class__ 获取当前对象所属的类
print(obj.__class__)

# __bases__ 获取一个类直接继承的所有父类,返回元组
print(Sasuke__bases)









