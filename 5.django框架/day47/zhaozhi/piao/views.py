from django.shortcuts import render

# Create your views here.

def home(request):
	print(request.path)
	current_user = "子龙"
	ret = render(request, 'home.html', {"username": current_user})
	return ret
