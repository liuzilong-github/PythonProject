# ### 字符串的格式化format
# (1)顺序传参
# {}是format中的占位符
strvar = "{}向{}开了一枪,银弹而亡".format("赵沈阳", "需保障")
print(strvar)

# (2)索引传参
strvar = "{1}向{0}开了一枪,银弹而亡".format("赵沈阳", "需保障")
print(strvar)

# (3)关键字传参
strvar = "{who1}摸了{who2}一下,回头一巴掌".format(who1="王伟",who2="马春妮")
strvar = "{who1}摸了{who2}一下,回头一巴掌".format(who1="马春妮",who2="王伟")
print(strvar)

# (4)容器类型数据(列表或元组)传参
# 方法一:
strvar = "{0[0]}摸了{1[1]}一下,嘿嘿一笑,有戏".format(["赵蜂拥","赵世超","杨元涛"] , ("王雨涵","王同培"))
print(strvar)

# 方法二(推荐):
strvar = "{group1[0]}摸了{group2[1]}一下,嘿嘿一笑,有戏".format(group1=["赵蜂拥","赵世超","杨元涛"] , group2 = ("王雨涵","王同培"))
print(strvar)

# 方法三(推荐):
"""
注意:
1.如果该容器是字典,通过键值对取值时,不需要加引号
2.通过下标取值时,不能使用负号(逆向索引)
"""
strvar = "{group1[zfy]}摸了{group2[0]}一下,嘿嘿一笑,有戏".format(group1={"zfy":"赵蜂拥","zsc":"赵世超"} , group2 = ("王雨涵","王同培"))
print(strvar)

