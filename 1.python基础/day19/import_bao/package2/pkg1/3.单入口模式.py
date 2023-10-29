# ### 单入口模式
"""
相对路径
.	代表当前路径
..	代表上一级路径

相对路径不能被解释器直接引入,路径找不到
分模块中的文件不能直接执行,必须通过导入到主入口文件,
间接执行才能找到对应的路径

含有相对路径的分模块不能直接执行,得通过主入口文件间接执行
"""

ceshi100 = "ceshi100"
ceshi101 = "ceshi101"

# 相对于当前路径找pkg1_m1模块
from . import pkg1_m1
print(pkg1_m1.ceshi103)

# 相对于当前路径pkg1_m1模块中引入ceshi104成员
from .pkg1_m1 import ceshi104
print(ceshi104)

# 找上一级中的一个模块
from .. import pkg_module1
print(pkg_module1.ceshi201)

# 找上一级中的一个模块里的一个成员
from ..pkg_module1 import ceshi202
print(ceshi202)

# 找上一级包中的具体某个模块
from ..pkg2 import pkg2_m2
print(pkg2_m2.ceshi300)

# 找上一级包中的具体某个模块里的具体的某个成员
from ..pkg2.pkg2_m2 import ceshi301
print(ceshi301)


"""
# . 是无限的
.		当前路径
..		上一级路径
...		上一级的上一级
....	上一级的上一级的上一级
.....	(这里的点是无限的)
from .............. import 模块
"""









