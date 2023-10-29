# ### import 导入模块
import mymodule
import mymodule
import mymodule

"""注意点: 模块导入时,导入一次,终身受益,并不会重复导入"""

# 1.import导入的基本使用
"""
# (1) 模块.变量
print(mymodule.cat)
# (2) 模块.函数
mymodule.jump()
# (3) 模块.类
print(mymodule.Classroome().name)
"""

# 2.导入任意模路径下的任意模块
"""
默认导入当前脚本文件同级目录下的模块等..
系统执行流程: 首先看一下sys.path里面有没有想要导入的这个模块路径,
如果有,默认导入;如果没有,需要手动追加
"""
import sys
print(sys.path)
"""
[
'D:\\python32_gx\\day19\\import_bao', 
'D:\\python_lianxi', 
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip', 
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\DLLs', 
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\lib', 
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36', 
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages'
]

[
'/Users/liuzilong/Documents/个人/PythonProject/day19/import_bao', 
'/Users/liuzilong/Documents/个人/PythonProject', 
'/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip', 
'/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8', 
'/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload', 
'/Users/liuzilong/Library/Python/3.8/lib/python/site-packages', 
'/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages'
]
"""

"""
sys.path.append(r"D:\python32_gx\day14")
import mymodule2
print(mymodule2.bird)
"""

# 3.from .. import .. 基本使用
"""from ... 从哪里 import ... 引入具体的某个成员"""

# 导入单个成员
from mymodule import dog
print(dog)

# 导入多个成员
from mymodule import jump, lookdoor
jump()
lookdoor()

# 导入所有成员 * 代表所有
from mymodule import *
print(dog)
print(cat)

# 设置 * 号导入的范围
from mymodule import *
print(dog)		# error
print(cat)

# 设置引入成员的别名 as
from mymodule import cat as c, lookdoor as ld
print(c)
ld()

# 4.__name__的使用
"""
返回模块名字的魔术属性 __name__
	如果当前文件是直接运行的,返回"__main__"字符串
	如果当前文件是间接导入的,返回当前文件名(模块名)
"""
res = __name__
print(res, type(res))












