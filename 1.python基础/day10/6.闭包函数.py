# ### 闭包函数
"""
互相嵌套的两个函数,如过内函数使用了外函数的局部变量
并且外函数把内函数返回出来的过程,叫做闭包
里面的内函数叫做闭包函数

是不是闭包?
	1.内函数使用了外函数的局部变量
	2.外函数返回内函数
"""

# 1.基本语法形式
def zhaoshenyang_family():
	father = "马云"
	def hobby():
		print("我对钱没有一丝丝的兴趣,我不看重钱,这是我爸爸{}说的".format(father))
	return hobby

func = zhaoshenyang_family()
func()

tup = func.__closure__
print(tup[0].cell_contents)		# 马云
print(tup)

# 2.闭包的复杂形式
def zhaowanli_family():
	gege = "王思聪"
	didi = "鞋王,高振宁"
	money = 1000

	def gege_hobby():
		nonlocal money
		money -= 500
		print("我交朋友不在乎他有没有钱,反正都没有我有钱.我就喜欢交女朋友... 钱物还剩下{}".format(money))

	def didi_hobby():
		nonlocal money
		money -= 400
		print("家里有鞋柜,各式各样的奢侈鞋,一双大概20~30万,钱物还剩下{}".format(money))

	def bing_master():
		return [gege_hobby, didi_hobby]

	return bing_master

func = zhaowanli_family()
print(func)
lst = func()
print(lst)

# 获取哥哥函数
gege = lst[0]
gege()
# 获取弟弟函数
didi = lst[1]
didi()


# 3.使用__closure__, cell_contents 判断是不是闭包
"""
如果返回的元组中有数据说明是闭包,谁的生命周期被延长就打印谁
"""
tup = func.__closure__
print(tup)

# 先获取第一个单元格, cell_contents获取对象中的内容
func1 = tup[0].cell_contents
# 打印闭包函数didi_hobby中,声明周期被延长的属性
print(func1.__closure__[0].cell_contents)
func1()

# 再获取第二个单元格, cell_contents获取对象中的内容
func2 = tup[1].cell_contents
# 打印闭包函数didi_hobby中,声明周期被延长的属性
print(func2.__closure__[0].cell_contents)
func2()

























