# ### import 导入包
"""
文件夹:包  文件:模块
当引入包时,会自动指定包中__init__.py的初始化文件,对包进行初始化
"""

# 1.import引入包的语法
import package1
# 导入包的属性
print(package1.ceshi1)

# 导入包下的某个模块
# 方法一:
import package1.mywork
package1.mywork.myjoin()

# 方法二 as 起别名:
import package1.mywork as pm
pm.myjoin()

# 方法三 把要引入的模块放到初始化文件当中进行引入,简化操作
import package1
"""os.path.getsize()"""
package1.mywork.mygetsize()


# 2.from ... import ... 引入包中具体的成员的语法
# 引入包中的属性
from package1 import ceshi2
print(ceshi2)

# 可以指定 * 号的范围,用__all__
from package1 import *
# print(ceshi2)		# error
print(ceshi3)

# 可以用as起别名
from package1 import ceshi2 as c2, ceshi1 as ceshi1
print(c1)
print(c2)

# 引入包中的模块
from package1 import mywork
mywork.myjoin()

# 引入包中模块下的成员
from package1.mywork import mygetsize
mygetsize()


# 3.单入口模式
"""使用相对路径进行导入"""
import package2.pkg1.pkg1_m2 as ppp2
# print(package2.pkg1.pkg1_m2.ceshi100)
print(ppp2.ceshi100)














