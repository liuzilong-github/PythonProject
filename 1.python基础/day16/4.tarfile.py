# ### tarfile 压缩模块
import tarfile

# (1) 压缩文件

# 1.只是单纯的打包
# 创建压缩包
tf = tarfile.open("ceshi0930_0.tar","w",encoding="utf-8")
# 写入文件
"""add(路径,别名)"""
tf.add("/bin/chown", "chown")
tf.add("/bin/cp", "cp")
tf.add("/bin/dash", "tmp/dash")
# 关闭文件
tf.close()	# 378880

# 2.使用gz算法压缩
tf = tarfile.open("ceshi0930_1.tar.gz","w:gz",encoding="utf-8")
# 写入文件
"""add(路径,别名)"""
tf.add("/bin/chown", "chown")
tf.add("/bin/cp", "cp")
tf.add("/bin/dash", "tmp/dash")
# 关闭文件
tf.close()	# 180413

# 3.使用bz2算法压缩
tf = tarfile.open("ceshi0930_2.tar.bz2","w:bz2",encoding="utf-8")
# 写入文件
"""add(路径,别名)"""
tf.add("/bin/chown", "chown")
tf.add("/bin/cp", "cp")
tf.add("/bin/dash", "tmp/dash")
# 关闭文件
tf.close()	# 163261


# (2) 解压文件
tf = tarfile.open("ceshi0930_1.tar.gz","r",encoding="utf-8")
""" extract(文件,路径) 解压单个文件 """
tf.extract("chown", "ceshi0930_1")
""" extract(路径) 解压所有文件 """
tf.extractall("ceshi0930_1_2")
tf.close()


# (3) 追加文件
"""对已经压缩的包文法进行追加文件,只能是没有压缩过的包进行追加文件"""
tf = tarfile.open("ceshi0930_0.tar","a",encoding="utf-8")
tf.add("/bin/mkdir", "mkdir")
tf.close()

# 使用with进行改造
with tarfile.open("ceshi0930_0.tar","a",encoding="utf-8") as tf:
	tf.add("/bin/mkdir", "mkdir234")


# (4) 查看文件
with tarfile.open("ceshi0930_0.tar","r",encoding="utf-8") as tf:
	lst = tf.getnames()
	print(lst)


# ### 追加文件到压缩包中在压缩
import os, shutil
"""
1.把已经压缩的包进行解压
2.把要追加的内容放进去
3.过滤文件重新压缩
"""
# 记录压缩包所在的绝对路径
pathvar1 = os.path.abspath("ceshi0930_2.tar.gz")
# 要解压到哪个文件夹中(绝对路径)
pathvar2 = os.path.join(os.getcwd(), "ceshi0930_2")
print(pathvar1) # /mnt/hgfs/python32_gx/day16/ceshi0930_2.tar.bz2
print(pathvar2) # /mnt/hgfs/python32_gx/day16/ceshi0930_2

# 1.把已经压缩的包进行解压
with tarfile.open(pathvar1,"r",encoding="utf-8") as tf:
	tf.extractall(pathvar2)

# 2.把要追加的内容放进去
shutil.copy("/bin/echo", pathvar2)

# 3.过滤文件重新压缩
# 查看文件夹中有什么文件
lst = os.listdir(pathvar2)
print(lst) # ['chown', 'cp', 'echo', 'tmp']

with tarfile.open(pathvar1,"w:bz2",encoding="utf-8") as tf:
	for i in lst:
		if i != "chown":
			# 拼凑成完整的绝对路径
			abs_path = os.path.join(pathvar2,i)
			# 剩下的都要压缩
			"""add(路径,别名)"""
			tf.add(abs_path,i)
"""
	/mnt/hgfs/python32_gx/day16/ceshi0930_2/chown
	/mnt/hgfs/python32_gx/day16/ceshi0930_2/cp
	/mnt/hgfs/python32_gx/day16/ceshi0930_2/echo	
	tf.add("/bin/chown","chown")
"""












