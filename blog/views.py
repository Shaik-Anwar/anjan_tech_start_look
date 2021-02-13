from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



#def all_blogs(request):
#    return render(request, 'blog/index.html')

class HomeView(ListView):
    model= Post
    template_name = 'blog/index.html'

class PostView(DetailView):
    model= Post
    template_name = 'blog/blog-post.html'
