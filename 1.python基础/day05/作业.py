# 1.猜大小的游戏：
# 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。
number = 66
input_number = int(input("请输入数组"))
if number < input_number:
	print("猜测的结果大了")
elif number > input_number:
	print("猜测的结果小了")
elif number == input_number:
	print("猜测结果正确")

# 2.输出 1-100 内的所有奇数
num = 1
while num < 101:
	if num % 2 == 1:
		print(num)
	num += 1

# 3.输出 1-100 内的所有偶数
num = 1
while num < 101:
	if num % 2 == 0:
		print(num)
	num += 1

# 4.用户登陆（有三次输错机会）且每次输错误时显示剩余错误次数（提示：使用字符串格式化）
frequency = 3
while frequency:
	username = input("请输入用户名：")
	password = input("请输入密码：")
	if username == "admin" and password == "123456":
		print("登录成功！")
		break
	else:
		frequency -= 1
		print("用户名或密码错误，您还有%s次机会" % frequency)

# 5.写代码，有如下字符串利用切片实现每一个功能
strvar = "132a4b5c"
# 1)对字符串进行切片形成新的字符串 "132"
strvar[:3]
# 2)对字符串进行切片形成新的字符串 "a4b"
strvar[3:6]
# 3)对字符串进行切片形成新的字符串 "1245"
strvar[::2]
# 4)对字符串进行切片形成新的字符串 "3ab"
strvar[1:-2:2]
# 5)对字符串进行切片形成新的字符串 "c"
strvar[-1]
# 6)对字符串进行切片形成新的字符串 "ba3"
strvar[-3::-2]

# 6.国际棋盘效果
White_Chess = "★"
Black_Chess = "☆"
count = 1
while count < 65:
	if count % 2 == 0:
		print(White_Chess, end='')
	else:
		print(Black_Chess, end='')
	if count % 8 == 0:
		print()
		White_Chess, Black_Chess = Black_Chess,White_Chess
	count += 1



















