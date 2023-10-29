import re
strvar = '1-2*((60-30+-8*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

# 外面有括号,里面再也没有括号的的表达式就是最里层表达式;
# obj = re.search(r"\([^\(\)]+\)",strvar)
# print(obj.group())

# strvar = '1-2*(-5-6/-2*2)+(40 -  7)'

# 去除多余的符号
def operate_sign(strvar):
	strvar = strvar.replace("--","+")
	strvar = strvar.replace("++","+")
	strvar = strvar.replace("-+","-")
	strvar = strvar.replace("+-","-")
	return strvar

# 计算表达式的值
def calc_res(strvar):
	if "/" in strvar:
		a,b = strvar.split("/")
		return float(a) / float(b)
		
	elif "*" in strvar:
		a,b = strvar.split("*")
		return float(a) * float(b)

# 匹配计算出对应的表达式
def calc_exp(strvar):
	print(strvar , "strvar ... ") # (-5-6/-2*2) 
	
	# ### part1 只计算乘除
	while True:
		# 1.写一条正则匹配出乘除
		obj = re.search(r"\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?",strvar)
		if obj:
			# 2.匹配出乘除表达式
			res1 = obj.group()
			print(res1 , "res1 ... ") # 6/-2 res1 ... 
			
			# 2.计算当前表达式的结果
			res2 = calc_res(res1)
			print(res2 , "res2 .. ")  # -3.0 res2 ..
			
			# 3.用结果替换原乘除表达式
			strvar = strvar.replace(res1,str(res2))
			print(strvar , "strvar ... 1111") # (-5--3.0*2) strvar ... 1111
		else:
			break
	

	# ### part2 只计算加减
	
	# 把表达式当中多余的符号做一个替换
	strvar = operate_sign(strvar)
	print(strvar,"2222")	
	
	# 计算这个表达式+-结果
	lst = re.findall("[+-]?\d+(?:\.\d+)?",strvar)
	# print(lst)
	
	# 计算累加和
	total = 0
	for i in lst:
		total += float(i)
	
	return total
	
# 去除括号
def remove_bracket(strvar):
	while True:
		obj = re.search(r"\([^\(\)]+\)",strvar)
		print(obj, "liuzilong")
		if obj:
			# 匹配括号里面的表达式
			res1 = obj.group()
			print(res1 , "res1 ... ... .. liuzilong ") # (-5-6/-2*2) res1 ... ... ..
			# 计算括号里面的表达式
			res2 = calc_exp(res1)	
			print(res2,"res2 ... remove_bracket") # 1.0
			# 用计算的结果替换原来的括号
			strvar = strvar.replace(res1,str(res2))
		else:
			return strvar
		
		# print(strvar," strvar ... remove_bracket")

# 主函数统一调用
def main(strvar):
	# 0.先去掉字符串当中出现的空格
	# 1.通过正则匹配到最里层小括号
	# 2.计算括号里面的数值
	# 3.拿算好的数值替换原来的小括号
	# 4.循环在去匹配下一个小括号,依次类推 ...
	
	# 先去掉字符串当中出现的空格
	strvar = strvar.replace(" ","")
	print(strvar)
	
	# 移除表达式中的所有括号
	res = remove_bracket(strvar)
	print(res , "res   main ...")
	
	# 计算最后一次没有括号的那个表达式的结果
	return calc_exp(res)
		
res = main(strvar)
print(res)
# print(eval(strvar))






