
# news/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # programmes/
    path('', views.post_list_view, name='post_list'),
    
    # programmes/5/ (উদাহরণস্বরূপ)
    path('<int:pk>/', views.post_detail_view, name='post_detail'),
]