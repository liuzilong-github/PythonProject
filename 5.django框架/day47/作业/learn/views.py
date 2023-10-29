from django.shortcuts import render

# Create your views here.


def login(request):
	if request.method == "GET":
		return render(request, "login.html")
	else:
		uname = request.POST.get("uname")
		pwd = request.POST.get("pwd")
		print(uname, pwd)
		if uname == "root" and pwd == "123456":
			return render(request, "home.html", {"username": uname})
		else:
			return render(request, "error.html")
