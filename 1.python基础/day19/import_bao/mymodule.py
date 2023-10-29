
# 可以手动指定 * 号的引入范围 __all__
__all__ = ["cat"]


cat = "甜甜"
dog = "旺财"

def jump():
	print("小猫能上树")

def lookdoor():
	print("小狗能看门")
	

class Classroom():
	name = "python32"

print("我是mymodule模块")


print("<======1=====>")
print(__name__)
print("<======2=====>")


"""
把需要引入的代码写在if判断的上面
把需要做简单测试的代码,不需要引入的代码写在if判断下面,防止导入
"""
if __name__ == "__main__":
	print("<======3======>")
	jump()
	lookdoor()
	print("<======4======>")