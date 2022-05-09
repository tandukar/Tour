from django.urls import path
from . import views
from .  views import ad_homeView, enrollView, pack_detailView, homeView,UpdatePostView, DeletePostView,paymentView

urlpatterns = [
    path('ad-home/', ad_homeView.as_view(), name="ad_homeView"),
    path('details/edit/<int:pk>/', UpdatePostView.as_view(), name="UpdatePost"),
    path('details/<int:pk>/delete', DeletePostView.as_view(), name="DeletePost"),
   
    path('info/', views.infoView, name="infoView"),
    path('packView/', views.PackView, name="PackView"),
    path('package/', homeView.as_view(), name="homeView"),
    path('details/<int:pk>', pack_detailView.as_view(), name="pack_detailView"),

    path('enroll/', enrollView.as_view(), name="enrollView"),

    path('details/<int:pk>/checkout', paymentView.as_view(), name="checkout"),

    path('user_csv', views.user_csv, name="user_csv"),
    path('user_pdf', views.user_pdf, name="user_pdf"),

    path('enrolled/', views.En_usersView, name="enrolled"),


    path('aboutus/', views.aboutus, name="aboutus"),
    path('seasons/', views.seasons, name="seasons"),
    
    path('',views.homepage, name="homepage"),
    
   
  
]
