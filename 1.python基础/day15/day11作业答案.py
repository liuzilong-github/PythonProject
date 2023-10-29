# 1.用map来处理字符串列表,把列表中所有人都变成 leader ,比方alex_leader
name = ['oldboy', 'alex', 'wusir']
"""
it = map(lambda n : n+"_leader",name)
print(list(it))
"""
# 2.用map来处理下述 listvar ,要求得到新列表,每个元素名字加后面加_leader
listvar = [{'name':'alex'},{'name':'wusir'}]
def func(n):
	# print(n)
	# n["name"] + "_leader"
	# 方法一
	# return n["name"] + "_leader"
	# 方法二
	n["name"] += "_leader"
	return n
	
it = map(func,listvar)
print(list(it))

# 3.用filter来处理,得到股票价格大于20的股票名字
shares={
   	'IBM':36.6,
   	'Lenovo':23.2,
  	'oldboy':21.2,
        'ocean':10.2,
	}

# 方法一
def func(n):
	if shares[n] > 20:
		return True
	else:
		return False

# 方法二
def func(n):
	if shares[n] > 20:
		return True
		
# 方法三
def func(n):
	return shares[n] > 20

it = filter(func,shares)
print(list(it))

# 方法四
print(list(filter(lambda n : shares[n] > 20,shares)))


# 4.有下面字典:
portfolio=[
	{'name':'IBM','shares':100,'price':91.1},
	{'name':'AAPL','shares':20,'price':54.0},
	{'name':'FB','shares':200,'price':21.09},
	{'name':'HPQ','shares':35,'price':31.75},
	{'name':'YHOO','shares':45,'price':16.35},
	{'name':'ACME','shares':75,'price':115.65}
]
# a.获取购买每只股票的总价格(乘积),迭代器中[9110.0, 1080.0 ,......]
def func(n):
	return n["shares"] * n["price"]
it = map(func,portfolio)
print(list(it))
# lambda
print(list(map(lambda n : n["shares"] * n["price"] ,portfolio)))

# b.用filter过滤出price大于100的股票。
def func(n):
	if n["price"] > 100:
		return True

it = filter(func,portfolio)
print(list(it))

# 方法二
print(list(filter(lambda n : n["price"] > 100 , portfolio )))

# 5.将listvar 按照列表中的每个字典的values大小进行排序,形成一个新的列表。
listvar = [
	{'sales_volumn': 0},
	{'sales_volumn': 108},
	{'sales_volumn': 337},
	{'sales_volumn': 475},
	{'sales_volumn': 396},
	{'sales_volumn': 172},
	{'sales_volumn': 9},
	{'sales_volumn': 58},
	{'sales_volumn': 272},
	{'sales_volumn': 456},
	{'sales_volumn': 440},
	{'sales_volumn': 239}
]

def func(n):
	return n["sales_volumn"]
	
lst = sorted(listvar,key=func)
print(lst)

# 方法二
print(sorted(listvar,key=lambda n : n["sales_volumn"]))








