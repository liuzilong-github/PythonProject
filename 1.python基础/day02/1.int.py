# ### Number数字类型（int float bool complex）
# int类型（正整数 0 负整数）
intvar = 100
print(intvar)

# type 获取值的数据类型
res = type(intvar)
print(res)

# id 获取值的内存地址
res = id(intvar)
print(res)

# 二进制整型
intvar = 0b110
print(intvar)
print(type(intvar))
print(id(intvar))

# 八进制整型
intvar = 0o127
print(intvar)
print(type(intvar))
print(id(intvar))

# 十六进制整型
intvar = 0xff
print(intvar)
print(type(intvar))
print(id(intvar))