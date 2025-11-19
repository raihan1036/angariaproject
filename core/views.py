from django.shortcuts import render, get_object_or_404
import json
from django.conf import settings
# Import ALL your models
from .models import JobPost, Product, HeroImage, Branch, ContactSettings

# --- 1. Homepage View ---
def home_view(request):
    # A. Fetch Products & Hero Images
    products = Product.objects.all()
    hero_images = HeroImage.objects.filter(is_active=True).order_by('-id')
    
    # B. Fetch Map Branches (Fixes the Map)
    db_branches = Branch.objects.all()
    branches_list = []
    for branch in db_branches:
        branches_list.append({
            "name": branch.name,
            "lat": branch.latitude,
            "lng": branch.longitude
        })
    # Convert python list to JSON string for JavaScript
    branches_json = json.dumps(branches_list)

    # C. Fetch Contact Info (Fixes the Text)
    # We get the last item you added in Admin
    contact_data = ContactSettings.objects.last()

    # D. Send everything to the HTML
    context = {
        "branches": branches_json,      # <-- This fixes the Map
        "contact_data": contact_data,   # <-- This fixes the Text
        "products": products,
        "hero_images": hero_images,
    } 
    return render(request, 'home.html', context)

# --- Other Views (Keep these as they are) ---

def services_view(request):
    return render(request, 'services.html', {})

def savings_view(request):
    return render(request, 'savings.html', {})

def job_list_view(request):
    jobs = JobPost.objects.all().order_by('-id') 
    context = {'jobs': jobs}
    return render(request, 'careers/career_list.html', context) 

def job_detail_view(request, pk):
    job = get_object_or_404(JobPost, pk=pk) 
    context = {'job': job}
    return render(request, 'careers/career_detail.html', context)