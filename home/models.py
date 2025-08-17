from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    content = models.TextField(max_length=400)
    number  = models.CharField(max_length=10)

    def __str__(self):
        return (self.name)
    

class ImportantLink(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)   
    url = models.URLField(max_length=500)
    icon = models.CharField(max_length=50, blank=True, null=True) 

    def __str__(self):
        return self.title