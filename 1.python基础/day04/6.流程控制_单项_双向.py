# ### 流程控制

"""
流程: 代码执行的过程
控制: 对代码执行过程中的把控

三大结构:
(1)顺序结构: 默认代码从上到下,依次执行
(2)分支结构: 单项分支 双向分支 多想分支 巢状分支
(3)循环结构: while / for
"""

# 单项分支
"""
if 条件表达式:
	code1
	code2
当条件表达式成立,返回True,执行对应的代码块
"""
zhiye = "程序员"
if zhiye == "程序员":
	print("拿高薪")
	print("钱多,话少,死的早")
	print("发量日渐稀少")


# 双向分支(二选一)
"""
if 条件表达式:
	code1 ..
else:
	code2 ..
如果条件表达式成立,返回True,执行if这个区间的代码块
如果条件表达式不成立,返回False,执行else这个区间的代码块
if   分支的代码块也叫做真区间
else 分支的代码块也叫做假区间
"""
zhiye = "美团外卖骑手"
zhiye = "律师"
if zhiye == "美团外卖骑手":
	print("打他")
	print("骂他")
	print("喂他辣椒水")
else:
	print("给你一朵红花")


# input 等待用户输入字符串(注意:结果一定是字符串)
"""
name = input("你好~ 你妈贵姓~")
print(name, type(name))
"""

# ### 模拟网站登录
# 如果账户admin = wangwen 密码:password = 111 显示登录成功,否则显示登录失败
# admin = "wangwen"
# password = "111"

admin = input("请输入您的账号:")
password = input("请输入您的密码:")
if admin == "wangwen" and password == "111":
	print("登录成功")
else:
	print("登录失败")











