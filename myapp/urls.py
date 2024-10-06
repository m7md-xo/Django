from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('posts/', views.blog_posts, name='blog_posts'),
    path('login/', LoginView.as_view(), name= 'login')
]
