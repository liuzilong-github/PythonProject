
import pymysql

def create_model():

	conn = pymysql.connect(
		host='127.0.0.1',
		port=3306,
		user='root',
		password='',
		database='nbweb',
		charset='utf-8'
	)
	cursor = conn.cursor()

	sql = 'creat table userinfo(id int primary key auto_increment, name char(10) not null age int unsigned);'
	cursor.execute(sql)
	conn.commit()

	conn.close()