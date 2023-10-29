# 注释：就是对代码的解释，方便程序员阅读代码，被注释的代码不执行。
# 1.注释的分类：单行注释、多行注释

# 单行注释：#
# python2.x print "hello,world"
# python3.x print("hello,world")

# 多行注释：''' """
'''
print("hello,world")
print("hello,world")
print("hello,world")
'''

"""
print("hello,world")
print("hello,world")
print("hello,world")
"""

# 2.多行注释的注意点
'''
如果里面嵌套的是三个单引号，外层使用三个多引号
如果里面嵌套的是三个双引号，外层使用三个单引号
单双引号要岔开
'''
'''
print("hello,world")
print("hello,world")
"""
print("hello,world")
print("hello,world")
"""
print("hello,world")
print("hello,world")
'''

"""
print("hello,world")
print("hello,world")
'''
print("hello,world")
print("hello,world")
'''
print("hello,world")
print("hello,world")
"""

# 3.注释具有一定的排错性
"""
先用注释包裹一部分代码，查看是否报错
如果ok，缩小注释范围，再去一行行的排查
直到找到错误为止，以此类推...
"""

# 4.其他语言的注释形式
"""
/*	*/ 多行注释
// 单行注释
<!-- --> html注释
"""






















