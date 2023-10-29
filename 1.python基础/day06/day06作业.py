# 1.利用if语句写出猜大小的游戏：
# 	设定一个理想数字比如：66，
# 	让用户三次机会猜数字，如果比66大，则显示猜测的结果大了；
# 	如果比66小，则显示猜测的结果小了;
# 	只有等于66，显示猜测结果正确，退出循环。
# 	最多三次都没有猜测正确，退出循环，并显示‘都没猜对,继续努力’。
num = 66
i = 3
while i: 
	str_num = input("请输入数字：")
	if int(str_num) == num:
		print("猜测结果正确")
		break
	elif int(str_num) < num:
		print("猜测的结果小了")
		i -= 1
	else:
		print("猜测的结果大了")
		i -= 1
	if i == 0:
		print("都没猜对,继续努力")

	
# 2.使用while和for 遍历字符串 "IG战队牛逼"
strvar = "IG战队牛逼"
i = 0
while i < len(strvar):
	print(strvar[i])
	i += 1

for i in strvar:
	print(i)


# 3.使用for循环对s="黄绿青蓝紫"进行循环，每次打印的内容是每个字符加上"色的"，	
#   例如：黄色的 绿色的 青色的 ... 
strvar = "黄绿青蓝紫"
for i in strvar:
	print("%s色的" % i)


# 4.完成要求：
# 用户可持续输入(while循环)
# 	输入A，则显示走大路回家，然后在让用户进一步选择：
# 		是选择公交车，还是步行？
# 		选择公交车，显示10分钟到家，并退出整个程序。
# 		选择步行，显示20分钟到家，并退出整个程序。
# 	输入B，
# 		则显示走小路回家，并退出整个程序。
# 	输入C，
# 		则显示绕道回家，然后在让用户进一步选择：
# 		是选择游戏厅玩会，还是网吧？
# 			选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
# 			选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
while True:
	strvar = input("请输入选项：")
	if strvar == "A":
		print("走大路回家")
		var1 = input("是选择公交车，还是步行？")
		if var1 == "公交车":
			print("10分钟到家")
		elif var1 == "步行":
			print("20分钟到家")
		break
	elif strvar == "B":
		print("走小路回家")
		break
	elif strvar == "C":
		print("绕道回家")
		var2 = input("选择游戏厅玩会，还是网吧")
		if var2 == "游戏厅玩会":
			print("一个半小时到家，爸爸在家，拿棍等你。")
		elif var2 == "网吧":
			print("两个小时到家，妈妈已做好了战斗准备。")


# 5.写代码：计算 1 - 2 + 3 - 4 + ... + 99 中除了88以外所有数的总和？
i = 1
num = 0
while i < 100:
	if i == 88:
		i += 1
		continue
	if i % 2 == 1:
		num += i
	else:
		num -= i
	i += 1
print(num)



# 6.(升级题)打印菱形小星星
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *
i = 1
x = 0
y = 5
p = 4
q = 0
while i <= 12:
	if i <= 6:
		count = i + x
		print(" " * y + "*" * count)
		i += 1
		x += 1
		y -= 1
	else:
		count = i + p
		print(" " * q + "*" * count)
		i += 1
		p -= 3
		q += 1


count = 6
for i in range(1, 12, 2):
	count -= 1
	print(" " * count + "*" * i)
for j in range(11, 0, -2):
	print(" " * count + "*" * j)
	count += 1
























