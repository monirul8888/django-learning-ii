
from django.urls import path
from .views import *

urlpatterns = [
    
    path("", machine_learning, name="machine_learning")
  
]
