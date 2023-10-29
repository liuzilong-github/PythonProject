# ### 数学模块
import math

# ceil() 向上取整(对比内置round)
res = math.ceil(3.01)
res = math.ceil(-3.45)
print(res)

# floor() 向下取整操作(对比内置round)
res = math.floor(3.99)
res = math.floor(-3.99)
print(res)

# pow() 计算一个数值的n次方(结果为浮点数) (对比内置pow)
"""结果为浮点数,必须是两个参数"""
res = math.pow(2,3)
# res = math.pow(2,3,3) error
print(res)

# sqrt() 开平方运算(结果为浮点数)
res = math.sqrt(9)
print(res)

# fabs() 计算一个数的绝对值(结果为浮点数) (对比内置abs)
res = math.fabs(-1)
print(res)

# modf() 将一个数值拆分为整数和小数两部分组成元组
res = math.modf(3.897)
print(res)

# fsum() 将一个容器数据中的数据进行求和运算(结果为浮点数) (对比内置sum)
lst = [1,2,3,4]
res = math.fsum(lst)
print(res)

# 圆周率常熟 pi
print(math.pi)