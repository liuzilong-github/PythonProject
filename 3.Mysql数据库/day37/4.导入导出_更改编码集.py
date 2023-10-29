# ### (1) 导入导出 不要加分号
"""
导出数据库
1.退出mysql
2.选择要导出的默认路径
3.mysqldump -uroot -p db001 > db001.sql

导入数据库
1.登录到mysql之后
2.创建新的数据库
3.source 路径+文件
"""

# ### (2) 配置linux下的编码集
"""
!includedir /etc/mysql/conf.d	# 客户端的修改
# 设置mysql客户端默认字符集
default-character-set=utf8
!includedir /etc/mysql/mysql.conf.d		# 服务端的修改
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8

service mysql restart
"""





