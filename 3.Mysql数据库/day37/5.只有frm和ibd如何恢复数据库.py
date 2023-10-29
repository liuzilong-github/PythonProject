# innerdb 在只有frm和idb文件的情况下,如何恢复数据

"""
# 1.安装 MYSQL Utilities
https://downloads.mysql.com/archives/utilities/

# 2.cmd中找到frm那个文件,执行如下命令
切换到对应目录,执行下面语句,不要加分号
mysqlfrm --diagnostic ./文件目录/t1.frm
查出建表语句,复制查询出来的建表语句在mysql中创建的新数据中使用

# 3.对已创建的表进行表空间卸载,删除ibd文件
alter table innerdb1 discard tablespace;

# 4.把要恢复的idb文件替换进去

# 5.对已创建的表进行空间装载
alter table innerdab1 import tablespace;

CREATE TABLE `innodb1` (
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB;
"""






