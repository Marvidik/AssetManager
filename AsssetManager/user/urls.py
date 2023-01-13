from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import   checkuser,checkuser2,emailcheck,Register 

urlpatterns = [
    path("register",Register.as_view(),name="register"),
    path("",LoginView.as_view(template_name="user/login.html"),name="login"),
    path("usercheck/",checkuser,name="usercheck"),
    path("usercheck2/",checkuser2,name="usercheck2"),
    path("emailcheck/",emailcheck,name="emailcheck")
]
