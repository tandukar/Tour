

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model

from .forms import  PostForm,enrollForm
from .models import Post,enroll


from django.contrib import messages


#for generating csv
import csv
# for generating pdf
from django.http import FileResponse, HttpResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



# Create your views here.

class ad_homeView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'ad_home.html'
    # fields='__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'ad_editPack.html'
    form_class = PostForm

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
   


class enrollView(ListView):
    model = Post
    template_name = 'enroll.html'



def  En_usersView(request):
    
    model= enroll 
    enrolled_count = model.objects.count()
    enrolled = model.objects.all()
    return render(request,'ad_enrolled.html',{'enrolled_count':enrolled_count,'enrolled':enrolled})




#adding info for enrolli
class paymentView(CreateView):
    model = enroll  
    form_class=enrollForm
    template_name = 'checkout.html'

    def form_valid(self, form):
         form.instance.post_id = self.kwargs['pk']

         return super().form_valid(form)
    success_url = reverse_lazy('enrollView')

  

def seasons(request):
    return render(request, 'seasons.html')

def aboutus(request):
    return render(request, 'aboutus.html')



def homepage(request):
    return render(request, 'index.html')


#Generate csv files.

def user_csv(request):
   response = HttpResponse(content_type = 'text/csv')
   response['Content-Disposition'] = 'attactment; filename: users.csv'
 

   #create a csv writer
   writer = csv.writer(response)


 # configure model
   User= get_user_model()  
   users = User.objects.all()

   writer.writerow(['User Name','First Name', 'Last Name', 'Email'])


   for user in users:
       writer.writerow([user.username, user.first_name, user.last_name, user.email])

   return response


#generate enrolled users csv

def enroll_csv(request):
   response = HttpResponse(content_type = 'text/csv')
   response['Content-Disposition'] = 'attactment; filename: enrolled.csv'
 

   #create a csv writer
   writer = csv.writer(response)


 # configure model
    
   users = enroll.objects.all()

   writer.writerow(['User Name','First Name', 'Last Name', 'Email', 'post', 'size', 'purchased date'])


   for user in users:
       writer.writerow([user.username, user.firstname, user.lastname, user.email, user.post, user.Size, user.date_added])

   return response
      

      


#Generate pdf files.

def user_pdf(request):
    #Create Bytestream buffer
    buf = io.BytesIO()
    #Create a canvas
    c = canvas.Canvas(buf, pagesize= letter, bottomup=0)
    documentTitle = "Registerd Uers"
    title ="Registerd Uers"
    c.setTitle(documentTitle)
    c.drawString(270,50,title )
    
   
    #create a text object
    text_object = c.beginText()
    text_object.setTextOrigin(inch, inch)
    text_object.setFont('Helvetica' , 14)


    User= get_user_model()  
    users = User.objects.all()

    lists = []
    
    for user in users:
        lists.append("")
        lists.append(user.username)
        lists.append(user.first_name)
        lists.append(user.last_name)
        lists.append(user.email)
        lists.append("--------------------------")

        for list in lists:
            text_object.textLine(list)
         

    c.drawText(text_object)
    c.showPage()
    c.save()
    buf.seek(0)


    return FileResponse(buf, as_attachment=True, filename = 'users.pdf')
