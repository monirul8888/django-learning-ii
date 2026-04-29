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
    return render(request, 'ml/machineLearning.html', data)

def cnn(request):
    data = {
        'cnn_models': [
            {'name': 'CNN Basic', 'accuracy': 88},
            {'name': 'ResNet', 'accuracy': 94},
            {'name': 'MobileNet', 'accuracy': 91},
        ]
    }
    return render(request, 'ml/cnn.html', data)


def ann(request):
    data = {
        'ann_models': [
            {'name': 'Simple ANN', 'accuracy': 82},
            {'name': 'Deep ANN', 'accuracy': 90},
        ]
    }
    return render(request, 'ml/ann.html', data)