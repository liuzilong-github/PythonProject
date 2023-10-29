# ### 复习format

# 指定传的参数类型必须是字符串
strvar = "{:s}在吃东西"
res = strvar.format("赵沈阳")
print(res)

# 关键字传参
strvar = "{who}在吃东西"
res = strvar.format(who="赵万里")
print(res)

# 关键字传参 + 字符串类型
strvar = "{who:s}在吃东西".format(who="刘文伯")
print(strvar)

# 容器类型传参
strvar = "{dic[zwb]:s}在吃东西".format(  dic={"zwb":"刘文伯"} )
print(strvar)

# 容器类型传参 + 填充符号 + 指定类型
strvar = "{dic[zwb]:*^10s}在吃东西".format(  dic={"zwb":"刘文伯"} )
print(strvar)

# 容器类型传参 + 填充符号
strvar = "{dic[zwb]:*^10}在吃东西".format(  dic={"zwb":"刘文伯"} )
print(strvar)

# 容器类型传参 + 默认填充空格
strvar = "{dic[zwb]:^10}在吃东西".format(  dic={"zwb":"刘文伯"} )
print(strvar)
