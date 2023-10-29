# ### 关键字的使用 pass break continue
# pass 过（代码块中的占位符）

"""
if 20 == 20:
	pass

while True:
	pass
"""

# break 终止当前循环（只能用在循环之中）
# 1 ~ 10 遇到5终止循环
i = 1
while i <= 10:
	print(i)
	if i == 5:
		break
	i += 1

i = 1
while i <= 3:
	j = 1
	while j <= 3:
		if j == 2:
			break
		print(i,j)
		j += 1
	i += 1
# 1,1
# 2,1
# 3,1

"""
if 5 == 5:	error
	break
"""

# continue 跳过当前循环，从下一次循环开始
# 打印 1 ~ 10 跳过5
i = 1
while i <= 10:
	if i == 5:
		# 在跳过之前，因为会终止执行后面的代码，从下一次循环开始
		# 为了避免死循环，手动加1
		i += 1
		continue
	print(i)
	i += 1

# 1 ~ 100 打印所有不含有4的数字
# 方法一
i = 1
while i <= 100:
	strvar = str(i)
	if "4" in strvar:
		i += 1
		continue
	print(i)
	i += 1

# 方法二
i = 1
while i <= 100:
	if i // 10 == 4 or i % 10 == 4:
		i += 1
		continue
	print(i)
	i += 1













