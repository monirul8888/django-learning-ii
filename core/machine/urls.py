
from django.urls import path
from .views import *

urlpatterns = [
    
    path("machine/", machine_learning, name="machine_learning"),
    path("cnn/", cnn, name="cnn"),
    path("ann/", ann, name="ann"),
  
]
