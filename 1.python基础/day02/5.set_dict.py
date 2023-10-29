# ### 1.set 集合类型（交差并补）
"""特点：无序，自动去重"""
# 1.集合无序
setvar = {"巨石强森","史泰龙","施瓦辛格","王文"}
print(setvar, type(setvar))

# 获取集合中的元素 不可以
# setvar[0]		error

# 修改集合中的元素 不可以
# setvar[2] = 111		error

# 2.集合自动去重
setvar = {"巨石强森","史泰龙","施瓦辛格","王文","史泰龙","史泰龙","史泰龙"}
print(setvar, type(setvar))

# 3.定义一个空集合
setvar = set()
print(setvar, type(setvar))



# ### 2.dict 字典类型
"""
键值对存储的数据，表面上有序，实际上无序
dictvar = {键1:值1, 键2:值2, ...}
3.6版本之前，完全无序
3.6版本之后，存储的时候，保留了字典定义的字面顺序，在获取内存中数据时
重新按照字面顺序做了排序，所以看起来有序，实际上存储时还是无序
"""

# 1.定义一个字典
dictvar = {"top":"the shy","middle":"肉鸡","bottom":"jacklove" ,"jungle":"臭鞋","support":"吃饱饱_嘴里种水稻"}
print(dictvar, type(dictvar))

# 2.获取字典的值
res = dictvar["middle"]
res = dictvar["jungle"]
print(res)

# 3.修改字典中的值
dictvar["top"] = "the xboy"
print(dictvar)

# 4.定义一个空字典
dictvar = {}
print(dictvar, type(dictvar))



# ### 3.set 和 dict的注意点
"""
字典的键 和 集合的值 有数据类型上的要求：
（允许的数据类型）不可变的数据类型：Number(int float conplex bool) str tuple
（不允许的数据类型）可变的数据类型：list set dict

哈希算法的提出目的是让书局尽量均匀地在内存当中分配，以减少哈希碰撞，提升存储分配的效率
哈希算法一定是无序的散列，所以集合 和 字典都是无序的

字典的键有要求，值没有要求
字典的值可任意换掉，但是键不可以
"""
# 字典允许的类型范围
dictvar = {1:"abc",4.89:111,False:333,3+90j:666,"王文":"你好帅啊,我好喜欢哦,没毛病",(1,2,3,4,5,6):9999}
print(dictvar)
print(dictvar[(1,2,3,4,5,6)])
# dictvar = {[1,2,3]:123} error  

# 集合允许的范围类型
setvar = {1,"a",4.56,9+3j,False,(1,2,3)}
# setvar = {1,"a",4.56,9+3j,False,(1,2,3),{"a","b"}} error
print(setvar)



# 总结：
"""
无论是变量缓存机制还是小数据数据池的驻留机制，
都是为了节省内存空间，提升代码效率
"""









