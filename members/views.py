from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


# View to login user
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('home')
        else:
            # Message for unsuccessfull login
            messages.success{request, ("Login Error, Try Again.")}
        pass
    else:
        return render(request, 'login.html')

