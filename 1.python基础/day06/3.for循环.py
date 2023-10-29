# ### for循环
# 遍历 循环 迭代, 把容器中的元素一个一个获取出来

# while 循环在遍历数据时的局限性
"""
lst = [1,2,3,4,5]
i = 0
while i < len(lst):
	print(lst[i])
	i += 1

setvar = {"a", "b", "c"}	# error
i = 0
while i < len(setvar):
	print(setvar[i])
	i += 1
"""

# for循环的基本语法
"""
Iterable 可迭代性数据: 1.容器类型数据 2.range对象 3.迭代器
for 变量 in Iterable:
	code1
"""

# 字符串
container = "北京和深圳温差大概20多度"
# 列表
container = [1,2,3,4,4,5]
# 元组
container = ("孙开洗","孙健","孙悟空")
# 集合
container = {"陈璐","曹静怡","王志国","邓鹏","合力"}
# 字典
container = {"cl":"风流倜傥","cjy":"拳击选手","wzg":"寻花问柳","dp":"帅气,祖国的栋梁","hl":"你是个好人"}

# 遍历数据
for i in container:
	print(i)

# 1.遍历不等长多级容器
container = [1,2,3,4,("嗄","234",{"马春配","李虎凌","刘子涛"})]
for i in container:
	# 判断当前元素是否是容器,如果是,进行二次遍历,如果不是,直接打印
	if isinstance(i, tuple):
		# ("嗄","234",{"马春配","李虎凌","刘子涛"})
		for j in i:
			# 判断当前元素是否是集合,如果是,进行三次遍历,如果不是,直接打印
			if isinstance(j, set):
				for k in j:
					print(k)
			else:
				print(j)
	# 打印数据
	else:
		print(i)


# 2.遍历不等长多级容器
container = [("刘玉波","历史源","张光旭"), ("上朝气","于朝志"),("韩瑞晓",)]
for i in container:
	for j in i:
		print(j)


# 3.遍历等长容器
container = [("马云","小马哥","马春配") , ["王健林","王思聪","王志国"],{"王宝强","马蓉","宋小宝"}]
for a,b,c in container:
	print(a,b,c)

# 变量的解包
a,b,c = "poi"
a,b = (1,2)
a,b = 1,2
a,b,c = [10,11,12]
a,b = {"林明辉","家率先"}
a,b = {"lmh":"林明辉","jsx":"家率先"}
a,b,c = ("马云","小马哥","马春配")
print(a,b,c)


# ### range对象
"""
range(开始值,结束值,步长)
取头舍尾,结束值本身获取不到,获取到它之前的那一个数据
"""

# range(一个值)
for i in range(5):	# 0 ~ 4
	print(i)

# range(两个值)
for i in range(3,8):	# 3 4 5 6 7
	print(i)

# range(三个值) 正向的从左到右
for i in range(1,11,3):	# 1 4 7 10
	print(i)

# range(三个值) 逆向的从右到左
for i in range(10,0,-1):	# 10 9 8 7 ... 1
	print(i)


# 总结:
"""
while 一般用于处理复杂的逻辑关系
for   一般用于迭代数据
部分情况下两个循环可以互相转换
"""

i = 1
while i <= 9:
	j = 1
	while j <= i:
		print("%d*%d=%2d" % (i,j,i*j), end='')
		j += 1
	print()
	i += 1

for i in range(1,10):
	for j in range(1,i+1):
		print("%d*%d=%2d" % (i,j,i*j), end='')
	print()

# 打印 1 ~ 5 跳过5
i = 1
while i <= 10:
	if i == 5:
		i += 1
		continue
	print(i)
	i += 1

for i in range(1,11):
	if i == 5:
		continue
	print(i)










