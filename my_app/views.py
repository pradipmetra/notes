from django.http import HttpResponse
from django.shortcuts import render,redirect

def members(request):
    return HttpResponse("hello world")

def my_view(request):
    
    return render(request, 'index.html')

def register(request):
    return render(request, 'registration.html')

