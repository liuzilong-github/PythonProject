# ### 正则函数
import re
# search 通过正则匹配出第一个对象返回,通过group取出对象中的值
strvar = "3+4 6*4"
obj = re.search(r"\d+[+*]\d+", strvar)
print(obj)

# 获取匹配到的内容
print(obj.group())
# 获取分组当中的内容(返回元组)
print(obj.groups())

# match 验证用户输入内容(了解)
"""search 在正则表达式的前面加上个 ^ 等价于 match ,其他用法上一模一样"""
strvar = "a17366668888"
strvar = "17366668888"
obj = re.search(r"^\d+", strvar)
obj = re.match(r"\d+", strvar)
print(obj.group())
print(obj)

# split 切割
strvar = "alex|wusir_xboyww@risky"
lst = re.split(r"[|_@]", strvar)
print(lst)

strvar = "alex3324wusir412891xboy1231risky"
lst = re.split(r"\d+", strvar)
print(lst)

# sub 替换
strvar = "alex|wusir_xboyww@risky"
"""
strvar = strvar.replace("|", "&")
strvar = strvar.replace("_", "&")
strvar = strvar.replace("@", "&")
print(strvar)
"""
# sub(正则,替换的字符,原字符串,替换的次数)
res = re.sub(r"[|_@]", "&", strvar)
res = re.sub(r"[|_@]", "&", strvar, 1)
print(res)

# subn 替换(用法上与sub相同,只是返回值不同)
res = re.subn(r"[|_@]", "&", strvar)
res = re.subn(r"[|_@]", "&", strvar, 1)
print(res)
# res = re.subn(r"[|_@]", "&", strvar)
# ('alex&wusir&xboyww@risky', 2)

# finditer 匹配字符串中相应内容,返回迭代器
"""返回的是迭代器,迭代器中包含了对象,通过对象.group来获取匹配到的值"""
from collections import Iterator, Iterable
strvar = "sdf23647fdgdfg()*()*23423423"
it = re.finditer(r"\d+", strvar)
print(isinstance(it, Iterator))

for obj in it:
	print(obj.group())

# compile 指定一个统一的匹配规则
"""
正常情况下,正则表达式编译一次,执行一次
为了避免反复编译,节省时间空间,可以使用compile统一规则
编译一次,终身受益
"""
strvar = "asdfs234sdf234"
parrern = re.compile(r"\d+")

print("<===========>")
obj = parrern.search(strvar)
print(obj.group())

lst = parrern.findall(strvar)
print(lst)

# 修饰符
# re.I 使匹配对大小写不敏感
strvar = "<h1>大标题</H1>"
pattern = re.compile("<h1>(.*?)</h1>", flags=re.I)
obj = pattern.search(strvar)
print(obj.group())

# re.M 使每一行都能够单独匹配(多行匹配),影响 ^ 和 $
"""单行独立匹配,而不是整体匹配"""
strvar = """
<p>111</p>
<a>222</a>
<strong>333</strong>
"""

pattern = re.compile("^<.*?>(?:.*?)<.*?>$", flags=re.M)
lst = parrern.findall(strvar)
print(lst)

# re.S 使 . 匹配包括换行在内的所有字符
strvar = """
give
sdfsdfmefive
"""
# 多个修饰符一起使用通过|拼接
pattern = re.compile(r".*?mefive", flags=re.S|re.I|re.M)
obj = pattern.search(strvar)
print(obj.group())









