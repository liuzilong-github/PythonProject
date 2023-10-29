# ### Number数字类型 (int float bool complex)

# 1.float浮点型（小数）
floatvar = 3.6
print(floatvar, type(floatvar))
# 表达方式2 科学记数法
floatvar = 5.7e5	# 小数点右移5
floatvar = 5.7e-2	# 小数点左移2
pring(floatvar, type(floatvar))


# 2.bool 布尔型（True 真的 False 假的）
boolvar = True
boolvar = False
print(boolvar, type(boolvar))


# 3.complex 复数类型
"""
3 + 4j
实数+虚数
实数：3
虚数：4j
j：如果有一个数他的平方等于-1，那么这个数就是j，科学家认为有，用来表达一个高精度的类型
"""
# 表达方式1
conplexvar = 3 + 4j
complex = -2j
print(conplexvar, type(complexvar))
# 表达方式2
"""
complex(实数, 虚数) => 复数
"""
complexvar = complex(3,6)
print(complexvar, type(complex))