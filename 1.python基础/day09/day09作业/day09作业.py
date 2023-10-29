"""
#1.有如下文件，a1.txt，里面的内容为：
# 	键盘敲烂,
# 	月薪过万.
# 	键盘落灰,
# 	狗屎一堆.

# 分别完成以下的功能：
# a:将原文件全部读出来并打印。
with open("a1.txt", mode="r", encoding="utf-8") as fp:
	res = fp.read()
	print(res)
# b:在原文件后面追加一行内容：信不信由你，反正我信了。
with open("a1.txt", mode="a", encoding="utf-8") as fp:
	fp.write("信不信由你，反正我信了。")
# c:将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
with open("a1.txt", mode="a+", encoding="utf-8") as fp:
	fp.read()
	fp.write("信不信由你，反正我信了。")
# d:将原文件全部清空，换成下面的内容:
# 	每天坚持一点，
# 	每天努力一点，
# 	每天多思考一点，
# 	慢慢你会发现，
# 	你的进步越来越大。
strvar = "	每天坚持一点，
	每天努力一点，
	每天多思考一点，
	慢慢你会发现，
	你的进步越来越大。"
with open("a1.txt", mode="w", encoding="utf-8") as fp:
	fp.write(strvar)
# e:将原文件内容全部读取出来，
# 	并在'键盘落灰'这一行的前面加一行，'年薪百万'
# 	然后将更改之后的新内容，写入到一个新文件：a1.txt。
with open("a1.txt", mode="r", encoding="utf-8") as f1, open("a2.txt", mode="w", encoding="utf-8") as f2:
	lst = f1.readlines()
	lst.insert(2, '年薪百万,\n')
	f2.writelines(lst)
"""


"""
#2.有如下文件，t1.txt,里面的内容为：
# 	葫芦娃，葫芦娃，
# 	一根藤上七个瓜
# 	风吹雨打，都不怕，
# 	啦啦啦啦。
# 	上面的内容你肯定是心里默唱出来的,对不对

# 分别完成下面的功能：
# a:以r+的模式打开原文件，判断原文件是否可读，是否可写。
with open("t1.txt", mode="r+", encoding="utf-8") as fp:
	res = fp.readable()
	print(res)
	res = fp.writable()
	print(res)
# b:以r的模式打开原文件，利用for循环遍历文件对象。
with open("t1.txt", mode="r", encoding="utf-8") as fp:
	for i in fp:
		print(i)
# c:以r的模式打开原文件，以readlines()方法读取出来，并循环遍历
with open("t1.txt", mode="r", encoding="utf-8") as fp:
	lst = fp.readlines()
	for i in lst:
		print(i)
# d:以r模式读取‘葫芦娃，’前四个字符。
with open("t1.txt", mode="r", encoding="utf-8") as fp:
	res = fp.read(4)
	print(res)
# e:以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
with open("t1.txt", mode="r", encoding="utf-8") as fp:
	res = fp.readline()
	print(res.strip())
# f:以r模式打开文件，从‘风吹雨打.....’开始读取，一直读到最后。
with open("t1.txt", mode="r", encoding="utf-8") as fp:
	for i in fp.readlines()[2:]:
		print(i)
# g:以a+模式打开文件，先追加一行：‘老男孩教育’然后在全部读取出来。
with open("t1.txt", mode="a+", encoding="utf-8") as fp:
	fp.write("\n老男孩教育")
	fp.seek(0)
	res = fp.read()
	print(res)
# h:截取原文件，截取内容：‘葫芦娃，葫芦娃，’
with open("t1.txt", mode="r", encoding="utf-8") as fp:
	fp.truncate(24)
"""


# 3.文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
# 	apple 10 3
# 	tesla 100000 1
# 	mac 3000 2
# 	lenovo 30000 3
# 	chicken 10 3
# 变成如下数据格式,并计算出总价格
# [
# 	{'name':'apple','price':10,'amount':3},
# 	{'name':'tesla','price':1000000,'amount':1}
# ]
lst = []
total = 0
with open("a.txt", mode="r", encoding="utf-8") as fp:
	for i in fp.readlines():
		name, price, amount = i.split()
		lst.append({"name": name, "price": price, "amount": amount.strip()})
		total += int(price) * int(amount.strip())
print(lst)
print("总价格为:{}".format(total))


# 4.定义函数:打印用户传入的容器类型数据长度
def get_length(content):
	if isinstance(content, (str, list, tuple, set, dict)):
		return len(content)
	else:
		return "输入类型错误"

res = get_length("abc")
print(res)


# 5.定义函数:参数为容器类型数据,打印所有奇数位索引对应的元素
def get_odd_nember(content):
	if isinstance(content, (str, list, tuple, set, dict)):
		return content[1::2]
	else:
		return "输入类型错误"

res = get_odd_nember("abc")
print(res)


# 6.定义函数:,接收一个参数(可迭代性数据),用_让元素相连成字符串,打印出来
def splicing(content):
	strvar = ""
	if isinstance(content, (str,list,set,tuple,dict)):
		for i in content:
			strvar += str(i) + "_"
		return strvar.rstrip("_")
	else:
		return "输入类型错误"

res = splicing("abc")
print(res)


# 7.输入字符串 "k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....} 打印出来
def transformation(str):
	dic = {}
	lst = str.split("|")
	for i in lst:
		a, b = i.split(":")
		dic[a] = int(b)
	return dic

res = transformation("k:1|k1:2|k2:3|k3:4")
print(res)

# 8.输入列表li= [11,22,33,44,55,66,77,88,99,90]
# 	将大于 66 的值保存至字典的k1键中，
# 	将小于 66 的值保存至字典的k2键中。
# 	打印字典 {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
li = [11,22,33,44,55,66,77,88,99,90]

def compare(lst):
	dic = {"k1": [], "k2": []}
	for i in lst:
		dic["k1"].append(i) if i > 66 else dic["k2"].append(i)
	return dic

res = compare(li)
print(res)