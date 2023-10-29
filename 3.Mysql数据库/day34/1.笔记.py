# ### mysql关系型数据库

"""
[快捷键]
快捷键: ctrl + l 清屏
快捷键: ctrl + c 终止
exit:  退出数据库
\q:    退出
\G:    垂直显示

[linux] mysql服务命令
server mysql stop
server mysql start
server mysql restart

[windows] mysql服务命令
net stop mysql
net start mysql
"""

# ### part1
# (1) 登录
"""
# 登录的完整语法
mysql -u用户 -p密码 -hIP地址
mysql -uroot -p -h默认本地ip
localhost => 127.0.0.1
# (2) 退出
exit 或者 \q
"""

# ### part2
"""
# 查询当前登录用户
select user()
# 设置密码
set password = password("123456")
# 去除密码
set password = password("")
"""

# part3
"""
VMnet8: nat
WMnet1: host-only
ipconfig [windows] ifconfig [linux]

# 给具体某个ip设置一个账户连接mysql
create user "ceshi100"@"192.168.126.1" identified by "111";
# 给具体192.168.126.%这个网段下的所有ip设置账户
create user "ceshi101"@"192.168.126.%" identified by "222";
# 给所有ip下的主机设置账户
create user "ceshi102"@"%" identified by "333";

USAGE 没有任何权限
# 查看具体某个ip下的用户权限
show grants for "ceshi102"@"%";
+--------------------------------------+
| Grants for ceshi102@%                |
+--------------------------------------+
| GRANT USAGE ON *.* TO 'ceshi102'@'%' |
+--------------------------------------+

# 授权语法
grant 权限 on 数据库.表 to "用户名"@"ip地址" identified by "密码";
'''
select 查询数据的权限
insert 添加数据的权限
update 更改数据的权限
delete 删除数据的权限
all	   所有权限
*	   所有
'''
# 授权查询权限
grant select,insert on *.* to "ceshi102"@"%" identified by "333";
# 授权所有权限
grant all on *.* to "ceshi102"@"%" identified by "333";
# 移除删除权限(删除数据库/表)
revoke drop on *.* from "ceshi102"@"%";
# 移除所有权限
revoke all on *.* from "ceshi102"@"%";
# 刷新权限,立即生效
flush privileges
"""

# ### part4 [必须熟练]
"""
mysql命令中,不区分大小写
[linux] 路径
sudo find / -name db001
sudo su root 切换到最高权限账户
cd /mysql
/var/lib/mysql/数据库...

[windows] 路径
D:\MySQL5.7\mysql-5.7.25-winx64\data
"""

"""
# (1) 操作数据库 [文件夹]
# 增:
	# 创建数据库
	creat database db001 charset utf8;
# 查:
	# 查看数据库
	show database;
	# 查看建库语句
	show create database db001;
	+----------+----------------------------------------------------------------+
	| Database | Create Database                                                |
	+----------+---------------------------    -------------------------------------+
	| db001    | CREATE DATABASE `db001` /*!40100 DEFAULT CHARACTER SET utf8 */ |
	+----------+----------------------------------------------------------------+
	CREATE DATABASE `db002` /*!40100 DEFAULT CHARACTER SET utf8 */
# 改:
	# 修改数据库编码集
	alter database db002 charset gbk;
# 删:
	# 删除数据库
	drop database db001;

# (2) 操作数据表 [文件]
# 增:
	# 选择数据库
	use tables;
	# 创建表
	create table t1(id int, name char);
# 查:
	# 查看所有表
	show tables;
	# 查看建表语句
	show create table t1;
	'''
	Table: t1
	Create Table: CREATE TABLE `t1` (
	  `id` int(11) DEFAULT NULL,
	  `name` char(1) DEFAULT NULL
	) ENGINE=InnoDB DEFAULT CHARSET=utf8
	1 row in set (0.00 sec)
	'''
	# 查看表结构
	desc t1;
	+-------+---------+------+-----+---------+-------+
	| Field | Type    | Null | Key | Default | Extra |
	+-------+---------+------+-----+---------+-------+
	| id    | int(11) | YES  |     | NULL    |       |
	| name  | char(1) | YES  |     | NULL    |       |
	+-------+---------+------+-----+---------+-------+
# 改:
	# modify 只能改变类型
	alter table t1 modify name char(5);
	# change 改变类型+字段名
	alert table t1 change name name123 char(4);
	# add 添加字段
	alter table t1 add gae int;
	# drop 删除字段
	alter table t1 drop age;
	# rename 更改表名
	alter table t1 rename t111111;
# 删:
	grop table t1;

# (3) 操作记录 [文件的内容]
# 增:
	# 一次插入一条数据
	insert into t1(id, name) values(1, "abcd");
	# 一次插入多条数据
	insert into t1(id, name) values(2, "wangwen"), (3, "liuwenbo"), (4, "康裕康");
	# 不指定具体字段,默认把字段全部插一遍
	insert into t1 values(6, "沈思雨");
	# 可以具体指定某个字段进行插入
	insert into t1(name) values("张宇");
# 查:
	# * 所有
	select * from t1;
	# 查询单个字段
	select id from t1;
	# 查询多个字段
	select id, name from t1;
# 改:
	# update 表名 set 字段=值 where 条件
	update t1 set name = "王伟" where id = 2;
	# 不加条件有风险,一改全改,一定加where
	update t1 set name = "王伟";
# 删:
	# 删除的时候,必须加上where
	delete from t1 where id = 1;
	# 删除所有数据,一删全删,一定加where
	delete from t1;
	# 删除所有(数据 + 重置id)
	truncate table t1;
"""

