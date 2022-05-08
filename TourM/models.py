from audioop import reverse
from django.db import models
from django.urls import reverse
from .models import Comment
from ckeditor.fields import RichTextField

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Provinces(models.Model):
    Provinces = models.CharField(max_length=255)

    def __str__(self):
        return self.Provinces     
    def get_absolute_url(self):
        return reverse('homeView')


class Post(models.Model):
    title = models.CharField(max_length=255)
    creator =models.CharField(default='The company',max_length=255 )  
    body = RichTextField()
    days = models.PositiveIntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    price = models.IntegerField(default='',null=False)
    Provinces = models.CharField(max_length=255, null=False)
    Size = models.PositiveIntegerField(default='1', validators=[MaxValueValidator(100),MinValueValidator(1)])      #group size {if paxi availability add garne bhe useful}
    Hoster=models.CharField(max_length=255, null=False)
    pack_img = models.ImageField(null = True, blank=True, upload_to="pacImages/")
   
    def __str__(self):
        return self.title + ' | '+ str(self.creator) 

    
    def get_absolute_url(self):
        return reverse('homeView')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = "comments", on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)


#creating the model for contact
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    desc =models.TextField()
    date = models.DateTimeField()


    def __str__(self) -> str:
        return self.name