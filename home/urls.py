from django.contrib import admin
from django.urls import path,include
from home  import views

admin.site.site_header = "Arpit Jain"
admin.site.site_title = " developed by Arpit Jain"
admin.site.index_title = "Portfolio"



urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('worksample',views.worksample,name='worksample'),
    path('djangoProjects',views.djangoProjects,name='djangoProjects'),
]
