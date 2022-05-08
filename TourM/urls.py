from django.urls import path
from . import views
from .views import ad_homeView, enroll, pack_detailView, homeView, AddCommentView

urlpatterns = [
    path('ad-home/', ad_homeView.as_view(), name="ad_homeView"),
    path('package/', homeView.as_view(), name="homeView"),
    path('details/<int:pk>', pack_detailView.as_view(), name="pack_detailView"),
    path('enroll/<int:pk>', enroll.as_view(), name="enrollView"),
    path('',views.homepage, name="homepage"),
    path('contact/', views.contact, name="contact"),#sameer update.
    path('post/', views.post, name="post"), #url where the user cmt on post
    path('comment/', AddCommentView.as_view(), name="add_comment"),
    path('comment_on_post/', views.comment_on_post, name="add_comment"),
]
