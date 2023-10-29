# ### python的内置函数
# abs    绝对值函数
print(abs(-1))
print(abs(100))

# round  四舍五入
"""奇进偶不进 n.5的情况特定发生;"""
res = round(3.87)
res = round(4.51)
# res = round(2.5)
# res = round(3.5)
res = round(6.51)
print(res)

# sum    计算一个序列得和
lst = [1,2,3,4,34]
res  = sum(lst)
print(res)

total = 0
for i in lst:
	total += i
print(total)

# max    获取一个序列里边的最大值
# min    获取一个序列里边的最小值
lst = (-100,1,2,3,4,34)
res = max(lst)
res = min(lst)
print(res)

# max / min 的高阶函数的使用方式
tup = (   ("赵万里",100)  , ("赵沈阳",101) , ("孟凡伟",99) )
def func(n):
	# print(n)
	# 按照年龄找到最小值元组
	return n[-1]
	
res = min(tup,key=func)
print(res)
res = max(tup,key=func)
print(res)


dic = {"赵万里":100,"赵沈阳":200,"孟凡伟":-5000}
def func(n):
	# 如果是字典,默认传递的是键
	# print(dic[n])
	return abs(dic[n])
res = min(dic,key=func)
res = max(dic,key=func)
print(res)



# pow    计算某个数值的x次方
"""如果是三个参数,前两个运算的结果和第三个参数取余"""
print(pow(2,3))
print(pow(2,3,7))
print(pow(2,3,4))
print(pow(2,3,5))

print("<======>")
# range  产生指定范围数据的可迭代对象
# 一个参数
for i in range(3): # 0 1 2
	print(i)
	
# 二个参数
for i in range(3, 8): # 3 4 5 6 7 
	print(i)

# 三个参数
# 正向操作
for i in range(1,9,5): # 1 6 留头舍尾
	print(i)
	
# 逆向操作
for i in range(9,1,-3): # 9 6 3 
	print(i)
	

# bin    将10进制数据转化为二进制
print(bin(8))
# oct    将10进制数据转化为八进制
print(oct(8))
# hex    将10进制数据转化为16进制
print(hex(16))
	
	
# chr    将ASCII编码转换为字符
print(chr(65))
# ord    将字符转换为ASCII编码
print(ord("A"))
	
	
# ### eval和exec在和第三方用户交互时候,谨慎使用;
# eval   将字符串当作python代码执行
strvar = "print(123)"
strvar = "int(15)"
print(strvar)
res = eval(strvar)
print(res,type(res))

# strvar = "a=3" error eval的局限性 不能创建变量
# eval(strvar)

# exec   将字符串当作python代码执行(功能更强大)
strvar = "a=3" 
exec(strvar)
print(a)

strvar = """
for i in range(10):
	print(i)
"""
exec(strvar)





# repr   不转义字符输出字符串
strvar = "D:\nython32_gx\tay14"
res = repr(strvar)
print(res)

# input  接受输入字符串
"""
res = input("输入内容")
print(res , type(res))
"""

# hash   生成哈希值
# 文件校验
print(hash("1"))






















	
	
	
	
	
	
	
	
	
	
	



