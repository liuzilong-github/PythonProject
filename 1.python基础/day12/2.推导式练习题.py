# ### 推导式练习题
# (1) {'x': 'A', 'y': 'B', 'z': 'C' } 把字典写成x=A,y=B,z=C的列表推导式
dic = {'x': 'A', 'y': 'B', 'z': 'C' }
lst = []
for k,v in dic.items():
	res = k + "=" + v
	lst_new.append(res)
print(lst)

# 推导式
lst = [k+"="+v for k,v in dic.items()]
print(lst)

# (2) 把列表中所有字符变成小写  ["ADDD","dddDD","DDaa","sss"]
lst = ["ADDD","dddDD","DDaa","sss"]
lst_new = []
for i in lst:
	lst_new.append(i.lower())
print(lst_new)

# 推导式
lst = [i.lower() for i in lst]
print(lst)

# (3) x是0-5之间的偶数,y是0-5之间的奇数 把x,y组成一起变成元组,放到列表当中
# 方法一
lst = []
for i in range(6):
	for j in range(6):
		if i % 2 == 0 and j % 2 == 1:
			lst.append((i,j))
print(lst)

# 推导式
lst = [(i,j) for i in range(6) for j in range(6) if i % 2 == 0 and j % 2 == 1]
print(lst)

# 方法二
lst = []
for i in range(6):
	if i % 2 == 0:
		for j in range(6):
			if j % 2 == 0:
				lst.append((i,j))
print(lst)

# 推导式
lst = [(i,j) for i in range(6) if i % 2 == 0 for j in range(6) if j % 2 == 1]
print(lst)

# (4) 使用列表推导式 制作99乘法表中的运算
for i in range(1,10):
	for j in range(1,i+1):
		print("{:d}*{:d}={:2d} ".format(i,j,i*j) , end="")
    print()

# 推导式
lst = ["{:d}*{:d}={:2d} ".format(i,j,i*j) for i in range(1,10) for j in range(1,i+1)]
print(lst)

# (5) 求M,N中矩阵和元素的乘积
# M = [ [1,2,3], 
#       [4,5,6], 
#       [7,8,9]  ] 

# N = [ [2,2,2], 
#       [3,3,3], 
#       [4,4,4]  ] 

M = [ [1,2,3] ,[4,5,6] , [7,8,9] ]
N = [ [2,2,2] ,[3,3,3] , [4,4,4] ]

"""
M[0][0] * N[0][0] = 2
M[0][1] * N[0][1] = 4
M[0][2] * N[0][2] = 6

M[1][0] * N[1][0] = 12
M[1][1] * N[1][1] = 15
M[1][2] * N[1][2] = 18

M[2][0] * N[2][0] = 12
M[2][1] * N[2][1] = 15
M[2][2] * N[2][2] = 18
"""
# =>实现效果1   [2, 4, 6, 12, 15, 18, 28, 32, 36]
lst = []
for i in range(3):
	for j in range(3):
		lst.append(M[i][j] * N[i][j])
print(lst)

# 推导式
lst = [M[i][j] * N[i][j] for i in range(3) for j in range(3)]

# =>实现效果2   [  [2, 4, 6], [12, 15, 18], [28, 32, 36]   ]
lst = []
for i in range(3):
	lst.append([])
print(lst)

for i in range(3):
	for j in range(3):
		lst[i].append(M[i][j] * N[i][j])
print(lst)

# 推导式
lst = [[M[i][j] * N[i][j] for i in range(3)] for i in range(3) for j in range(3)]
print(lst)

"""
[[M[i][j] * N[i][j] for i in range(3)]
[[2,4,6], [12,15,18], [28,32,36]]
"""












