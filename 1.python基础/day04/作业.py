"""
# 1.99//4  ,  99%4 ,  -99 %4  ,  -99 %-4值是多少
99 // 4 = 24
99 % 4 = 3
-99 % 4 = 1
-99 % -4 = -3

# 2.成员和身份运算符如何使用
成员运算符用来判断字符串中的某个字符,列表、元组、集合中的某个元素,字典中的某个key是否在对应的字符串、列表、元组、集合、字典中
身份运算符用来判断两个变量的内存地址是否一致

# 3.逻辑运算符优先级?逻辑短路在什么情况下发生?
not > and > or
逻辑短路: False and 表达式
         True or 表达式

# 4.优先级最高和最低的运算符是?
优先级最高的运算符: **
优先级最低的运算符: =

# 5.左移右移后的值如何计算?按位非的公式?
左移: 相当于乘法(乘以2的n次幂)
右移: 相当于除法(除以2的n次幂)
按位非的公式: -(n+1)

# 6.~(-25) ~25 推到一下过程
~(-25)
原码: 100 ... 11001
反码: 111 ... 00110
补码: 111 ... 00111

按位非: 000 ... 11000
原码: 000 ... 11000 => 24

~25
原码: 000 ... 11001
反码: 000 ... 11001
补码: 000 ... 11001

按位非: 111 ... 00110
反码: 100 ... 11001
原码: 100 ... 11010 => -26

# 7.res = 17>15 or 78<11 or 7 and 8 and not True is True  res=?
res = True or False or 7 and 8 and False
res = True or False or False
res True

# 8.计算表达式的值
    1).6 or 2 > 1    => 6  
    2).3 or 2 > 1    => 3  
    3).0 or 5 > 4    => True  
    4).5 < 4 or 3    => 3
    5).2 > 1 or 6    => True
    6).3 and 2 > 1   => True
    7).0 and 3 > 1   => 0
    8).2 > 1 and 3   => 3
    9).3 > 1 and 0   => 0
    10).3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2   => True and 2 or True and 4 or True => 2 or 4 or True => 2
    11)not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
        => not True and True or False and True and True or False
        => False and True or False and True and True or False
        => False or False or False
        => False

# 9.提示用户输入 "如何在dnf中变得更强?". 如果输入的是充钱,打印"马化腾爱你" ,反之输出,"你想一想,不充钱怎么可能变得更强"
problem = input("如何在dnf中变得更强?")
if problem == "充钱":
    print("马化腾爱你")
else:
    print("你想一想,不充钱怎么可能变得更强")
"""





