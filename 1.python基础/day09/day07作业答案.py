# ### 字符串相关练习
# 1.有变量name = "aleX leNb" 完成如下操作：
name = "aleX leNb"
# 移除 name 变量对应的值两边的空格,并输出处理结果
name.strip()
# 1)移除name变量左边的"al"并输出处理结果
name.lstrip("al")
# 2)移除name变量右面的"Nb",并输出处理结果
name.rstrip("Nb")
# 3)移除name变量开头的a与最后的"b",并输出处理结果
print(name[1:-1])
# 4)判断 name 变量是否以 "al" 开头,并输出结果
res = name.startswith("al")
print(res)
# 5)判断name变量是否以"Nb"结尾,并输出结果
res = name.endswith("Nb")
print(res)
# 6)将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果 
res = name.replace("l","p")
print(res)
# 7)将name变量对应的值中的第一个"l"替换成"p",并输出结果
res = name.replace("l","p",1)
print(res)
# 8)将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
res = name.split("l")
print(res) 
# 9)将name变量对应的值根据第一个"l"分割,并输出结果。 
# 字符串.split("分割的字符",分割的次数)
# 从左向右
print(name.split("l",1))
strvar = "you-can-you-up"
# 从右向左
print(strvar.rsplit("-",2))

# 10)将 name 变量对应的值变大写,并输出结果
name.upper()
# 11)将 name 变量对应的值变小写,并输出结果
name.lower()
# 12)将name变量对应的值首字母"a"大写,并输出结果
print(name.capitalize())
# 13)判断name变量对应的值字母"l"出现几次，并输出结果
print(name.count("l"))
# 14)如果判断name变量对应的值前四位"l"出现几次,并输出结果
print(name.count("l",0,4))
# 15)从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
print(name.index("N"))
# 16)从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1)输出结果
print(name.find("N"))
# 17)从name变量对应的值中找到"X le"对应的索引,并输出结果
print(name.find("X le"))
# 18)请输出 name 变量对应的值的第 2 个字符?
print(name[1] )
# 19)请输出 name 变量对应的值的前 3 个字符? 
print(name[:3])
# 20)请输出 name 变量对应的值的后 2 个字符?
print(name[-2:])
# 21)请输出 name 变量对应的值中 "e" 所在索引位置?
name = "aleX leNb"
print(name.find("e"))

print("<=====>")
for i in range(len(name)):
	if name[i] == "e":print(i)
		

# 2.实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:") 用户输入：5+9或3+ 9或5 + 6，然后进行分割再进行计算
"""
content = input("请输入内容:") 
print(content)
a,b = content.split("+")
print( a,b )
print(float(a.strip()) + float(b.strip()))
"""
# 3.升级题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+  13，然后进行分割再进行计算。
"""
content = input("请输入内容:") 
print(content)
lst = content.split("+")
print(lst)

total = 0
for i in lst:
	total += float(i.strip())
print(total)
"""

# 4.计算用户输入的内容中有几个整数.
# 如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla
"""
content = input("请输入内容：")
total = 0
for i in content:
	if i.isdecimal():
		total += 1
print(total)
"""

# 5.等待用户输入内容，是否包含敏感字符？
# 如果存在敏感字符提示“存在敏感字符请重新输入”，敏感字符：“粉嫩”、“铁锤”
# 方法一
'''
lst = ["粉嫩","铁锤"]
while True:
	# 重置sign标记
	sign = False
	content = input("请输入内容：")
	# print(content)
	"""
	if content.find("粉嫩") == -1 and content.find("铁锤") == -1:
		print("ok")
	else:
		print("not ok")
	"""
	# 小分铁嫩锤
	for i in lst:
		if i in content:	
			# 把sign标记设置成True
			sign = True
			break
	
	# 如果sign 这个标记是True,敏感,否则不敏感;
	if sign == True:
		print("存在敏感字符请重新输入")
	else:
		print("不存在敏感字符")
		break
'''
print("<====>")
# 方法二 (python特有) 额外的
"""如果在循环时,遇到break临时终止了循环,else这个分支不执行的
只有在正常全部循环执行了一遍之后,才会执行else分支
"""
"""
for i in range(3):
	if i == 2:
		break
else:
	print("ok")
"""


"""
lst = ["粉嫩","铁锤"]
# 触发break,不执行else , 不触发break , 执行else
while True:
	content = input("请输入内容：")
	for i in lst:
		# 但凡发现了敏感词汇,直接break,就不会走else分支了
		if i in content:
			print("是敏感词汇,请重新输入")
			# 终止内层的for循环
			break
	else:
		print("不是敏感词汇")
		# 终止外层while循环
		break
"""
			

	

# 6.制作趣味模板程序需求：等待用户输入名字、地点、爱好
# 拼装数据打印出：敬爱可亲的xxx，最喜欢在xxx地方xxx
while True:	

	name = input("请输入姓名:  按q可以退出~")
	if name.upper() == "Q":
		print("欢迎老铁下次来玩~")
		break
	
	place = input("请输入地点:")
	hobby = input("请输入爱好:")
	print("敬爱可亲的{}，最喜欢在{}地方{}".format(name,place,hobby))
	








