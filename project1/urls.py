"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from calculatorApp import 
from project1 import views
admin.site.site_header="Arpit Jain is Admin"
admin.site.site_title="CodeSmashers Admin Panel"
admin.site.index_title="Welcome to CodeSmashers Admin Panel"
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    # path('', views.home, name='home'),
    path('',include("home.urls")),# main Portfolio
    path('calculator/',include("calculatorapp.urls")),
    path('votingPollApp/',include("votingPollApp.urls")),
    path('ToDoListApp/',include("ToDoListApp.urls")),
    path('stringAnalyzer/',include("StringAnalyzerApp.urls")),
    path('ourteams/',include("ourteams.urls")),
    path('myblog/', include('blog.urls')),
]
