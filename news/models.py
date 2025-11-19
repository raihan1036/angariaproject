from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    # এই নতুন লাইনটি যোগ করুন
    # 'post_images/' ফোল্ডারে ছবিগুলো সেভ হবে
    featured_image = models.ImageField(upload_to='post_images/', blank=True, null=True) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False) # পোস্ট ড্রাফট করার জন্য

    def __str__(self):
        return self.title