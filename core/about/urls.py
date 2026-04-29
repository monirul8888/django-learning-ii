
from django.urls import path
from .views import *

urlpatterns = [
    
    path ("about/", about, name="about"),
    path("about1/", about1, name="about1"),
  
]
