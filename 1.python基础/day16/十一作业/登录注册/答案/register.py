# ### 注册
# (1)检测两次密码如果相同,确认注册成功
# (2)检测两次密码如果不同,提示两次密码不一致
# (3)用户名不能重复

# 存放用户的列表
accountlist = []
fp = open("user.txt", mode="r+", encoding="utf-8")
for i in fp:
	# 获取账户名
	account = i.split(":")[0]
	# 添加到账户列表
	accountlist.append(account)

sign = True
while sign:
	name = input("请输入您要注册的用户名: ")
	if name = "" or " " in name:
		print("抱歉,该名字中含有非法字符")
	else:
		# 判断该名字是否被注册过了
		if name in accountlist:
			print("抱歉~您的用户名已被注册~")
		else:
			# 这个名字允许使用
			# 确认用户的密码,输入第一次
			pwd1 = input("请输入您的密码:")
			while True:
				# 确认用户的密码,输入第二次
				pwd2 = input("请确认您的密码:")
				if pwd1 == pwd2:
					# 可以存储该账户密码到文件中
					strvar = name + ":" + pwd1 + "\n"
					fp.write(strvar)
					fp.close()
					sign = False
					print("恭喜您~注册成功")
					break
				# 退出当前的注册状态
				elif pwd2.upper() == "Q":
					print("欢迎下次再来~")
					break
				# 密码不一致
				else:
					print("两次密码不一致~")







