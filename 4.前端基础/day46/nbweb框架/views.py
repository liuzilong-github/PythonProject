
import time

# def html(conn):
# 	# 连接数据库,拿数据,将数据添加到html文件中,到页面展示
# 	now = str(time.time())
# 	with open('templates/beatfulpage.html', 'r', encoding='utf-8') as f:
# 		data = f.read()
# 	data = data.replace('%xxoo%', now).encode('utf-8')
#
# 	conn.send(data)
#
# 	conn.close()
# # return data
#
# def css(conn):
# 	with open('statics/xx.css', 'rb') as f:
# 		data = f.read()
# 	# return data
# 	conn.send(data)
#
# 	conn.close()
# def jpg(conn):
# 	with open('statics/1.jpg', 'rb') as f:
# 		data = f.read()
# 	# return data
# 	conn.send(data)
#
# 	conn.close()
# def js(conn):
# 	with open('statics/xx.js', 'rb') as f:
# 		data = f.read()
# 	# return data
# 	conn.send(data)
#
# 	conn.close()
# def person(conn):
# 	with open('templates/person.html', 'rb') as f:
# 		data = f.read()
# 	# return data
# 	conn.send(data)
# 	conn.close()

# 必须要写一个conn形参
def index(conn):
	with open('templates/index.html', 'rb') as f:
			data = f.read()
		# return data
	conn.send(data)
	conn.close()



