# angariaproject/urls.py

from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- ADD THIS LINE ---
    # This adds all of Django's built-in auth URLs
    # (like /accounts/login/, /accounts/logout/, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Your app URLs
    path('programmes/', include('news.urls')), 
    path('', include('core.urls')),  
]

# This part for media files is correct
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)