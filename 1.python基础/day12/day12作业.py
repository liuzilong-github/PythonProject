# 1.用推导式写如下程序
# (1)构建如下列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
lst = [i for i in range(0, 19, 2)]
print(lst)

# (2)lst = ['alex', 'WuSir', '老男孩', '神秘男孩'] 将lst构建如下列表:['alex0', 'WuSir1', '老男孩2', '神秘男孩3']
lst = ['alex', 'WuSir', '老男孩', '神秘男孩']
lst_new = [i+str(lst.index(i)) for i in lst]
print(lst_new)

# (3)构建如下列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
lst = [(i, i+1) for i in range(6)]
print(lst)

# (4)求出50以内能被3整除的数的平方，并放入到一个列表中。
lst = [i*i for i in range(51) if i % 3 == 0]
print(lst)

# (5)M = [[1,2,3],[4,5,6],[7,8,9]], 把M中3,6,9组成新列表
M = [[1,2,3],[4,5,6],[7,8,9]]
lst = [i[2] for i in M]
print(lst)

# (6)构建如下列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
lst = ["python{}期".format(i) for i in range(1,11)]
print(lst)

# (7)过滤掉长度小于3的字符串列表 , 并转换成大写字母
lst = ["dssdf", "Ahjsd", "ds"]
lst_new = [i.upper() for i in lst if len(i) >= 3]
print(lst_new)

# (8)除了大小王,里面有52项,每一项是一个元组,请返回如下扑克牌列表[('红心'，'2'),('草花'，'J'), …('黑桃'，'A')]
lst1 = ["红心", "草花", "黑桃", "梅花"]
lst2 = [str(i) for i in range(2,11)]
lst2.extend("AJQK")
lst = [(i,j) for i in lst1 for j in lst2]
print(lst)

# 2.用推导式写如下程序
lst1 = {
		'name':'alex',
		'Values':[
			{'timestamp': 1517991992.94,'values':100,},
			{'timestamp': 1517992000.94,'values': 200,},
			{'timestamp': 1517992014.94,'values': 300,},
			{'timestamp': 1517992744.94,'values': 350},
			{'timestamp': 1517992800.94,'values': 280}
		]
	}
# 将lst1 转化成如下lst2:
# lst2 = [
# 	[1517991992.94, 100],
# 	[1517992000.94, 200],
# 	[1517992014.94, 300],
# 	[1517992744.94, 350],
# 	[1517992800.94, 280]
# ]
lst2 = [[i['timestamp'],i['values']] for i in lst1["Values"]]
print(lst2)

# 3.读取一个文件所有内容,通过生成器调用一次获取一行数据.
def get_file_content(filename):
	with open(filename, mode="r", encoding="utf-8") as fp:
		yield fp.readline()

gen = get_file_content("a1.txt")
res = next(gen)
print(res)

# 4.将普通求和函数改写成yield写法
# def add(a,b):
#     return a + b
def add_new(a,b):
	yield a + b

gen = add_new(3,6)
res = next(gen)
print(res)