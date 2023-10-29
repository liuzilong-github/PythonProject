# ### 算数运算符: + - * / // % **

# +
var1 = 7
var2 = 90
res = var1 + var2
print(res)

# -
var1 = 7
var2 = 90
res = var1 - var2
print(res)

# *
var1 = 7
var2 = 10
res = var1 * var2
print(res)

# / 结果永远为小数
var1 = 7
var2 = 10
res = var1 / var2
print(res, type(res))

# // 地板除
"""
被除数 / 除数 = 商
注意点：如果被除数或者除数是小数，那么得到正常结果之后，数值后面带上.0变成小数
"""
var1 = 10.0
var2 = 3.0
res = var1 // var2
print(res)

# % 取余
var1 = 7
var2 = 4
res = var1 % var2
# 负数取余
res = -7 % 4 # -3 + 4 = 1
res = 7 % -4 # 3 + (-4) = -1
res = -7 % -4 # -3 (如果被除数和除数都是负的，正常结果加负号即可)
res = 81 % 7 # 4
res = 81 % -7 # -3
res = -81 % 7 # 3
res = -81 % -7 # -4
print(res)

# ** 幂运算
res = 2 ** 3
print(res)


# ### 比较运算符: > < >= <= == !=
"""比较运算符的结果要么为True，要么为False，只有两个值"""
res = 10 > 5
res = 10 >= 10
# == 这个符号是在做比较，比较 == 两边的数值是否一样
res = 5 == 9
res = 5 != 9
print(res)











