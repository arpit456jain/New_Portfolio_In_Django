from django.db import models

# Create your models here.
class Contact(models.Model):

    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    phone= models.CharField(max_length=13)
    email= models.CharField(max_length=100)
    content= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        
         return self.name + "  with email  " + self.email



# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    views= models.IntegerField(default=0)

    def __str__(self):
        return self.title + " by " + self.author



from django.contrib.auth.models import User
from django.utils.timezone import now

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
  

    def __str__(self):
        return self.comment[0:10] + ".... by " + str(self.user)
