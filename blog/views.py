from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # To Create New Blog Posts from the FrontEnd
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
    #success_url = reverse_lazy('home')


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):  # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
