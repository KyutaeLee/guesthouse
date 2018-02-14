from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hi(request):
    return HttpResponse("Hello")

def home(request):
    return render(request, 'sitepage/home.html')

def about(request):
    return render(request, 'sitepage/about.html')
