# ### python 操作mysql
import pymysql

# ### 1.基本语法
"""
# (1) 创建连接对象 host user password database 这四个参数必写
conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="test", charset="utf8", port=3306)
# (2) 创建游标对象(用来操作数据库的增删改查)
cursor = conn.cursor()
print(cursor)
# (3) 执行sql语句
sql = "select * from employee"
# 执行查询语句返回总条数
res = cursor.execute(sql)
print(res)
# (4) 获取数据 fetchone 获取一条数据
# 返回的是元组,里面包含的是第一条的完整数据
res = cursor.fetchone()
print(res)
res = cursor.fetchone()
print(res)
res = cursor.fetchone()
print(res)
# (5) 释放游标对象
cursor.close()
# (6) 释放连接对象
conn.close()
"""


# ### 2.创建/删除 表操作
conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="test")
cursor = conn.cursor()

# (1) 创建一张表
sql = """
create table t1(
id int unsigned primary key auto_increment,
first_name varchar(255) not null,
last_name varchar(255) not null,
sex tinyint not null,
age tinyint unsigned not null,
money float
);
"""
res = cursor.execute(sql)
print(res)	# 无意义的返回值

# (2) 查询表结构
sql = "desc employee"
res = cursor.execute(sql)
print(res)	# 返回的是字段的个数
res = cursor.fetchone()
print(res)
res = cursor.fetchone()
print(res)
res = cursor.fetchone()
print(res)

# (3) 删除表
try:
	sql = "drop table employee"
	res = cursor.execute(sql)
	print(res)	# 无意义的返回值
except:
	pass


# ### 3.事务处理
# pymysql 默认是开启事务的,所有增删改的数据必须提交,否则默认回滚; rollback
conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="test")
cursor = conn.cursor()
sql1 = "begin"
sql2 = "update employee set emp_name = '程咬钻石' where id = 18"
sql3 = "commit"

res1 = cursor.execute(sql1)
res1 = cursor.execute(sql2)
res1 = cursor.execute(sql3)

# 一般在查询的时候,通过fetchone来获取结果
res1 = cursor.fetchone()
print(res1)

cursor.close()
conn.close()











