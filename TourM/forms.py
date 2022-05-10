
from django import forms
from .models import Post , enroll
from django.contrib.auth.forms import UserCreationForm


# choices =Provinces.objects.all().values_list('Provinces','Provinces')
choices = [('in Desc','in Desc'),('province 1','province 1'),('province 2','Madhesh Province'),('province 3','Bagmati Province'),('province 4','Gandaki Province'),('province 5','Lumbini Province'),('province 6','Karnali Province'),('province 7','Sudurpashchim Province')]
choices1 = [('in Desc','in Desc'),('Hotel','Hotel'),('Hostel','Hostel'),('Resort','Resort')]
choices2 = [('in Desc','in Desc'),('Bus','Bus'),('Flight','Flight'),('Hiace','Hiace')]
choices3 = [('----','---'),('Host  Pvt.Ltd','Host  Pvt.Ltd'),('One Life Adventures','One Life Adventures'),('Herald Travels','Herald Travels')]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'Hoster', 'body', 'days', 'price','Provinces','Size','Transportation' ,'Accomodation','pack_img','pack_img1','pack_img2','pack_img3','pack_img4')

        widgets = {
            'title': forms.TextInput( attrs={'class': 'form-control'}),
            'Hoster': forms.Select(choices = choices3,attrs={'class': 'form-control'}),
            'days': forms.NumberInput( attrs={'class': 'form-control'}),
            'Provinces': forms.Select(choices = choices,attrs={'class': 'form-control'}),
            'price': forms.TextInput( attrs={'class': 'form-control'}),
            'body': forms.Textarea( attrs={'class': 'form-control'}),
            'Size': forms.NumberInput ( attrs={'class': 'form-control'}),
            'Transportation': forms.Select(choices = choices2,attrs={'class': 'form-control'}),
            'Accomodation': forms.Select(choices = choices1,attrs={'class': 'form-control'}),
            

        }




class enrollForm(forms.ModelForm):

     
    #  Post=forms.CharField(max_length=30 ,widget=forms.Select(choices=enroll_choices,attrs={'class': 'form-control'}))
     username=forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
     firstname=forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
     lastname=forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
     email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
     Size=forms.NumberInput ( attrs={'class': 'form-control'}),
     



     class Meta:
         model = enroll 
     
         fields = ('username', 'firstname', 'lastname', 'email','Size' )
        
