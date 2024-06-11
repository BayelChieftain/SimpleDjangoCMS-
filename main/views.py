from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(req):
    data = {
        'title': 'Main page.',
        'values': ['Some', 'Most', 'Less', 'love']
    }
    return render(req, 'main/index.html', data)


def about(req):
    return render(req, 'main/about.html')
