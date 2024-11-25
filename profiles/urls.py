from django.urls import path
from .views import profile_view

urlpatterns = [
    path('profiles/', profile_view, name='profiles'),
    
]