from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machine(request):
    return HttpResponse("<h1> Django Tutorial </h1>")

def deep_learning(request):
    return HttpResponse("<h1> Django Tutorial (Deep Learning) </h1>")

def about(request):
    return HttpResponse("<h1> <b> Monirul Islam </b> </h1>")