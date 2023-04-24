
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
        path('', views.MainPage.as_view(), name='main_page'),
        path('about/', views.AboutDetail.as_view(), name='about_detail'),
        path('contact/', views.Contact.as_view(), name='contact'),
        path('archive/', views.Archive.as_view(), name='archive'),
        path('<int:post_pk>/', views.PostDetail.as_view(), name='post_detail'),
        ]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
