
from django.urls import path
from .views import *

urlpatterns = [
    
    path ("", machine, name="machine"),
    path("dp/", deep_learning, name="deep_learning"),
  
]
