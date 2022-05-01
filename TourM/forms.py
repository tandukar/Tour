from dataclasses import fields
from django import forms
from .models import Post , Provinces 


# choices =Provinces.objects.all().values_list('Provinces','Provinces')

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'creator', 'body', 'days', 'price','Provinces' )

#         widgets = {
#             'Provinces': forms.Select(choices = choices, attrs={'class': 'form-control'}),

#         }

        
