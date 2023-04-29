from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

# Create your views here.

class MainPage(ListView):
    model = Post
    template_name = 'mainpage.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class Archive(ListView):
    model = Post
    template_name = 'mainpage.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post_pk = self.kwargs['post_pk']
        return self.model.objects.get(post_pk=post_pk)

class AboutDetail(TemplateView):
    template_name = 'about.html'

class Contact(TemplateView):
    template_name = 'contact.html'
