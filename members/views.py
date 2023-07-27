from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
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
            messages.success(request, ("Login Error, Try Again."))
            return redirect('login')
    else:
        return render(request, 'login.html')


# View to Logout User
def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Logged Out"))
    return redirect('home')


# View To Create User
def register_user(request):
    return render(request, 'register_user.html', {})
