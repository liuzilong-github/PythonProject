# 1、什么是原码、反码、补码？
"""
原码：用来显示
补码：用来存储
反码：用来原码与反码之间转换
（正数：原码=反码=补码，负数：原码等于补码取反加1，补码等于原码取反加1）
"""

# 2、进制转换234 => 2,8,16：
"""
二进制：0b11101010
八进制：0o352
十六进制：0xea
"""

# 3、进制转换0b10101110，0o137，0xabc：
"""
0b10101110 => 174
0o137 => 95
0xabc => 2748
"""

# 4、进制转换0xabc转换为八进制：
"""
0xabc => 5274
"""

# 5、计算9+(-3) 和 (-9)+3：
"""
9：
原码：0000 ... 1001
反码：0000 ... 1001
补码：0000 ... 1001

-3：
原码：1000 ... 0011
反码：1111 ... 1100
补码：1111 ... 1101

计算：
0000 ... 1001
1111 ... 1101
0000 ... 0110 => 6


-9：
原码：1000 ... 1001
反码：1111 ... 0110
补码：1111 ... 0111

3：
原码：0000 ... 0011
反码：0000 ... 0011
补码：0000 ... 0011

计算：
1111 ... 0111
0000 ... 0011
1111 ... 1010
1000 ... 0101
1000 ... 0110 => -6
"""

# 6、什么是注释：
"""
对代码的解释，帮助他人理解代码，被注释的代码不会被执行
"""

# 7、注释种类：
"""
单行注释：#
多行注释："""""", '''''',
"""

# 8、怎么用注释排错：
"""
先包裹一部分代码，运行程序查看是否报错，若不报错，则缩小范围一行行的排查，直到找到错误为止。
"""

# 9、如何定义变量：
"""
a = 10, b = 20
"""

# 10、变量命名：
"""
数字，字母，下划线组成，不能以数字开头，不能使用关键字，区分大小写
"""

# 11、如何交换变量：
"""
a,b = b,a
"""

# 12、python六大标准数据类型：
"""
number(int, float, complex, bool), string, list, tuple, set, dict,
"""

# 13、浮点型和复数的两种表达方式：
"""
浮点型：1.2, 1.2e2
复数：2+3j，complex(2,3)
"""

# 14、写出三个转义字符，及对应的含义：
"""
\n：换行
\t：制表符（换行）
\r：将r后面的字符串拉到当前行的行首
"""

# 15、简述如何使用字符串的格式化占位符：
"""
%d：整型占位符
%f：浮点型占位符
%s：字符串类型占位符
"字符串" % (值1,值2)
"""

# 16、简述容器类型各个特征：
"""
string：可获取，不可修改，有序
list：可获取，可修改，有序
tuple：可获取，不可修改，有序
set：无序，自动去重
dict：可获取，键不可修改，值可修改，无序
"""

# 17、以下各是什么类型：
"""
{}：空字典
{1}：整型
("abc")：字符串
("abc",)：元组
"""

# 18、字典的键和集合的值有什么要求：
"""
可哈希不可修改的值：number, str, tuple
"""

# 19、用几种方式获取列表中的最后一个值：
"""
lst = [1,2,3]
lst[2], lst[-1]
"""

# 20、3.6版本中，变量的缓存机制有哪些？
"""
int：-5~正无穷
float：非负数
bool：值相同
complex：只有虚数
str：值相同
tuple：空元组
"""





