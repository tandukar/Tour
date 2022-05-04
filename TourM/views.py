from re import template
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView,CreateView

from .models import Post


# Create your views here.

class ad_homeView(CreateView):
    model = Post
    template_name = 'ad_home.html'
    


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
