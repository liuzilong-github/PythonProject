# ### sql 注入攻击
import pymysql

# (1) sql注入的现象
# 现象: 绕开账号密码登录成功
user = input("请输入您的用户名>>>")
pwd = input("请输入您的密码>>>")

conn = pymysql.connect(host="127.0.01.1", user="root", password="123456", database="test")
cursor = conn.cursor()
sql1 = """
create table usr_pwd(
id int unsigned primary key auto_increment,
username varchar(255) not null
password varchar(255) not null
)
"""
sql2 = "select from usr_pwd where username = '%s' and password = '%s' " % (user, pwd)
print(sql2)
res = cursor.execute(sql2)
print(res)	# 1 查到成功 0 没查到失败
res = cursor.fetchone()
"""
select * from usr_pwd where username='2222' or 4=4 -- aaa' and password='';
相当于: select * from usr_pwd where 10 = 10;
绕开了账户和密码的判断 -- 代表的是注释;
"""
if res:
	print("登录成功")
else:
	print("登录失败")

cursor.close()
conn.close()

# (2) 预处理机制
"""
在执行sql语句之前,提前对sql语句中出现的字符进行过滤优化,避免sql注入攻击
execute(sql, (参数1, 参数2, 参数3 ... )) execute 2各参数默认开启预处理机制
填写 234234 or 100 = 100 -- sadadaddasas 尝试攻击
"""
user = input("请输入您的用户名>>>")
pwd = input("请输入您的密码>>>")

conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", database="test")
cursor = conn.cursor()
sql = "select * from usr_pwd where username = %s and password = %s"
res = cursor.execute(sql, (user, pwd))
print(res)

print("登录成功" if res else "登录失败")

cursor.close()
conn.close()















