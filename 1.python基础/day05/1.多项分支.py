# ### 多项分支(多选一)

"""
if 条件表达式1:
	code1
elif 条件表达式2:
	code2
elif 条件表达式3:
	code3
else:
	code4

如果条件表达式1成立,执行对应的分支code1,反之判断条件表达式2是否成立
如果条件表达式2成立,执行对应的分支code2,反之判断条件表达式3是否成立
如果条件表达式3成立,执行对应的分支code3,如果不成立,直接走else分支

elif 可以是0个 或者 多个
else 可以是0个 或者 一个
"""

youqian = False
youfang = False
youche = False
if youqian == True:
	print("说明这个人很有实力")
elif youfang == True:
	print("能交给朋友么")
elif youche == True:
	print("开了雅迪艾玛调动车,我们碰一碰吧")	
else:
	print("你还是去做美团骑手吧")


# ### 巢状分支
"""单项分支,双向分支,多项分支的互相嵌套组合"""
youqian = True
youfang = True
youche = True
youyanzhi = True
youtili = False

if youqian == True:
	if youfang == True:
		if youche == True:
			if youyanzhi == True:
				if youtili == True:
					print("我要嫁给你~")
				else:
					print("你去吃点大腰子再来~")
			else:	
				print("你去一下泰国+韩国,整整容")
else:
	print("你是个好人呐~")


#出题 height
#女生找对象
	# 男生在1米~1.5米之间 小强 你在哪里?
	# 男生在1.5~1.7米之间 没有安全感~
	# 男生 1.7~ 1.8米之间 帅哥 留个电话
	# 男生 1.8~2米之间 帅哥 你建议多一个女朋友吗

# python特有
"""
height = float(input("请输出您的身高"))
if 1 <= height < 1.5:
	print("小强 你在哪里?")
elif 1.5 <= height < 1.7:
	print("没有安全感~")
elif 1.7 <= height < 1.8:
	print("帅哥 留个电话")
elif 1.8 <= height < 2:
	print("帅哥 你建议多一个女朋友吗")
else:
	print("抱歉,没有合适的选项")
"""

# 通用写法
height = float(input("请输出您的身高"))
if height >= 1 and height < 1.5:
	print("小强 你在哪里?")
elif height >= 1.5 and height < 1.7:
	print("没有安全感~")
elif height >= 1.7 and height < 1.8:
	print("帅哥 留个电话")
elif height >= 1.8 and height < 2:
	print("帅哥 你建议多一个女朋友吗")
else:
	print("抱歉,没有合适的选项")


"""
tab 向右缩进
shift + tab 向左缩进
"""


















