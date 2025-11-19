# news/models.py
from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="শিরোনাম")
    content = models.TextField(verbose_name="বিস্তারিত বিবরণ")
    
    # FIX: Rename this field to 'featured_image'
    featured_image = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name="ছবি")
    
    published_date = models.DateTimeField(default=timezone.now, verbose_name="প্রকাশের তারিখ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "কর্মসূচী"
        verbose_name_plural = "কর্মসূচীসমূহ"
        ordering = ['-published_date']