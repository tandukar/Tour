from audioop import reverse
from django.db import models
from django.urls import reverse

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
    pack_img = models.ImageField(null = True, blank=True, upload_to="pacImages/")
   


    def __str__(self):
        return self.title + ' | '+ str(self.creator) 

    
    def get_absolute_url(self):
        return reverse('homeView')


   