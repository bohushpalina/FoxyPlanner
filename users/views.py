from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

@login_required
def profile(request):
    return render(request, "users/profile.html", {"user": request.user})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Шифруем пароль
            user.save()
            login(request, user)  # Авторизуем пользователя после регистрации
            return redirect("home")  # Редирект на главную (поменяй, если надо)
    else:
        form = RegisterForm()
    
    return render(request, "users/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Перенаправляем на страницу, с которой пытался войти
        else:
            messages.error(request, "Неверный логин или пароль")
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")