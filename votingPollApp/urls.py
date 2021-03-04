
from django.contrib import admin
from django.urls import path,include
from votingPollApp import views
urlpatterns = [
    path('',views.index,name="indexs"),
    path('getQuery',views.getQuery,name="getQuery"),
    path('feedback/',views.feedback,name="feedback"),
]
