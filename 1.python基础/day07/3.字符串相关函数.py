# ### 字符串相关函数
# *capitalize 字符串首字母大写
strvar = "how are you"
res = strvar.capitalize()
print(res)

# *title 每个单词的首字母大写
strvar = "how old are you"
res = strvar.title()
print(res)

# *upper 将所有字母变成大写
strvar = "How Old Are You"
res = strvar.upper()
print(res)

# *lower 将所有字母变成小写
strvar = "How Old Are You"
res = strvar.lower()
print(res)

# *swapcase 大小写互换
strvar = "How old Are You"
res = strvar.swapcase()
print(res)

# *len 计算字符串的长度
strvar = "python32真热"
res = len(strvar)
print(res)

# *count 统计字符串中某个元素的数量
# count(字符,[开始值,结束值])
strvar = "真热真热呀"
# res = strvar.count("真")		# 2
# res = strvar.count("热",2)		# 1
# res = strvar.count("热",2,3)	# 只有真这个字符,没有热
print(res)

# *find 查找某个字符串第一次出现的索引位置(推荐)
# find(字符,[开始值,结束值])
strvar = "To be or not to be that is a question"
res = strvar.find("to")
res = strvar.find("be",4)
# 如果find 返回的是 -1 代表没找到
res = strvar.find("be",4,10)
print(res)

# *index 与 find功能相同 find找不到返回-1,index找不到数据直接报错
"""
res = strvar.index("be",4,10)
print(res)
"""

# *startswith 判断是否以某个字符或字符串开头
"""
startswith(字符,[开始值,结束值])
endswith(字符,[开始值,结束值])
"""
strvar = "To be or not to be that is a question"
res = strvar.startswith("To")
res = strvar.startswith("To",10)
print(res)

# *endswith 判断是否以某个字符或字符串结尾
res = strvar.endswith("question")
res = strvar.endswith("is",-14,-11)
print(res)


# ### is系列
# *isupper 判断字符串是否都是大写字母
strvar = "HOW A YOU"
res = strvar.isupper()
print(res)

# *islower 判断字符串是否都是小写字母
strvar = "asdf - as"
res = strvar.islower()
print(res)

# *isdecimal 检测字符串是否以数字组成,必须是纯数字
strvar = "jdhskfjshdk"
strvar = "2132840912.123"
strvar = "323423"
res = strvar.isdecimal()
print(res)

# *split 按某字符将字符串分割成列表(默认字符是空格) ***
strvar = "you can you up no can no bb"
lst = strvar.split()
strvar = "you#can#you#up#no#can#no#bb"
lst = strvar.split("#")
print(lst)

# *join 按某个字符将列表拼接成字符串(容器类型都可) ***
lst = ['you', 'can', 'you', 'up', 'no', 'can', 'no', 'bb']
strvar = "".join(lst)
strvar = "#".join(lst)
print(strvar)

# *replace 把字符串的旧字符换成新字符 ***
# 字符串.replace("就字符","新字符",[限制替换的次数])
strvar = "范冰冰爱不爱我,爱我,不爱我,爱我,不爱我"
res = strvar.replace("不爱我","爱我")
# 选择替换的次数
res = strvar.replace("不爱我","爱我",1)
print(res)

# *strip 默认去掉首尾两边的空白符 ***
strvar = "      周润发  "
res = strvar.strip()
print(strvar)
print(res)

# *center 填充字符串,原字符居中(默认填充空格)
# center(字符长度,填充符号)
strvar = "赵世超"
res = strvar.center(10)
# res = strvar.center(10, "*")
print(res)











