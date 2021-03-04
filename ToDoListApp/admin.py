from django.contrib import admin

# Register your models here.
from ToDoListApp.models import Task

admin.site.register(Task)