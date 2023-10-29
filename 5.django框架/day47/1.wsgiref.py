
from wsgiref.simple_server import make_server

# wsgiref本身就是个web框架,提供了一些固定的功能(请求和响应信息的封装,不需要我们自己写原生的socket了也不需要咱们自己来完成请求信息的提取了,提取起来很方便)
# 函数名字随便起
def application(environ, start_response):
	"""
	:param environ: 是全部加工好的请求信息,加工成了一个字典,通过字典取值的方式就能拿到很多你想要拿到的信息
	:param start_response: 帮你封装响应信息的(相应行和响应头),注意下面参数
	:return
	"""
	start_response('200 OK', [('k1', 'v1'), ('k2', 'v2')])
	print(environ)
	# 输入地址127.0.0.1:8080,这个打印的是'/',输入地址127.0.0.1:8080/index,打印结果是'/index'
	print(environ['PATH_INFO'])

	return [b'<h1>Hello, Web!</h1>']

# 和socketserver那个模块很像
httpd = make_server('127.0.0.1', 8080, application)

print('Serving HTTP on port 8080...')
# 开始监听请求
httpd.serve_forever()