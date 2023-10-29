# ### 在同一文件中，变量的缓存机制（仅仅支持python3.6版本负责）
# 1.对于整型而言，-5~正无穷范围内的相同值 id一致
var1 = 5
var2 = 5
var1 = -100
var2 = -100
print(id(var1) , id(var2) )

# 2.对于浮点数而言，非负数范围内的相同值 id一致
var1 = 4.67
var2 = 4.67
var1 = -4.67
var2 = -4.67
print(id(var1) , id(var2))

# 3.对于布尔值而言，值相同情况下，id一致
var1 = True
var2 = True
print(id(var1) , id(var2))

# 4.对于复数在 实数+虚数 这样的结构中永不相同（只有虚数的情况例外）
var1 = 4 +5j
var2 = 4 +5j
# 5j 情况下例外
var1 = 5j
var2 = 5j
var1 = -5j
var2 = -5j
print(id(var1) ,id(var2))

# --->容器类型部分
# 5.字符串 和 空元组 相同的情况下，地址相同
var1 = "你"
var2 = "你"
var1 = ()
var2 = ()
print(id(var1) ,id(var2))

# 6.列表，元组，字典，集合无论什么情况 id标识都不同（空元组例外）
var1 = (1,2)
var2 = (1,2)
var1 = [1,2,3]
var2 = [1,2,3]
print(id(var1) ,id(var2))



# 总结：
"""
无论是变量缓存机制还是小数据数据池的驻留机制，
都是为了节省内存空间，提升代码效率
"""