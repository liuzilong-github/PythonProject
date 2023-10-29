# ### 函数的嵌套
"""
函数嵌套的两个函数:
	包裹在外层的叫做外函数,内层的就是内函数
"""
def outer():
	# inner()
	def inner():
		print("我是inner函数")

"""
(1)内部函数可以直接在函数外部调用吗?		不行
inner()
(2)调用外部函数后,内部函数可以在函数外部调用吗?		不行
outer()
inner()
(3)内部函数可以在函数内部调用吗?		可以
outer()
(4)内部函数在函数内部调用时,是否有先后顺序?		有的
现定义在调用
在其它语言中有预加载机制,提前把函数驻留到内存中,然后再去编译脚本内容
python没有预加载函数的机制,只能先定义在调用
"""

# 外函数是outer		中间函数是inner	最里层是smaller, 调用smaller函数
def outer():
	def inner():
		def smaller():
			print("我是smaller函数")
		smaller()
	inner()
outer()


# LEGB原则
def outer():
	def inner():
		def smaller():
			print(a)
		smaller()
	inner()
outer()


"""
LEGB原则(就近找变量原则)
寻找变量的调用顺序采用LEGB原则(即就近原则)
B - Builtin(Python): python内置模块的命名空间(内建作用域)
G - Global(module): 函数外部所在的命名空间(全局作用域)
E - Enclosing function locals: 外部嵌套函数的作用域(嵌套作用域)
L - Local(function): 当前函数内的作用域(局部作用域)
依据就近原则,从下往上,从里向外,依次寻找
"""













