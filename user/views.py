from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


from .forms import EditProfileForm,PasswordChangedForm,registerform
from django.contrib import messages
# Create your views here.


class UserRegisterView(generic.CreateView):
    
    form_class=registerform
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class UserEditView(generic.UpdateView):
    form_class= EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('homepage')
    
    def get_object(self):
        return self.request.user
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangedForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('homepage')




