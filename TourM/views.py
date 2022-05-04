
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth import get_user_model


from .models import Post


# Create your views here.

class ad_homeView(CreateView):
    model = Post
    template_name = 'ad_home.html'
    fields='__all__'


def infoView(request):
    User= get_user_model()  
    users = User.objects.all()
    users_count = User.objects.count()
    post_count = Post.objects.count()
    return render(request,'info.html',{'Users': users,'user_count':users_count,'post_count':post_count})

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
