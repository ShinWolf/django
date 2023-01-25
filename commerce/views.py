from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def services(request):
    return render(request, 'services.html')

def signin(request):
    return render(request, 'signin.html')

def register(request):
    return render(request, 'register.html')
