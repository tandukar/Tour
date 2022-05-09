from audioop import reverse
from xmlrpc.client import Transport
from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Provinces(models.Model):
    Provinces = models.CharField(default='in desc',max_length=255)

    def __str__(self):
        return self.Provinces     
    def get_absolute_url(self):
        return reverse('homeView')


class Post(models.Model):
    title = models.CharField(max_length=255) 
    body = RichTextField()
    days = models.PositiveIntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    price = models.IntegerField(default='',null=False)
    Provinces = models.CharField(default='in_desc', max_length=255, null=False)
    Size = models.PositiveIntegerField(default='1', validators=[MaxValueValidator(100),MinValueValidator(1)])      #group size {if paxi availability add garne bhe useful}
    Hoster=models.CharField(max_length=255, null=False)
    Accomodation= models.CharField(default='', max_length=255, null=False)
    Transportation= models.CharField(default='', max_length=255, null=False)
    pack_img = models.ImageField(null = True, blank=True, upload_to="pacImages/")
    pack_img1 = models.ImageField(null = True, blank=True, upload_to="pacImages/")
    pack_img2 = models.ImageField(null = True, blank=True, upload_to="pacImages/")
    pack_img3 = models.ImageField(null = True, blank=True, upload_to="pacImages/")
    pack_img4 = models.ImageField(null = True, blank=True, upload_to="pacImages/")
    
    def __str__(self):
        return self.title 

    
    def get_absolute_url(self):
        return reverse('homeView')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = "comments", on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)




class   enroll(models.Model):
    post = models.ForeignKey(Post, related_name = "enrolls", on_delete = models.CASCADE, default='')
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    
    date_added = models.DateTimeField(auto_now_add=True)

    # USERNAME_FIELD = 'username'

    def __str__(self):
         return '%s - %s' %(self.post.title, self.username)
    


   