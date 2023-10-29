import re

# 1、匹配整数或者小数（包括正数和负数）
print(re.findall(r"-?\d+(?:\.\d+)?", "1 -100 -232.23 12.55 fsdf 你好"))

# 2、匹配年月日日期 格式 2018-12-31
print(re.findall(r"\d{4}-\d{1,2}-\d{1,2}", "2018-12-31 2018-1-2 fsdf 你好 22"))
# re.findall(r"([12]\d{3})-(0?[1,9]|1[0-2])-(0?[1-9]|[12]\d|3[01])")

# 3、匹配qq号 5-12 首字符没有0
print(re.findall(r"[1-9]\d{4,11}", "54421419 3097809130 00000000 dad 大萨达"))

# 4、11位的电话号码
print(re.findall("1\d{10}", "13111223344 18518753334 dad 44444444444 12131 阿达"))

# 5、长度为8-10位的用户密码 : 包含数字字母下划线
print(re.findall(r"\w{8,10}", "asd131_dad dasdasdas 你阿德 1212"))

# 6、匹配验证码：4位数字字母组成的
print(re.findall(r"[0-9a-zA-Z]{4}", "7acd aaaa dasY 你阿德 1214"))

# 7、匹配邮箱地址 邮箱规则 123463922@qq.com  123@abc.com.cn
# @之前必须有内容且只能是字母,数字,下划线(_),减号(-),点(.)
# @符号后面是字母,数字,减号(-),保留121@qq.com.cn 的可能
# 最后一个点(.)之后必须有内容,字母,数字且长度为大于等于2个字节,小于等于6个字节
print(re.findall(r"(?:\w|\.|-)+@[0-9a-zA-Z-]+\.[0-9a-zA-Z]{2,6}$", "123@abc.commm"))
# re.findall(r"[\w\.\-]+@[0-9a-zA-Z\-]+(\.[0-9a-zA-Z\-]+)?\.[0-9a-zA-Z]{2,6}")


# 8、从类似
# <a>wahaha</a>
# <b>banana</b>
# <h1>qqxing</h1>
# <h1>q</h1>
# 这样的字符串中，
strvar = """
<a>wahaha</a>
<b>banana</b>
<h1>qqxing</h1>
<h1>q</h1>
"""
# 1）匹配出 wahaha，banana，qqxing 内容。
lst = re.findall(r"<.*?>(.*?)<.*?>", strvar)
print(lst)
# 2）匹配出 a,b,h1这样的内容
lst = re.findall(r"<(.*?)>.*?<.*?>", strvar)
print(lst)

# 9、'1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
strvar = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# 从上面算式中匹配出最内层小括号以及小括号内的表达式
lst = re.findall(r"\([0-9\+\-\*/]*\)", strvar)
print(lst)
# re.findall(r"\([^\(\)]+\)")


# 10正则小程序:
"""
	给你字符串 '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))' 计算最后结果.  
"""
strvar = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'


def operate_sign(str_var):
	str_var = str_var.replace("++", "+")
	str_var = str_var.replace("+-", "-")
	str_var = str_var.replace("-+", "-")
	str_var = str_var.replace("--", "+")
	return str_var


def calc_res(str_var):
	if "*" in str_var:
		a, b = str_var.split("*")
		return float(a) * float(b)
	elif "/" in str_var:
		a, b = str_var.split("/")
		return float(a) / float(b)


def calc_exp(str_var):
	while True:
		obj = re.search(r"\d+(\.\d+)?[*/][+-]?\d+(\.\d+)?", str_var)
		if obj:
			res1 = obj.group()
			res2 = calc_res(res1)
			str_var = str_var.replace(res1, str(res2))
		else:
			break
	str_var = operate_sign(str_var)
	total = 0
	res3 = re.findall(r"[+-]?\d+(?:\.\d+)?", str_var)
	for i in res3:
		total += float(i)
	return total


def remove_bracket(str_var):
	while True:
		obj = re.search(r"\([^\(\)]+\)", str_var)
		if obj:
			res1 = obj.group()
			res2 = calc_exp(res1)
			str_var = str_var.replace(res1, str(res2))
		else:
			return str_var


def main(str_var):
	# 去除表达式中的空格
	str_var = str_var.replace(" ", "")
	# 去除括号
	str_var = remove_bracket(str_var)
	return calc_exp(str_var)


res = main(strvar)
print("计算结果为:{}".format(res))
print(eval(strvar))




