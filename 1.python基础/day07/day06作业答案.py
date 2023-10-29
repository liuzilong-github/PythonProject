"""
1.利用if语句写出猜大小的游戏：
	设定一个理想数字比如：66，
	让用户三次机会猜数字，如果比66大，则显示猜测的结果大了；
	如果比66小，则显示猜测的结果小了;
	只有等于66，显示猜测结果正确，退出循环。
	最多三次都没有猜测正确，退出循环，并显示‘都没猜对,继续努力’。
"""

times = 1
while times <= 3
	num = input("请输入一个数字:")
	if num.isdecimal():
		num = int(num)
		if num > 66:
			print("结果大了")
		elif num == 66:
			print("对了")
			break
		elif num < 66:
			print("结果小了")
	else:
		print("抱歉,数字格式不对~")
	if times == 3:
		print("都没猜对,继续努力")
	times += 1


# 2.使用while和for 遍历字符串 "IG战队牛逼"
strvar = "IG战队牛逼"
i = 0
while i < len(strvar):
	print(strvar[i])
	i += 1

for i in strvar:
	print(i)


# 3.使用for循环对s="黄绿青蓝紫"进行循环，每次打印的内容是每个字符加上"色的"，	
  # 例如：黄色的 绿色的 青色的 ... 
s="黄绿青蓝紫"
for i in s:
	print(i + "色的")


# 4.完成要求：
"""
# 用户可持续输入(while循环)
	# 输入A，则显示走大路回家，然后在让用户进一步选择：
		# 是选择公交车，还是步行？
		# 选择公交车，显示10分钟到家，并退出整个程序。
		# 选择步行，显示20分钟到家，并退出整个程序。
	# 输入B，
		# 则显示走小路回家，并退出整个程序。
	# 输入C，
		# 则显示绕道回家，然后在让用户进一步选择：
		# 是选择游戏厅玩会，还是网吧？
			# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
			# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
"""
sign = True
while sign:
	opt = input("请输入选项A,B,C")
	if opt.lower() == "a":
		print("走大路回家")
		opt = input("是选择公交车，还是步行？")
		if opt == "公交车":
			print("10分钟到家")
			sign = False
			# break
		elif opt = "步行":
			print("20分钟到家")
			sign = False
			# break
	elif opt.lower() == "b":
		print("走小路回家")
		break
	elif opt.lower() == "c":
		print("绕到回家")
		opt = input("是选择游戏厅玩会，还是网吧?")
		if opt == "游戏厅":
			print("‘一个半小时到家，爸爸在家，拿棍等你.")
		elif opt == "网吧":
			print("两个小时到家，妈妈已做好了战斗准备。")


# 5.写代码：计算 1 - 2 + 3 - 4 + ... + 99 中除了88以外所有数的总和？
total = 0
for i in range(100):
	if i == 88:
		continue
	if i % 2 == 1:
		total += i
	elif i % 2 == 0:
		total -= i
print(total)

total = 0
i = 1
while i <= 99:
	if i == 88:
		i += 1
		continue
	if i % 2 == 1:
		total += i
	elif i % 2 == 0:
		total -= i
	i += 1
print(total)


# 6.(升级题)打印菱形小星星
"""
     *
    ***
   *****
  *******
 *********
***********
***********
 *********
  *******
   *****
    ***
     *
"""

"""
空格 + 星星 + 换行

总行数:
对于任意个星星n,总行数: n // 2 + 1
13 -> 7
11 -> 6
9 -> 5
7 -> 4

空格:
对于当前行1, 空格数量 = 总行数 - 当前行
1 => 5
2 => 4
3 => 2
4 => 2
5 => 1
6 => 0

星星:
对于当前行i,星星数量 = 2 * 当前行 - 1
1 => 1
2 => 3
3 => 5
4 => 7
"""

# 方法一
n = 13
hang = n // 2 + 1
i = 1
while i <= hang:
	# 打印空格
	kongge = hang - i
	print(" " * kongge,end='')
	# 打印星星
	xingxing = 2 * i - 1
	print("*" * xingxing,end='')
	# 打印换行
	print()
	i += 1

i = hang
while i >= 1
# 打印空格
	kongge = hang - i
	print(" " * kongge,end='')
	# 打印星星
	xingxing = 2 * i - 1
	print("*" * xingxing,end='')
	# 打印换行
	print()
	i -= 1

# 方法二
n = 13
hang = n // 2 + 1
i = 1
while i <= hang:
	# 打印空格
	kongge = hang - i
	while kongge > 0:
		print(" ",end='')
		kongge -= 1
	# 打印星星
	xingxing = 2 * i - 1
	j = 1
	while j <= xingxing:
		print("*",end='')
		j += 1
	# 打印换行
	print()
	i += 1

i = hang
while i >= 1
# 打印空格
	kongge = hang - i
	while kongge > 0:
		print(" ",end='')
		kongge -= 1
	# 打印星星
	xingxing = 2 * i - 1
	j = 1
	while j <= xingxing:
		print("*",end='')
		j += 1
	# 打印换行
	print()
	i -= 1


# (扩展了解)
"""abs 求绝对值的内置函数 abs(-1) = 1"""
for i in range(-6,7):
	# 只有一句代码的话,可以直接写在冒号的右边
	if i == 0:continue
	print(" " * (abs(i)-1), "*" * (13-2*abs(i)))





