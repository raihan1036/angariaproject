# core/models.py
from django.db import models
from django.utils import timezone

class JobPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="পদের নাম")
    company_name = models.CharField(max_length=200, default="আঙ্গারিয়া ক্ষুদ্র ব্যবসায়ী ও সমবায় সমিতি লিঃ", verbose_name="প্রতিষ্ঠানের নাম")
    
    # নতুন ফিল্ড: কোম্পানির লোগো (ঐচ্ছিক)
    company_logo = models.ImageField(upload_to='job_logos/', blank=True, null=True, verbose_name="প্রতিষ্ঠানের লোগো")
    
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="কাজের স্থান")
    
    # নতুন ফিল্ড: অভিজ্ঞতা (ঐচ্ছিক)
    experience = models.CharField(max_length=100, blank=True, null=True, verbose_name="অভিজ্ঞতা (যেমন: ৪ থেকে ৫ বছর)")
    
    # নতুন ফিল্ড: সংক্ষিপ্ত বিবরণ (ঐচ্ছিক)
    short_description = models.TextField(blank=True, null=True, verbose_name="সংক্ষিপ্ত বিবরণ (তালিকা পেজের জন্য)")
    
    description = models.TextField(verbose_name="চাকরির বিস্তারিত বিবরণ")
    application_deadline = models.DateField(blank=True, null=True, verbose_name="আবেদনের শেষ তারিখ")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="প্রকাশের তারিখ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "চাকরির পোস্ট"
        verbose_name_plural = "চাকরির পোস্টসমূহ"
        # আবেদনের শেষ তারিখ অনুযায়ী সাজানো থাকবে
        ordering = ['application_deadline']



        # core/models.py

# ... your other models like JobPost might be here ...

class Ad(models.Model):
    title = models.CharField(max_length=100, help_text="For internal reference (e.g., 'Spring Sale Ad')")
    image = models.ImageField(upload_to='ads/', verbose_name="Ad Image")
    link = models.URLField(max_length=255, blank=True, null=True, help_text="Optional: URL the ad clicks to")
    
    start_date = models.DateTimeField(default=timezone.now, verbose_name="Ad Start Date")
    end_date = models.DateTimeField(verbose_name="Ad End Date")
    is_active = models.BooleanField(default=True, help_text="Manually turn this ad on or off")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"
        ordering = ['start_date']



# core/models.py

# ... (Keep your JobPost or other models here) ...

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="পণ্য নাম")
    image = models.ImageField(upload_to='products/', verbose_name="ছবি")
    
    # --- CHANGED LINE ---
    price = models.IntegerField(null=True, blank=True, verbose_name="কিস্তির সময় কাল")
    # --------------------
    
    old_price = models.IntegerField(null=True, blank=True, verbose_name="পূর্বের মূল্য (অপশনাল)")
    description = models.TextField(verbose_name="বিবরণ")
    
    def __str__(self):
        return self.name
    

    # core/models.py

# ... (Keep your existing JobPost and Product models) ...

class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero_images/', verbose_name="হিরো ছবি")
    caption = models.CharField(max_length=255, blank=True, verbose_name="ক্যাপশন (অপশনাল)")
    is_active = models.BooleanField(default=True, verbose_name="সক্রিয়?")

    class Meta:
        verbose_name = "হিরো ছবি"
        verbose_name_plural = "হিরো ছবিসমূহ"

    def __str__(self):
        return f"Hero Image {self.id} ({'Active' if self.is_active else 'Inactive'})"
    


    # core/models.py

class Branch(models.Model):
    name = models.CharField(max_length=200, verbose_name="ব্রাঞ্চের নাম")
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name="ঠিকানা (অপশনাল)")
    
    # We use FloatField for coordinates
    latitude = models.FloatField(verbose_name="Latitude (অক্ষাংশ)")
    longitude = models.FloatField(verbose_name="Longitude (দ্রাঘিমাংশ)")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Branch Location"
        verbose_name_plural = "Branch Locations"





        # core/models.py

# core/models.py

# ... (Your other models like Branch, Product etc. are above here) ...

class ContactSettings(models.Model):
    title = models.CharField(max_length=200, default="আমাদের শাখার অবস্থান", verbose_name="হেডার / শিরোনাম")
    content = models.TextField(verbose_name="বিস্তারিত তথ্য (ঠিকানা, ফোন, ইত্যাদি)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact Info (Simple)"
        verbose_name_plural = "Contact Info (Simple)"

# --- STOP HERE. Make sure there is NO code below this line ---