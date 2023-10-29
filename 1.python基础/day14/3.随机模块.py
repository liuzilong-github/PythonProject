# ### 随机模块
import random

# random() 获取随机0~1之间的小数(左闭右开) 0<=x<1
res = random.random()
print(res)

# randrange() 随机获取指定范围内的整数(包含开始值,不包含结束值,间隔值)
# 一个参数
res = random.readrange(3)
print(res)	# 0 1 2

# 两个参数
res = random.readrange(3,6)
print(res)	# 3 4 5 

# 三个参数
res = random.randrange(1,9,4)
print(res)	# 1 5

res = random.readrange(7,3,-1)
print(res) # 7 6 5 4

# readint() 随机产生指定范围内的随机整数(了解)
res = random.randint(1,3)	# 1 2 3
# res = random.randint(3,5,1)	error
print(res)

# uniform() 获取指定范围内的随机小数(左闭右开)
res = random.uniform(0,2)	# 0<=x<2
print(res)
res = random.uniform(2,0)
print(res)

"""
原码解析:
return a + (b-a) * self.random()

a = 2, b = 0
return 2 + (0-2) * (0<=x<=1)
x = 0 return 2 取到
x = 1 return 0 取不到
0 < x <= 2
"""

# choice() 随机获取序列中的值(多选一
lst = ["孙凯喜","王永飞","于朝志","须臾间","含税小"]
res = random.choice(lst)
print(res)

def mychoice(lst):
	index_num = random.randrange(len(lst))
	return lst[index_num]
print(mychoice(lst))

# lambda 改造
lambda lst: lst[random.randrange(len(lst))]
print(res)

# sample() 随机获取序列中的值(多对多) [返回列表]
tup = ("孙凯喜","王永飞","于朝志","须臾间","含税小")
res = random.sample(tup, 3)
print(res)

# shuffle() 随机打乱序列中的值(直接打乱原序列)
lst = ["孙凯喜","王永飞","于朝志","须臾间","含税小"]
random.shuffle(lst)
print(lst)


# ### 验证码效果
# 验证码里面有大写字母 65 ~ 90
# 小写字母 97 ~ 122
# 数字 0 ~ 9
def yanzhegma():
	strvar = ""
	for i in range(4):
		# 大写字母
		b_c = chr(random.randrange(65,91))
		# 小写字母
		s_c = chr(random.randrange(97,123))
		# 数字
		num = str(random.randrange(10))
		# 把可能出现的数据都放到列表中,让系统抽一个
		lst = [b_c, s_c, num]
		# 抽完之后累计拼接在字符串strvar当中
		strvar += random.choice(lst)
	# 循环四次拼接结束,返回随机验证码
	return strvar

res = yanzhengma()
print(res)













