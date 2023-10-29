# (5)format的填充符号的使用(^ > <)
"""
^ 原字符串居中显示
> 原字符串居右显示
< 原字符串居左显示

{who:*^10}
* : 填充的符号
^ : 原字符串居中显示
10: 原字符串长度 + 填充符号的长度 = 10
"""

strvar = "{who:*^10}去长春长生医药公司,{do:*^10},感觉{feel:*^10}".format(who="李亚峰",do="扎疫苗",feel="血槽被掏空")
print(strvar)


# (6)进制转换等特殊符号的使用(:d :f :s :,)

# :d 整型占位符(强制要求类型是整型)
strvar = "刘一峰昨天晚上买了{:d}个花露水泡脚".format(9)
print(strvar)
# :3d 占3位,不够3位拿空格来补(原字符串居右)
strvar = "刘一峰昨天晚上买了{:3d}个花露水泡脚".format(9)
print(strvar)
strvar = "刘一峰昨天晚上买了{:<3d}个花露水泡脚".format(9)
print(strvar)
strvar = "刘一峰昨天晚上买了{:^3d}个花露水泡脚".format(9)
print(strvar)

# :f 浮点型占位符(强制要求类型是浮点型,默认保留小数6位)
strvar = "王雨涵毕业之后的薪资是{:f}".format(9.9)
print(strvar)
# :.2f 小数点后保留2位,存在四舍五入
strvar = "王雨涵毕业之后的薪资是{:2f}".format(9.93726483)
print(strvar)

# :s 字符串占位符
strvar = "{:s}".format("杨元涛真帅")
print(strvar)

# :, 金钱占位符
strvar = "{:,}".format(12345678)


# 综合案例
strvar = "{:s}开工资{:.2f}元,买了{:d}个兰博基尼".format("孙坚", 200000.12345, 10)
print(strvar)


