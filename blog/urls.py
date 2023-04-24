
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
        path('', views.MainPage.as_view(), name='main_page'),
        path('about/', views.AboutDetail.as_view(), name='about_detail'),
        path('contact/', views.Contact.as_view(), name='contact'),
        path('archive/', views.Archive.as_view(), name='archive'),
        path('<int:post_pk>/', views.PostDetail.as_view(), name='post_detail'),
        ]
