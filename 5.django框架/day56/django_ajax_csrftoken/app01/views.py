from django.shortcuts import render, HttpResponse
import json

# Create your views here.

'''
解析器:
a = request.META['content-type']

if a == 'application/x-www-form-urlencoded':
    data = request.body     -- a=1&b=2
    l1 = data.split('&')
    for i in l1:
        k,v = i.split('=')
        request.post[k] = v
elif a == 'multipart/form-data':    文件片段数据格式
    request.FILES[]
'''


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # data = request.POST
        # print(data)    # <QueryDict: {'xname': ['yuantao'], 'pwd': ['666']}>
        # print(request.body)    # b'xname=asdf&pwd=123'
        data = request.body
        data = data.decode()
        data = json.loads(data)
        print(data, type(data))    # {'xname': 'asdf', 'pwd': '123'} <class 'dict'>
        username = data.get('xname')
        password = data.get('pwd')
        if username == 'admin' and password == '123456':
            return HttpResponse('ok')
        # ret = render(request, 'login.html', {'error': '用户名或密码错误!', 'username': username, 'password': password})
        ret = HttpResponse('not ok')
        ret.status_code = 400
        return ret








