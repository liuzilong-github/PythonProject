# ### 正则表达式 - 匹配单个字符
import re
"""lst = re.findall(正则表达式, 字符串)"""

# \d 匹配数字
strvar = "sdjfklj234&*(&1"
lst = re.findall(r"\d", strvar)
print(lst)

# \D 匹配非数字
strvar = "YWERsdf78_&"
lst = re.findall(r"\D", strvar)
print(lst)

# \w 匹配字母或数字或下划线	(正则函数中,支持中文的匹配)
strvar = "sadf234_^&*%$^$%你好"
lst = re.findall(r"\w", strvar)
print(lst)

# \W 匹配非字母或数字或下划线
strvar = "sadf234_^&*%$^$%你好"
lst = re.findall(r"\W", strvar)
print(lst)

# \s 匹配任意的空白符 (" " \t \n \r)
strvar = " 		 \r "
lst = re.findall(r"\s", strvar)
print(lst)

# \S 匹配任意的非空白符
strvar = " 		 \r  123_*("
lst = re.findall(r"\S", strvar)
print(lst)

# \n 匹配一个换行符
strvar = """
今天国庆假期结束了,兄弟们满载	而归,玩的	很困,尽	快调	整.
"""
lst = re.findall(r"\n", strvar)
print(lst)

# \t 匹配一个制表符
lst = re.findall(r"\t", strvar)
print(lst)


# 字符组 [] 匹配出字符组当中列举的字符
# lst = re.findall("[123]]", "a1b2c3d4")
# print(lst)

print(re.findall("a[abc]b", "aab abb acb adb"))		# aab abb acb
print(re.findall("a[0123456789]b]", "a1b a2b a3b acb ayb"))		# a1b a2b a3b
# 优化写法 0123456789 => 0-9
print(re.findall("a[0-9]b", "a1b a2b a3b acb ayb"))		# a1b a2b a3b

print(re.findall("a[abcdefg]b", "a1b a2b a3b acb ayb adb"))		# acb adb
# 优化写法 abcdefg => a-g 表达所有的小写字母 a-z
print(re.findall("a[a-g]b", "a1b a2b a3b acb ayb adb"))		# acb adb
print(re.findall("a[a-z]b", "a1b a2b a3b acb ayb adb"))		# acb ayb adb

print(re.findall("a[ABCDEFG]b", "a1b a2b a3b aCb aYb aDb"))		# aCb aDb
# 优化写法 ABCDEFG => A-G 表达所有的小写字母 A-Z
print(re.findall("a[A-G]b", "a1b a2b a3b aCb aYb aDb"))		# aCb aDb
print(re.findall("a[A-Z]b", "a1b a2b a3b aCb aYb aDb"))		# aCb aYb aDb

# 注意点: 不能直接写A-z, 中间ascii编码中包含了特殊的符号
print(re.findall("a[A-z]b", "a1b a2b a3b acb aYb adb a[b"))		# acb aYb adb a[b
# 匹配所有的字母和数字
print(re.findall("a[0-9a-zA-Z]b", "a1b a2b a3b acb aYb adb a[b"))		# a1b a2b a3b acb aYb adb
print(re.findall("a[0-9a-zA-Z]b", "a-b aab aAb aWb aqba1b"))	 # aab aAb aWb aqb a1b
print(re.findall("a[0-9][#*/]b", "a1/b a2b a29b a56b a456b"))		# a1/b

# ^ 在字符组开头的位置出现,代表了除了...的意思
print(re.findall("a[^-+*/]b", "a%b ccaa*bda&bd"))		# a%b a&b

# 匹配 ^ 时,需要在前面加上\进行转义
strvar = "a^c a-c a\c"
lst = re.findall(r"a[\^\-\\]c", strvar)		# a^c a-c a\c
print(lst)
print(lst[-1])

# 注意点: 为了防止转义,在正则表达式中或者要匹配的字符串中,无脑加r实现匹配
strvar = r"a\b"
lst = re.findall(r"a\\b", strvar)
print(lst[0])







