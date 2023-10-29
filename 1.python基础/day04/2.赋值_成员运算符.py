# ### 赋值运算符: = += -= *= /= //= %= **=

# = 赋值运算符 将右侧的值赋值给左侧变量
a = 5 <= 3
print(a)

var1 = 10
var2 = 5
# +=
"""var1 = var1 + var2"""
var1 += var2
print(var1)

# -=
"""var1 = var1 - var2"""
var1 -= var2
print(var1)

# %=
"""var1 = var1 % vae2"""
var1 %= var2
print(var1)

# ### 成员运算符: in 和 not in (针对容器类型数据)
"""字符串判断时，必须是连续的片段"""
strvar = "今天天气要下雨,赶紧回家收衣服"

res = "今" in strvar
res = "天气" in strvar
res = "赶回" in strvar
print(res)

# 针对于列表，元组，集合
container = ["赵沈阳","赵万里","赵世超"]
container = ("赵沈阳","赵万里","赵世超")
container = {"赵沈阳","赵万里","赵世超"}
res = "赵沈阳" in container
res = "赵万里" not in container
res = "赵世超123423123" not in container
print(res)

# 针对于字典（判断的是字典的键，不是值）
container = {"zsy":"赵沈阳","zwl":"赵万里","zsc":"赵世超"}
res = "赵沈阳" in container # False
res = "zsy" in container
print(res)


