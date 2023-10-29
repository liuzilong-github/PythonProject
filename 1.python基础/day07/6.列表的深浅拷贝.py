# ### 列表的深浅拷贝
"""
a = 100
b = a
a = 200
print(b)

lst1 = [1,2,3]
lst2 = lst1
lst1.append(4)
print(lst2)
"""

# 1.浅拷贝
import copy
# 模块.方法() 同名模块下的同名方法
# 方法一(推荐)
lst1 = [1,2,3]
lst2 = copy.copy(lst1)
lst1.append(10)
print(lst2)
print(lst1)

# 方法二
lst1 = [1,2,3]
lst2 = lst1.copy()
lst1.append(11)
print(lst1)
print(lst2)

# 2.深拷贝
# 把所有层级的容器元素都单独拷贝一份,放到独立的空间中
"""
# 现象
lst1 = [1,2,3,[4,5,6]]
lst2 = copy.copy(lst1)
lst[-1].append(77)
lst1.append(8888)
print(lst2)
print(lst1)
"""

import copy
lst1 = [1,2,3,[4,5,6]]
lst2 = copy.deepcopy(lst1)
lst1[-1].append(99)
print(lst2)
print(lst1)

# 其他容器的深拷贝
lst1 = (1,2,3,{"a":1,"b":[10,20]})
lst2 = copy.deepcopy(lst1)
lst[-1]["b"].append(30)
print(lst1)
print(lst2)


"""
总结:
浅拷贝:
	只拷贝一级容器中的所有元素独立出一个单独的空间
深拷贝:
	把所有层级的容器中的所有元素都单独拷贝一份,形成独立的空间
"""

"""
tuple 只有count index两个方法,使用同列表
"""










