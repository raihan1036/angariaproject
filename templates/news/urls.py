# news/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # This matches /programmes/
    path('', views.post_list_view, name='post_list'), 
    
    # This matches /programmes/1/ or /programmes/2/ etc.
    # We will name it 'post_detail'
    path('<int:pk>/', views.post_detail_view, name='post_detail'), 
]