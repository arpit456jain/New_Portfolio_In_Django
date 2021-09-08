from django.contrib import admin
from django.urls import path,include
from StringAnalyzerApp import views

urlpatterns = [
        
    path('',views.index,name = 'index'),
    path("analyse/", views.analyse, name='analyse'),
    path('registration/',include('registration.urls')),
]