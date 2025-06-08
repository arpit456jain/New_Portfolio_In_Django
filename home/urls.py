from django.contrib import admin
from django.urls import path,include
from home  import views

admin.site.site_header = "Arpit Jain"
admin.site.site_title = " developed by Arpit Jain"
admin.site.index_title = "Portfolio"



urlpatterns = [
    path('',views.portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
    path('worksample',views.worksample,name='worksample'),
    path('projects',views.projects,name='projects'),
]
