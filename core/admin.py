from django.contrib import admin
# We import ALL models that need to be in the admin panel here
from .models import JobPost, Product, HeroImage, Branch, ContactSettings

# 1. JobPost Admin (With Search, Filter, and Details)
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'application_deadline')
    search_fields = ('title', 'description', 'location')
    list_filter = ('location', 'application_deadline', 'company_name')

# 2. Product Admin (Shows prices)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'old_price')

# 3. Hero Image Admin (Slider images)
@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'is_active')
    list_filter = ('is_active',)

# 4. Branch Admin (For the Map)
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'address')
    search_fields = ('name',)

# 5. Contact Settings Admin (One-time setup for Header/Text)
@admin.register(ContactSettings)
class ContactSettingsAdmin(admin.ModelAdmin):
    # Uses the NEW 'title' field we created
    list_display = ('title',)
    
    # This logic ensures you can only add ONE entry, not multiple
    def has_add_permission(self, request):
        return not ContactSettings.objects.exists()

# Note: I removed 'Ad' because it wasn't in your most recent working imports.
# If you need 'Ad', let me know, and we can add it back safely.