# ### 列表相关练习
# 1.li = ["alex", "WuSir", "xboy", "oldboy"]
li = ["alex", "WuSir", "xboy", "oldboy"]
# 1)列表中追加元素"seven",并输出添加后的列表
li.append("seven")
# 2)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
li.insert(0,"Tony")
# 3)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li[1] = "Kelly"
# 4)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行
# 代码实现，不允许循环添加。
l2=[1,"a",3,4,"heart"]
li.extend(l2)
print(li)
# 5)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
s = "qwert"
li.extend(s)
print(li)
# 6)请删除列表中的元素"Tony",并输出添加后的列表
li.remove("Tony")
print(li)
# 7)请删除列表中的第2至4个元素，并输出删除元素后的列表
# del li[1:4]
# print(li)

# 8)删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
res = li.pop(1)
print(res)
print(li)

# 9)请将列表所有得元素反转，并输出反转后的列表
li.reverse()
print(li)
# 10)请计算出"alex"元素在列表li中出现的次数，并输出该次数。
print(li.count("xboy"))


# 2，写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5,"c"]
# 1)通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
print(li[:3])
# 2)通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
print(li[3:6])
# 3)通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
print(li[::2])
# 4)通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
print(li[1:-1:2])
# 5)通过对li列表的切片形成新的列表l5,l5 = ["c"]
print(li[-1:])
# 6)通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
print(li[-3::-2])


# 3,写代码，有如下列表，按照要求实现每一个功能。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 1)将列表lis中的"tt"变成大写。
print(lis[3][2][1][0].upper())
# 2)将列表中的数字3变成字符串"100"。
lis[3][2][1][1] = "100"
# 3)将列表中的字符串"1"变成数字101
# lis[3][2][1][-1] = 101
# print(lis)

lis[3][2][1].remove("1") # 先删
lis[3][2][1].append(101) # 在增
print(lis)


# 4,
li = ["alex", "eric", "rain"]   
# 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
# 一
print("_".join(li))

# 二
strvar = ""
for i in li:
	strvar += i + "_"
print(strvar.rstrip("_"))


# 5.利用for循环打印出下面列表的索引。
li = ["alex", "WuSir", "xboy", "oldboy"]
# 一
for i in range(len(li)):
	print(i)
# 二
for i in li:
	print(li.index(i))


# 6.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
a = []
for i in range(50):
	if i % 3 == 0 :
		a.append(i)
print(a)

# 7.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来
a = []
for i in range(100,9,-2):
	if i % 4 == 0:
		a.append(i)	
print(a)


# 8.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
li = ["xboy ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
lst2 = []
for j in li:
	if (j.strip().startswith("A") or j.strip().startswith("a")) and j.strip().endswith("c"):
		lst2.append(j.strip())
print(lst2)



# 9.敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# 将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到新列表中。
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
lst = []
"""
while True:
	strvar = input("请输入词汇:")
	lst.append(strvar.replace("苍老师","***").replace("东京热","***").replace("武藤兰","***").replace("波多野结衣","*****"))
	print(lst)
"""
"""
while True:
	strvar = input("请输入词汇:")
	
	# 按q退出
	if strvar.upper() == "Q":
		break
	
	# 过滤敏感词汇
	for i in li:
		if i in strvar:
			strvar = strvar.replace(i,len(i) * "*")
			
	# 把处理数据放到列表中
	lst.append(strvar)
	
print(lst)
"""
	

# 10.
print("<====>")
li = [1, 3, 4, "ALEx", [3, 7, "23AA",8, "XBoy"], 5,("A","b")]
# 循环打印列表中的每个元素,并转化为小写，遇到列表则再循环打印出它里面的元素。
for i in li:
	# 判断是否是字符串
	if isinstance(i,str):
		print(i.lower())
	# 判断是否是Number
	elif isinstance(i,(int,bool,complex,float)):
		print(i)
	# 判断是否是容器
	elif isinstance(i,(list,tuple,set,dict)):
		for j in i:
			# 判断容器中的元素是不是字符串
			if isinstance(j,str):
				print(j.lower())
			# 不是的话直接输出即可
			else:
				print(j)
		

# 11.tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# a.讲述元组的特性
# 可获取 , 不可修改 , 有序
# b.请问tu变量中的第一个元素 "alex" 是否可被修改？ 不可以
# c.请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
# 列表 能改 tu[1][2]["k2"].append("Seven")
# d.请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
# 元组,不行,






"""
扩展 : 
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
strvar = str(lis)
print(strvar,type(strvar))
strvar = strvar.replace("3","\'100\'")
lst = eval(strvar) # eval是把字符串当成代码执行
print(lst,type(lst))
"""









