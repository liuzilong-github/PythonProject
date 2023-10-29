from django.shortcuts import render, redirect

# Create your views here.


# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         if username == 'root' and password == '123456':
#             ret = redirect('home')
#             ret.set_cookie('is_login', 'xxx')   # 设置cookie,如果有同名的(键)cookie,那么就是修改cookie
#             ret.set_cookie('username', username)
#             return ret
#         return redirect('login')
#
#
# def home(request):
#     # ret = render(request, 'home.html')
#     # ret.set_cookie('is_login', True)    # 键相同,就是修改cookie
#     print('>>>>>>', request.COOKIES)    # {'is_login': 'True', 'username': 'root'}  字典数据
#     status = request.COOKIES.get('is_login')    # 获取请求携带的cookie数据
#     print(status, type(status))
#     if status == 'xxx':
#         return render(request, 'home.html')
#     else:
#         return redirect('login')
#
#
# def cart(request):
#     print('>>>>>', request.COOKIES)
#     status = request.COOKIES.get('is_login')
#     print(status, type(status))
#     if status == 'xxx':
#         cart_list = ['女朋友1', '欧美女朋友', ]
#         return render(request, 'cart.html', {'cart_list': cart_list})
#     else:
#         return redirect('login')
#
#
# def logout(request):
#     ret = redirect('login')
#     ret.delete_cookie('is_login')
#     return ret


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'root' and password == '123456':
            request.session['is_login'] = True
            request.session['username'] = username
            '''
            1.生成随机字符串
            2.加入到cookie中, {seesionid: 'asdfasdfasdf'}
            3.将设置的session数据(is_login, username...),序列化然后加密保存到数据库中,django-session表
            '''
            return redirect('home')
        return redirect('login')


def home(request):
    # status = request.session['is_login']
    status = request.session.get('is_login')
    '''
    1.取出cookie中的sessionid对应的字符串
    2.通过随机字符串去django-session表中找到对应记录
    3.将记录中的session_data的数据进行解密,并反序列化,然后取出键对应的值
    '''
    if status:
        return render(request, 'home.html')
    else:
        return redirect('login')


def cart(request):
    cart_list = ['女朋友1', '欧美女朋友']
    status = request.session.get('is_login')
    if status:
        return render(request, 'cart.html', {'cart_list': cart_list})
    else:
        return redirect('login')


def logout(request):
    request.session.flush()
    '''
    1.删除cookie中的sessionid值
    2.删除数据库中对应记录(本次请求cookie中的sessionid的值对应的记录)
    '''
    return redirect('login')