# ### os 模块(文件操作) 新建/删除
import os

os.chdir("/home/wangwen/mywork")
# -- os模块具有 新建/删除
# os.mkond 创建文件
os.mknod("1.txt")

# os.remove 删除文件
os.remove("1.txt")

# os.mkdir 创建目录(文件夹)
os.mkdir("ceshi111")

# os.rmdir 删除目录(文件夹)
os.rmdir("ceshi111")

# os.rename 对文件,目录重命名
os.rename("2.txt", "3.txt")

# os.makedirs 递归创建文件夹
os.makedirs("a/b/c/d/e/f")

# os.removedirs 递归删除文件夹(空文件夹)
os.removedirs("a/b/c/d/e/f")

# ### shutil模块 复制/移动
import shutil
# copyfileobj(fsrc, fdst, length=16*1024) 复制文件(length的单位是字符(表达一次读多少字符/字节))
"""
fp_src = open("3.txt", mode="r", encoding="utf-8")
fp_dst = open("4.txt", mode="w", encoding="utf-8")
shutil.copyfileobj(fp_src, fp_dst)
"""
# copyfile(src,dst)	单纯的仅复制文件内容,地城调用了copyfileobj
shutil.copyfile("4,txt", "5.txt")

# copymode(src,dst)	单纯的仅复制文件权限,不包括内容(虚拟机共享目录都是默认777)
"""注意:要先有两个文件才可以,不会默认创建"""
shutil.copymode("4.txt", "5.txt")

# copystat(src,dst)	复制所有状态信息,包括权限,组,用户,修改时间等,不包括内容
shutil.copystat("5.txt", "6.py")

# copy(src,dst)	复制文件权限和内容
shutil.copy("5.txt", "6.py")

# copy2(src,dst) 复制文件权限和内容,还包括权限,组,用户,时间等
shutil.copy2("5.txt","7,py")

# copytree(src,dst) 拷贝文件夹里所有内容(递归拷贝)
shutil.copytree("lianxi", "lianxi2")

# rmtree(path) 删除当前文件夹及其中所有内容(递归删除)
shutil.rmtree("lianxi2")

# move(path1,path2) 移动文件或文件夹
# shutil.move("7.py", "lianxi/888.php")
shutil.move("7.py", "/888.php")















