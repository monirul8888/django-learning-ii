from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about (request):
    return HttpResponse("This is About APP About Page")

def about1 (request):
    return HttpResponse("This is About APP About Page 1")
