from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    taskTitle = models.CharField(max_length=30)
    TaskDesc = models.TextField(max_length=300)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle