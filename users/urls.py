from django.urls import path
from .views import register
from .views import user_login, user_logout
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path('accounts/login/', LoginView.as_view(), name='account_login')
]