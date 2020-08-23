from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 



class MyCar(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/')
    owner = models.CharField(max_length=50,null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    year = models.IntegerField(default=2000)
    created_at = models.DateTimeField(default=timezone.now)

    
    
    def __str__(self):
        return "{}'s {}".format(self.owner, self.brand)



class Comment(models.Model):
    car =models.ForeignKey(MyCar,related_name='comments', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField() 
    created_date =models.DateTimeField(default=timezone.now)   
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True 
        self.save()
