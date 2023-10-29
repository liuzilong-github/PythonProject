from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def login(request):
	print('login>>>>>')
	if request.method == "GET":
		return render(request, 'login.html')
	username = request.POST.get('username')
	if username == 'root':
		request.session['is_login'] = True
		return redirect('index')
	else:
		return redirect('login')


def index(request):
	print('index>>>>>')
	return HttpResponse('index')
