from django.shortcuts import render
from django.views.generic import ListView, DetailView
from  .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class HomePage(ListView):
    model = Post
    template_name = 'home.html'


class PostDetails(DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatePost(CreateView):
    model = Post
    template_name ='new_post.html'
    fields = ['title', 'author', 'body']

class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')