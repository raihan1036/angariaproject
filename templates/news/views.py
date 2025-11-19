# news/views.py
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def post_list_view(request):
    posts = BlogPost.objects.all() # Get all posts
    context = {
        'posts': posts
    }
    # This is the template that was causing the error
    return render(request, 'news/post_list.html', context)

def post_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'news/post_detail.html', context)