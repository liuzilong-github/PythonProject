# ### time模块
import time

# time()	获取本地时间戳
res = time.time()
print(res)

# localtime <=> mktime => ctime

# localtime()	获取本地时间元组(参数是时间戳,默认当前)
# 默认当前时间元组
ttp = time.localtime()
print(ttp)

# 指定具体的时间戳
ttp = time.localtime(1601360000)
print(ttp)

# mktime()	通过时间元组获取时间戳(参数是时间元组)
res1 = time.mktime(ttp)
print(res1)

# ctime()	获取本地时间字符串(参数是时间戳,默认当前)
# 默认当前时间戳
res = time.ctime()
print(res)

# 指定具体的时间戳
res = time.ctime(res1)
print(res)

# asctime()		通过时间元组获取时间字符串(参数是时间元组) (了解)
"""只能通过手动的形式来调星期"""
ttp = (2022,9,29,15,46,40,0,0,0)
res = time.asctime(ttp)
print(res)

# mktime 配合 ctime 来取代 asctime (推荐)
"""自动识别当前是周几"""
res = time.mktime()
strvar = time.ctime(res)
print(strvar)

# sleep()	程序睡眠等待
"""
time.sleep(10)
print("我睡醒了")
"""

# strftime()	格式化时间字符串(格式化字符串,时间元组)
"""linux支持中文,windows不支持"""
strvar = time.strftime("%Y-%m-%d %H:%M:%S")
strvar = time.strftime("%Y-%m-%d %H:%M:%S 是杜兰特的死神的生日")
print(strvar)

strvar = time.strftime("%Y-%m-%d %H:%M:%S",(2020,10,31,10,10,10,0,0,0))
print(strvar)

# strptime()	将时间字符串通过指定格式提取到时间元组中(时间字符串,格式化字符串)
"""注意:替换时间格式化标签时,必须严丝合缝,不能随便添加空格活特殊字符"""
ttp = time.strptime("2020年的9月29号是死神杜兰特的生日,晚上20点30分40秒准备轰趴派队","%Y年的%m月%d号是死神杜兰特的生日,晚上%H点%M分%S秒准备轰趴派队")
print(ttp)


"""
strftime: 把时间元组 => 字符串
strptime: 把字符串 => 时间元组
"""

# pref_counter()	用于计算程序运行的时间(了解)

# starttime = time.pref_counter()
starttime = time.time()
for i in range(100000):
	pass
# endtime = time.pref_counter()
endtime = time.time()
print("中间用时:", endtime-starttime)











