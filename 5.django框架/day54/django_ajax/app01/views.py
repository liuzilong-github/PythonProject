from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

import json

# Create your views here.


# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         data = request.POST
#         print('data>>>>>>', data)    # <QueryDict: {'username': ['liuzilong'], 'password': ['123']}>
#         username = data.get('username')
#         password = data.get('password')
#         if username == 'yuantao' and password == '123456':
#             return HttpResponse('ok')
#         # return render(request, 'login.html', {'error': '用户名或密码有误', 'username': username, 'password': password})
#         ret = HttpResponse('not ok')
#         ret.status_code = 400
#         return ret


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        data = request.POST
        print('data>>>>>>', data)    # <QueryDict: {'xname': ['yuantao'], 'pwd': ['123456']}>
        username = data.get('xname')
        password = data.get('pwd')
        if username == 'yuantao' and password == '123456':
            return HttpResponse('ok')
        # return render(request, 'login.html', {'error': '用户名或密码有误', 'username': username, 'password': password})
        ret = HttpResponse('not ok')
        ret.status_code = 400
        return ret


# def index(request):
#     userinfo = {
#         'name': '春培',
#         'age': 18
#     }
#     userinfo_st = json.dumps(userinfo, ensure_ascii=False)
#     # return HttpResponse('ok')
#     # ret = HttpResponse(userinfo_st)
#     # ret['content_type'] = 'application\json'
#     # return HttpResponse(userinfo_st, content_type='application\json')
#     return JsonResponse(userinfo)


def index(request):
    userinfo = {
        'name': '春培',
        'age': 18
    }
    return JsonResponse(userinfo)


# def food(request):
#     food_list = ['黄瓜', '茄子', '香蕉', '萝卜', '冬瓜']
#     food_str = json.dumps(food_list)
#     return HttpResponse(food_str)


def food(request):
    food_list = ['黄瓜', '茄子', '香蕉', '萝卜', '冬瓜']
    return JsonResponse(food_list, safe=False)


def mylogin(request):
    return render(request, 'mylogin.html')


def myregister(request):
    return render(request, 'myregister.html')
