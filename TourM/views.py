from re import template
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView,CreateView
from requests import request
from datetime import datetime #for date,sameer
from TourM.models import Contact #importing the contact 

from .models import Post,Comment


# Create your views here.

class ad_homeView(CreateView):
    model = Post
    template_name = 'ad_home.html'
    fields='__all__'


class homeView(ListView):
    model = Post
    template_name = 'home.html'
   

class pack_detailView(DetailView):
    model = Post
    template_name = 'pack_details.html'
   


class enroll(DetailView):
    model = Post
    template_name = 'enroll.html'


def contact(request): #SAmeer DON le gareko
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()       
    return render(request,'contact.html')

class AddCommentView(CreateView):
     model = Comment
     template_name= 'add_comment.html'
     fileds ='__all__'
    

def cmt(request):
    return render(request,'cmt.html')

def homepage(request):
    return render(request, 'index.html')
