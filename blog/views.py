from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # naming convention : <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):

    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
