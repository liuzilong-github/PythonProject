# ### 登录小程序
# 账户密码会预先记录在文件中
# 输入账号密码:如果都正确,登录成功
# 如果用户登录时进行三次校验,都不对,记录黑名单文件中
# 如果是黑名单的用户,禁止下次再次登录

# 账户列表
accountlist = []
# 密码列表
pwdlist = []
# 黑名单列表
blacklist = []

with open("user.txt", mode="a+", encoding="utf-8") as fp:
	fp.seek(0)
	for i in fp.readlines():
		user,pwd = i.strip().split(":")
		accountlist.append(user)
		pwdlist.append(pwd)

	# 账户列表和密码列表,按照相同的索引下标一一对应

	sign = True
	while sign:
		name = input("请输入您的用户名:")
		if name in accountlist:
			# 打开黑名单
			with open("black.txt", mode="a+", encoding="utf-8") as fp:
				fp.seek(0)
				for i in fp.readlines():
					blacklist.append(i.strip())

			if name in blacklist:
				print("抱歉~ 该账户已经被冻结,请联系客户人员~")
			else:
				# 走到这个分支,说明是合法用户,可以让用户输入密码
				index_num = accountlist.index(name)
				# 通过索引号获取密码
				pwd_true = pwdlist[index_num]
				# 控制密码输错次数不超过3次
				times = 1
				while times <= 3:
					ask_pwd = input("请输入您的登录密码:")
					if ask_pwd == pwd_true:
						print("恭喜您~登录成功")
						sign = False
						break
					else:
						# 剩余次数 = 总次数-使用过的次数
						print("抱歉您的密码输入错误,还剩下{}机会".format(3-times))
						if times == 3:
							print("抱歉~,输错三次,您的账号被冻结~")
							# 把当前用户拉黑,记录到黑名单中
							with open("black.txt", mode="a+", encoding="utf-8") as fp:
								strvar = name + "\n"
								fp.write(strvar)

					times += 1
		else:
			print("抱歉,该用户名不存在")












