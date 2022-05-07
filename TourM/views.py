
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model

from .forms import  PostForm
from .models import Post


# Create your views here.

class ad_homeView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'ad_home.html'
    # fields='__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'ad_editPack.html'
    fields='__all__'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delPost.html'
    success_url = reverse_lazy('PackView')
    

def infoView(request):
    User= get_user_model()  
    users = User.objects.all()
    users_count = User.objects.count()
   
    return render(request,'info.html',{'Users': users,'user_count':users_count})

def PackView(request):
    model = Post
    post = model.objects.all()
   
    post_count = Post.objects.count()
    return render(request,'ad_pack.html',{'Packages': post,'post_count':post_count})

class homeView(ListView):
    model = Post
    template_name = 'home.html'
   

class pack_detailView(DetailView):
    model = Post
    template_name = 'pack_details.html'
   


class enroll(DetailView):
    model = Post
    template_name = 'enroll.html'


def homepage(request):
    return render(request, 'index.html')
