from django.contrib import admin
from django.urls import path,include
from ToDoListApp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.task, name='task'),
    path('search/', views.search, name='search'),
    path('deleteitem/<str:slug>', views.deleteitem, name='deleteitem'),
]
