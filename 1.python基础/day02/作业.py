# 1.浮点型,复数有几种表示方法?啥是复数
"""
floatvar = 2.5
floatvar = 2.5e5

complexvar = 3 + 4j
res = complexvar(3,4)

负数：如果一个数的平方为-1，则这个数就是j，用来表示一个高精度数。
"""

# 2.啥是转义字符,怎么用?啥是元字符串
"""
\ + 字符
转义字符：把有意义的字符转换为无意义，把无意义的字符转换成有意义

元字符串：r""
"""

# 3.list tuple str 特征
"""
list：可获取，可修改，有序
tuple：可获取，不可修改，有序
str：可获取，不可修改，有序
"""

# 4.整型当中,2 8 16进制的表示方法
"""
intvar = 0b110
intvar = 0o176
intvar = 0xff
"""

# 5.如何对字符串进行格式化?常用占位符?
"""
%s：字符串占位符
%d：整型占位符
%f：浮点型占位符
strvar = "你好，我是%s" % ("Alex")

"""

# 6.字典和集合有什么特点
"""
集合：无序，可以进行去重
字典：无序，可获取，可修改键对应的值
"""

# 7.字典的键和集合的值有什么类型上的要求
"""
必须是不可变类型的：str, int, float, bool, complex, tuple
"""

# 8.同一文件内的变量有什么样的缓存机制
"""
小数据池：为了节省内存空间
整型：-5~正无穷
浮点型：正数
复数：只有虚数时
字符串：相同
布尔型：True False
元组：()
"""


