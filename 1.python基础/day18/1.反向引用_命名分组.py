# ### 反向引用
import re
strvar = "<div>明天又要休息了</div>"
obj = re.search("<.*?>(.*?)<.*?>", strvar)
print(obj)

# 获取匹配到的内容
res1 = obj.group()
print(res1)

# 获取分组里的内容
res2 = obj.groups()
print(res2)

# 反向引用的语法 \1把第一个括号里面匹配到的内容在引用一次
obj = re.search(r"<.*?>(.*?)</\1>", strvar)
print(obj)
print(obj.group())
print(obj.groups())

strvar = " z3d4pzd a1b2cab "
obj = re.search(r"(.*?)\d(.*?)\d(.*?)\1\2", strvar)
print(obj)
print(obj.group())
print(obj.groups())

# ### 命名分组
"""
3) (?P<组名>正则表达式) 给这个组起一个名字
4) (?P=组名) 引用之前组的名字,把改组名匹配到的内容放到当前位置
"""
# 写法一
strvar = " z3d4pzd a1b2cab "
obj = re.search(r"(?P<tag1>.*?)\d(?P<tag2>.*?)\d(?P<tag3>.*?)\1\2", strvar)
print(obj)
print(obj.group())

# 写法二
strvar = " z3d4pzd a1b2cab "
obj = re.search(r"(?P<tag1>.*?)\d(?P<tag2>.*?)\d(?P<tag3>.*?)(?P=tag1)(?P=tag2)", strvar)







