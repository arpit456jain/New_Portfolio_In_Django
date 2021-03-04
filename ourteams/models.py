from django.db import models

# Create your models here.

class OurGallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    img = models.ImageField(upload_to="static/ourteams/media")
    jobrole = models.CharField(max_length=100,blank=True)
    phone_number = models.IntegerField(blank=True)
    fb_url = models.CharField(max_length=100,blank=True,default="#")
    insta_url = models.CharField(max_length=100,blank=True,default="#")
    github_url = models.CharField(max_length=100,blank=True,default="#")
    linkedn_url = models.CharField(max_length=100,blank=True,default="#")
    
    def __str__(self):
        return self.name