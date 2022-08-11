"urls in Your_Thoughts"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