# ### part5 常用数据类型
"""
# 整型
'''
tinyint 1个字节 有符号范围(-128~127) 无符号(0~255) unsigned 小整型值
int		4个字节 有符号范围(-21亿~21亿左右) 无符号(0~42亿) 大整型值
'''
	create table t3(id int, sex tinyint);
	insert into t3(id, sex) values(4000000000, 127); # error out of range
	insert into t3(id, sex) values(13, 128); # error out of range
	insert into t3(id, sex) values(13, 127);

# 浮点型
'''
float(255, 30)	单精度
double(255, 30) 双精度
decimal(65, 30) 金钱类型(用字符串的形式来存储小数)
'''
	# 整数位最多保留2位,小数位最多保留3位,存在四舍五入
	create table t4(f1 float(5,3), f2 double(5,3), f3 decimal(5,3));
	insert into t4 values(1.77777777777777777, 1.7777777777777777, 1.7777777777777777);
	insert into t4 values(11.7777777777777777, 11.777777777777777, 11.777777777777777);
	insert into t4 values(111.777777777777777, 111.77777777777777, 111.77777777777777);	# error out of range
	insert into t4 values(1.7, 1.7, 1.7);

	# float 小数位默认保留5位, double 小数位默认保留16位, decimal默认保留整数,四舍五入
	create table t5(f1 float, f2 double, f3 decimal);
	insert into t5 value(1.7777777777777777777777777, 1.7777777777777777777777777, 1.7777777777777777777777777);

	create table t6(f1 float(7,3));
	insert into t6 values(1234.5678);
	+----------+
	| f1       |
	+----------+
	| 1234.568 |
	+----------+
	# 整数位最多保留4位, 小数位最多保留3位
	# 默认double保留的小数位更多,float保留的小数位少;decimal保留整数位
	insert into t6 values(12345.67)

# 字符串 char(字符长度) varchar(字符长度)
'''
char(11)	定长:固定开辟11个字符长度的空间(手机号, 身份证号),开辟空间的速度上来说比较快,从数据结构上来说,需谨慎,可能存在空间浪费 max = > 255
varchar(11) 变长:动态最多开辟11个字符长度的空间(评论,广告),开辟空间的速度上来说相对慢,从数据结构上来说,推荐使用,不存在空间浪费 max > 255
text		文本类型:针对于文章,论文,小说 max > varchar
'''
	create table t7(c char(11), v varchar(11), t text);
	insert into t7 values("11111", "11111", "11111");
	insert into t7 values("你好啊你好啊你好啊你好", "你好啊你好啊你好啊你好", "你好啊你好啊你好啊你好");
	# concat 可以把各个字段拼接在一起
	select concat(c, "<==>", v, "<=>", t) from t7;

# 数据库内部方法
select user()
select concat()
select database()
select now()

# 枚举和集合
enum 枚举: 从列出来的数据当中选一个(性别)
set  集合: 从列出来的数据当中选多个(爱好)

creat table t8(
id int,
name varchar(11),
sex enum("男性","兽性","人妖"),
money float(5,3),
hobby set("吃肉","抽烟","喝酒","打麻将","嫖赌")
);

# 正常写法
insert into t8(id, name, sex, money, hobby) values(1, "张保张", "兽性", 2.6, "打麻将,吃肉,嫖赌");
# 自动去重
insert into t8(id, name, sex, money, hobby) values(1, "张保张", "兽性", 2.6, "打麻将,吃肉,嫖赌,嫖赌,嫖赌");
# 异常写法: 不能选择除了列出来的数据之外的其他值(error 报错)
insert into t8(id, name, sex, money, hobby) values(1,"张保障","人妖12",2.6,"打麻将,吃肉,嫖赌12");
"""










