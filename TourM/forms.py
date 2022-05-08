from dataclasses import fields

from django import forms
from .models import Post , Provinces,Comment


# choices =Provinces.objects.all().values_list('Provinces','Provinces')

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'creator', 'body', 'days', 'price','Provinces' )

#         widgets = {
#             'Provinces': forms.Select(choices = choices, attrs={'class': 'form-control'}),

#         }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets={
            'name' :forms.TextInput(attrs={'class':'form-control'}),
            'body' :forms.TextInput(attrs={'class':'form-control'}),

        }

        
