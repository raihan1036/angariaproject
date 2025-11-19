# core/urls.py

from django.urls import path
from django.contrib import admin
from .views import (
    home_view, 
    services_view, 
    savings_view,
    job_list_view,
    job_detail_view
)

# Admin Panel Customization (Optional settings)
admin.site.site_header = "Angaria Admin Panel"
admin.site.site_title = "Angaria Admin Portal"
admin.site.index_title = "Welcome to Angaria Admin"

urlpatterns = [
    # --- Main Pages ---
    # This uses home_view (which works) instead of landing_page (which was broken)
    path('', home_view, name='home'),
    path('services/', services_view, name='services'),
    path('savings/', savings_view, name='savings'),
    
    # --- Career/Job Pages ---
    path('career/', job_list_view, name='job_list'),
    path('career/<int:pk>/', job_detail_view, name='job_detail'),
]