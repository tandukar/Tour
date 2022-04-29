from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class=UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class UserEditView(generic.UpdateView):
    form_class=UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('homepage')


    def get_object(self):
        return self.request.user
    