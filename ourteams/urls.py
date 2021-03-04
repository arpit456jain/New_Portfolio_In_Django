from django.contrib import admin
from django.urls import path,include
from ourteams import views
urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.loginuser,name="login"),
    path("signup",views.signupuser,name="signup"),
    path("logout",views.logoutuser,name="logout"),
    path("delete/<str:slug>",views.delete,name="delete"),
    path("edit/<str:slug>",views.edit,name="edit"),
]