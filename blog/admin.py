from django.contrib import admin

# Register your models here.
from .models import Contact,Post, BlogComment

# Register your models here.
admin.site.register((Contact,BlogComment))


# # for tiny text editor
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)