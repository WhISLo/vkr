from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('profile')
    return render(request, 'authorization/register.html')  # , {'form': form}


def login_view(request):
    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('profile')
    return render(request, 'authorization/login.html')  # , {'form': form}


def logout_view(request):
    logout(request)
    return redirect('login')
