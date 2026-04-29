from django.shortcuts import render
from django.http import HttpResponse

def machine_learning(request):
    data = {
        'models': [
            {'name': 'Linear Regression', 'accuracy': 85},
            {'name': 'Decision Tree', 'accuracy': 90},
            {'name': 'Neural Network', 'accuracy': 95},
        ]
    }
    return render(request, 'machineLearning.html', data)