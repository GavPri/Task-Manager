from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# View to login user
def login_user(request):
    return render(request, 'login.html')

