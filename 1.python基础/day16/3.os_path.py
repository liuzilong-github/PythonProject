# ### os.psth 路径模块
import os

pathvar = "/home/wangwen/mywork/ceshi.py"
pathvar = __file__

# basename() 返回文件名部分
res = os.path.basename(pathvar)
print(res)

# dirname() 返回路径部分
res = os.path.dirname(pathvar)
print(res)

# split() 将路径拆分成单独的文件部分和路径部分,组合成一个元组
print(os.path.split(__file__))

# join() 将多个路径和文件组成新的路径,可以自动通过不同的系统加不同的斜杠 linux / windows \ ***
path1 = "home"
path2 = "wangwen"
path3 = "mywork"
pathvar = path1 + os.sep + path2 + os.sep + path3
print(pathvar)

# 用join改造
path_new = os.path.join(path1, path2, path3)
print(path_new)

# splitext() 将路径分割为后缀和其他部分(了解)
pathvar = "/home/wangwen/mywork/ceshi.py"
print( os.path.splitext(pathvar) )
print( pathvar.split(".")[-1] )

# getsize() 获取文件的大小 ***
# pathvar = os.path.dirname(__file__) # 方法一
pathvar = os.getcwd() # 方法二
path_new = os.path.join(pathvar, "2.py")
print(path_new)
# 计算文件大小
res = os.path.getsize(path_new)
print(pathvar)
res = os.path.getsize("/mnt/hgfs/python32_gx/day14")
print(res)


# isdir() 检测路径是否是一个文件夹 ***
res = os.path.isdir("/mnt/hgfs/python32_gx/day14")
print(res)
# isfile() 检测路径是否是一个文件 ***
res = os.path.isfile("/mnt/hgfs/python32_gx/day16/1.py")
print(res)
# islink() 检测路径是否是一个链接
res = os.path.islink("/home/wangwen/mywork/1122.py")
print(res)


# getctime() [windows]文件的创建时间,[linux]权限的改动时间(返回时间戳)
import time
res = os.path.getctime("/home/wangwen/mywork/4.txt")

# getmtime() 获取文件最后一次修改时间(返回时间戳)
res = os.path.getmtime("/home/wangwen/mywork/4.txt")

# getatime() 获取文件最后一次访问时间(返回时间戳)
res = os.path.getatime("/home/wangwen/mywork/4.txt")
print(res)
print(time.ctime(res))

# exists() 检测指定的路径是否存在 ***
res = os.path.exists("/home/wangwen/mywork/4.txt")
# res = os.path.exists("4.txt")
print(res)

# isabs() 检测一个路径是否是绝对路径
res = os.path.isabs("2.py")
print(res)
# abspath() 将相对路径转化为绝对路径
res = os.path.abspath("2.py")
print(res)

pathvar = "2.py"
if not os.path.isabs(pathvar):
	abs_path = os.path.abspath(pathvar)
print(abs_path)


# ### 作业题: 计算一个文件夹中的所有文件的大小












