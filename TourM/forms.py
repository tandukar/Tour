
from django import forms
from .models import Post , Provinces 


# choices =Provinces.objects.all().values_list('Provinces','Provinces')
choices = [('province 1','province 1'),('province 2','province 2'),('province 3','province 3')]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'Hoster', 'body', 'days', 'price','Provinces','Size','Accomodation' ,'pack_img')

        widgets = {
            'title': forms.TextInput( attrs={'class': 'form-control'}),
            'Hoster': forms.TextInput( attrs={'class': 'form-control'}),
            'days': forms.NumberInput( attrs={'class': 'form-control'}),
            'Provinces': forms.Select(choices = choices,attrs={'class': 'form-control'}),
            'price': forms.TextInput( attrs={'class': 'form-control'}),
            'body': forms.Textarea( attrs={'class': 'form-control'}),
            'Size': forms.NumberInput ( attrs={'class': 'form-control'}),
            'Accomodation': forms.TextInput( attrs={'class': 'form-control'}),

        }

        
