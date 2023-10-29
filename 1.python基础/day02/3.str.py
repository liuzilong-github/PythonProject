# ### 字符串类型 str
"""
用引号引起来的就是字符串，单引号，双引号，三引号

# 转义字符 \ + 字符
	（1）可以将无意义的字符变得有意义
	（2）可以将有意义的字符变得无意义
\n：换行
\r\n：换行
\t：缩进（水平制表符）
\r：将\r后面的字符串拉到了当前行的行首
"""

# 1.单引号的字符串
strvar = '测试'
print(strvar, type(strvar))

# 2.双引号的字符串
strvar = "测试"
print(strvar, type(strvar))
# 可以将无意义的字符变得有意义
strvar = "还有诗和\n远方的田野"
strvar = "还有诗和\r\n远方的田野"
strvar = "还有诗和\t远方的田野"
strvar = "还有诗和\r远方的田野"
strvar = "还有诗和\n远方的\r田野"
# 可以将有意义的字符变得无意义
strvar = strvar = "还有诗和\"远\"方的田野"
print(strvar)

# 3.三引号的字符串（可以支持跨行效果）
strvar = """
生活就像"醉"酒
表面上说'不'要
身体却很诚实
"""
print(strvar)

# 4.元字符串 r"字符串" 原型化输出字符串
strvar = "D:\nython32_python\tay02"
strvar = r"D:\nython32_python\tay02"
print(strvar)

# 5.字符串的格式化
"""
%d：整型占位符
%f：浮点型占位符
%s：字符串占位符
	"字符串" % (值1,,值2)
"""

# %d整型占位符
strvar = "王同佩昨天买了%d风油精,洗澡"  %  (2)
print(strvar)
# %2d 占两位（不够两位用空格补位）原字符串居右
strvar = "王同佩昨天买了%2d风油精,洗澡"  %  (2)
print(strvar)
# %-2d 占两位（不够两位用空格补位）原字符串居左
strvar = "王同佩昨天买了%-2d风油精,洗澡"  %  (2)
print(strvar)

# %f 浮点型占位符
strvar = "赵世超一个月开%f工资" % (9.9)
print(strvar)
# %.2f 保留小数点后面两位小数（存在四舍五入的情况，默认保留6位小数）
strvar = "赵世超一个月开%.2f工资" % (9.178)
print(strvar)
 
# %s字符串占位符
strvar = "%s最喜欢在电影院尿尿" % ("赵万里")
print(strvar)


# 综合案例
strvar = "%s在水里%s被发现了,罚款%.2f元,并且做了%d俯卧撑." % ("孟凡伟","拉屎",500.129,50000)
print(strvar)

# 如果搞不清楚用什么占位符,可以无脑使用%s
strvar = "%s在水里%s被发现了,罚款%s元,并且做了%s俯卧撑." % ("孟凡伟","拉屎",500.129,50000)
print(strvar)


























