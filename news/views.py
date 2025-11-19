from django.shortcuts import render
from .models import BlogPost

def post_list_view(request):
    # সব পাবলিশড পোস্টগুলোকে নতুন-থেকে-পুরাতন ক্রমে সাজানো হলো
    posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    
    context = {
        'posts': posts
    }
    return render(request, 'news/post_list.html', context)

def post_detail_view(request, post_id):
    # নির্দিষ্ট একটি পোস্ট দেখানোর জন্য
    post = BlogPost.objects.get(id=post_id, is_published=True)
    context = {
        'post': post
    }
    return render(request, 'news/post_detail.html', context)








# news/views.py
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# ভিউ ১: সব পোস্টের তালিকা (List View)
def post_list_view(request):
    posts = BlogPost.objects.all() # ডেটাবেস থেকে সব পোস্ট আনা হলো
    context = {
        'posts': posts
    }
    return render(request, 'news/post_list.html', context)

# ভিউ ২: একটি নির্দিষ্ট পোস্ট (Detail View)
def post_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk) # নির্দিষ্ট pk (id) দিয়ে একটি পোস্ট খোঁজা
    context = {
        'post': post
    }
    return render(request, 'news/post_detail.html', context)