from django.urls import path
from . import views
from .  views import ad_homeView, enroll, pack_detailView, homeView,UpdatePostView, DeletePostView

urlpatterns = [
    path('ad-home/', ad_homeView.as_view(), name="ad_homeView"),
    path('details/edit/<int:pk>/', UpdatePostView.as_view(), name="UpdatePost"),
    path('details/<int:pk>/delete', DeletePostView.as_view(), name="DeletePost"),
    path('info/', views.infoView, name="infoView"),
    path('packView/', views.PackView, name="PackView"),
    path('package/', homeView.as_view(), name="homeView"),
    path('details/<int:pk>', pack_detailView.as_view(), name="pack_detailView"),
    path('enroll/<int:pk>', enroll.as_view(), name="enrollView"),
    path('user_csv', views.user_csv, name="user_csv"),
    path('user_pdf', views.user_pdf, name="user_pdf"),
    path('',views.homepage, name="homepage"),
    
   
  
]
