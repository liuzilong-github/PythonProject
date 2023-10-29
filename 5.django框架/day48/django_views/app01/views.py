from django.shortcuts import render, HttpResponse, redirect
from django.views import View

# Create your views here.


def login(request):
    print(request)  # <WSGIRequest: GET '/login/?a=1&b=2'> WSGIRequest类的实例化对象
    print(request.method)
    print(request.POST)
    print(request.GET)  # request.GET.get('a') == 1
    print(request.path) # 获取当前请求路径
    print(request.get_full_path())  # 获取当前请求路径包含查询参数
    print(request.META) # 获取所有请求头的信息 {''HTTP_USER_AGENT':'asdfasdfasdf',....}
    # request.META 字典类型数据,所有的请求头的键前面都加上了一个HTTP_键名称
    # return HttpResponse('ok')
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        uname = request.POST.get("username")
        if uname == 'shiyuan':
            # return redirect('/home/')   # redirect的参数是一个路径
            return render(request, 'home.html')

def home(request):
    book = "测试"
    return render(request, 'home.html', {'book': book})

def index(request):
    re = HttpResponse("xx")
    # re = render(request, 'xxx')
    # re = redirect('/home/')
    re['name'] = 'gaodaao'  # 添加响应头键值对
    re.status_code = 404    # 修改状态码
    return re


class BookView(View):
    # get, post
    # 通过反射获取到请求方法对应的类中的方法进行执行
    def get(self, request):
        return HttpResponse('ok')

    """
        def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
    """


from django.utils.decorators import method_decorator

def func(f):
    def inner(*args, **kwargs):
        print("111111")
        ret = f(*args, **kwargs)
        print("222222")
        return ret
    return inner


# @method_decorator(func, name="get")   # CBV方法通过装饰器来进行扩展(方式三)
# @method_decorator(func, name="post")
class ArticlesView(View):

    # 重写dispatch方法来进行扩展
    # @method_decorator(func)   # CBV方法通过装饰器来进行扩展(方式二)
    # def dispatch(self, request, *args, **kwargs):
    #     print("111111")
    #     ret = super(ArticlesView, self).dispatch(request, *args, **kwargs)
    #     print("222222")
    #     return ret

    @method_decorator(func)     # CBV方法通过装饰器来进行扩展(方式一)
    def get(self, request, year):
        print(year)
        return render(request, 'articles.html')

    @method_decorator(func)
    def post(self, request, year):
        print(request.POST)
        return HttpResponse('ok')