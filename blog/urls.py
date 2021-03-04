from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('search/', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('postComment',views.postComment,name="postComment"),
    path('<str:slug>', views.blogPost, name="blogPost"),
]