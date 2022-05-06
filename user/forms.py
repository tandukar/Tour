from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm, UserCreationForm





class EditProfileForm(UserChangeForm):
     email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
     first_name=forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
     last_name=forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
     username=forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
     
    #  last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    #  is_superuser=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #  is_staff=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #  is_active=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #  data_joined=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))



     class Meta:
         model = User 
     
         fields = ('username', 'first_name', 'last_name', 'email' )
     



class PasswordChangedForm(PasswordChangeForm):
    
     old_password=forms.CharField(max_length=30 ,widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
     new_password1=forms.CharField(max_length=30 ,widget=forms.PasswordInput(attrs={'class': 'form-control' , 'type': 'password'}))
     new_password2=forms.CharField(max_length=30 ,widget=forms.PasswordInput(attrs={'class': 'form-control' , 'type': 'password'}))

     class Meta:
         model = User 
         fields = ('old_password', 'new_password1', 'new_password2' )



class registerform(UserCreationForm):
    
     username=forms.CharField(label="",max_length=30 ,widget=forms.TextInput(attrs={'class': 'form-control', 'PlaceHolder':'Username'  }))
     email=forms.EmailField(label="",widget=forms.EmailInput(attrs={'class': 'form-control', 'PlaceHolder':'Email' }))
     password1=forms.CharField(label="",max_length=30 ,widget=forms.PasswordInput(attrs={'class': 'form-control' , 'type': 'password', 'PlaceHolder':'Password' }))
     password2=forms.CharField(label="",max_length=30 ,widget=forms.PasswordInput(attrs={'class': 'form-control' , 'type': 'password', 'PlaceHolder':'Confirm password' }))
   

     class Meta:
         model = User 
         fields = ('username', 'email', 'password1','password2' )


