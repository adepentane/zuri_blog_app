from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView  # To Create New Blog Posts from the FrontEnd
from .models import Post


# Create your views here
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'


class BlogCreateView(CreateView):  # new
    model = Post
    template_name = 'post_new.html '
    fields = ['title ', 'author', 'body']

