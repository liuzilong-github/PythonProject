# 1.猜大小的游戏：
# 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。
"""
num = 66
str_num = input("请输入理想的数字")
num_new = int(str_num)
if num_new > num:
	print("猜测的结果大了")
elif num_new == num:
	print("显示猜测结果正确")
elif num_new < 66:
	print("则显示猜测的结果小了")
"""


# 2.输出 1-100 内的所有奇数
"""
i = 1
while i <= 100:
	if i % 2 == 1:
		print(i)
	i +=1
"""
# 3.输出 1-100 内的所有偶数
"""
i = 1
while i <= 100:
	if i % 2 == 0:
		print(i)
	i +=1
"""
# 4.用户登陆（有三次输错机会）且每次输错误时显示剩余错误次数（提示：使用字符串格式化）
"""
times = 1
while times <= 3:
	pwd = input("请输入您的密码:")
	if pwd == "111":
		print("恭喜你登录成功~")
		break
	
	# 剩余次数 = 总次数 - 已经使用的次数
	print("你剩余的输入次数是%d" % (3 - times))	
	times +=1
"""
"""
sign = True
times = 1
while sign:
	pwd = input("请输入您的密码:")
	if pwd == "111":
		print("恭喜你登录成功~")
		sign = False
	else:
		# 剩余次数 = 总次数 - 已经使用的次数
		print("你剩余的输入次数是%d" % (3 - times))

	# 如果次数已经是3次了,强制终止循环;
	if times == 3:
		print("你已经没有机会了... ")
		sign = False	
	times +=1
"""
# 5.写代码，有如下字符串利用切片实现每一个功能
strvar = "132a4b5c"
# 1)对字符串进行切片形成新的字符串 "132"
print(strvar[0:3])
# 2)对字符串进行切片形成新的字符串 "a4b"
print(strvar[3:6])
# 3)对字符串进行切片形成新的字符串 "1245"
print(strvar[::2])
# 4)对字符串进行切片形成新的字符串 "3ab"
print(strvar[1:6:2])
# 5)对字符串进行切片形成新的字符串 "c"
print(strvar[-1:])
# 6)对字符串进行切片形成新的字符串 "ba3"
print(strvar[-3::-2]) # -3 -5 -7 

# 6.国际棋盘效果
# 方法一
j = 0
while j < 8:	
	# □■□■□■□■
	if j % 2 == 0:
		print("□■□■□■□■",end="")			
	# ■□■□■□■□
	else:
		print("■□■□■□■□",end="")
	print()
	j +=1

"""
# □■□■□■□■
i = 0		
while i < 8:
	if i % 2 == 0:
		print("□",end="")
	else:
		print("■",end="")
	i +=1 

# ■□■□■□■□
i = 0		
while i < 8:
	if i % 2 == 0:
		print("■",end="")				
	else:
		print("□",end="")
	i +=1 
"""

print("<=====>")
j = 0
while j < 8:	
	# □■□■□■□■
	if j % 2 == 0:
		i = 0		
		while i < 8:
			if i % 2 == 0:
				print("□",end="")
			else:
				print("■",end="")
			i +=1 		
	# ■□■□■□■□
	else:
		i = 0		
		while i < 8:
			if i % 2 == 0:
				print("■",end="")				
			else:
				print("□",end="")
			i +=1 
	print()
	j +=1


# 方法二
"""
□■□■□■□■
■□■□■□■□
□■□■□■□■
■□■□■□■□
□■□■□■□■
■□■□■□■□
□■□■□■□■
■□■□■□■□
"""

print("<=====>")
i = 0
while i < 64:
	# 判断当前是奇数行还是偶数行
	if i // 8 % 2 == 0:
		# □■□■□■□■
		if i % 2 == 0:
			print("□",end="")
		else:
			print("■",end="")
	else:
		# ■□■□■□■□
		if i % 2 == 0:
			print("■",end="")			
		else:
			print("□",end="")
	# 第八个方块换行
	if i % 8 == 7:
		print()		
	i +=1
	
print("<=====>")
# 方法三
i = 0
while i < 4:
	strvar = ""
	j = 0
	# 打印黑白相间的小方块
	while j < 8:
		if j % 2 == 0:
			strvar += "□"
		else:
			strvar += "■"
		j +=1
	# 正向打印
	print(strvar)
	# 逆向打印
	print(strvar[::-1])
	i +=1



