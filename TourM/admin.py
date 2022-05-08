from django.contrib import admin
from .models import Post, Provinces, Comment
from TourM.models import Contact
# Register your models here.

admin.site.register(Post) 
admin.site.register(Provinces) 
admin.site.register(Comment) 

#registering the model in admin.
admin.site.register(Contact)