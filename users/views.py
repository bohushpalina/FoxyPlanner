from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegisterForm

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
