# ### nonlocal的使用(用来修改局部变量)
"""
nonlocal遵循LEGB原则
(1) 它会找当前空间上一层的变量进行修改
(2) 如果上一层空间没有,继续向上寻找
(3) 如果最后找不到,直接报错
"""

# (1) 它会找当前空间上一层的变量进行修改
def outer():
	a = 10
	def inner():
		nonlocal a
		a = 20
		print(a)
	inner()
	print(a)
outer()

# (2) 如果上一层空间没有,继续向上寻找
def outer():
	a = 20
	def inner():
		a = 15
		def smaller():
			nonlocal a
			a = 30
			print(a)
		smaller()
		print(a)
	inner()
	print(a)
outer()

# (3) 如果最后找不到,直接报错
"""
# nonlocal只能修改局部变量
a = 20
def outer():
	def inner():
		def smaller():
			nonlocal a
			a = 30
			print(a)
		smaller()
		print(a)
	inner()
	print(a)
outer()
"""

# (4) 不通过nonlocal 是否可以修改局部变量呢?	OK
def outer():
	lst = [1,2,3]
	def inner():
		lst[-1] = 3000
	inner()
	print(lst)
outer()







