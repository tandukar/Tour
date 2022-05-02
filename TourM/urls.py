from django.urls import path
from . import views
from .  views import ad_homeView, enroll, pack_detailView, homeView, infoView

urlpatterns = [
    path('ad-home/', ad_homeView.as_view(), name="ad_homeView"),
    path('info/', infoView.as_view(), name="infoView"),
    path('package/', homeView.as_view(), name="homeView"),
    path('details/<int:pk>', pack_detailView.as_view(), name="pack_detailView"),
    path('enroll/<int:pk>', enroll.as_view(), name="enrollView"),
    path('',views.homepage, name="homepage"),
  
]
