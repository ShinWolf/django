from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Account signin successfully")
            return redirect('index')
        else:
            return render(request, 'signin.html', {'error': 'Invalid login credentials.'})
    else:
        return render(request, 'signin.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("signin")
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, 'register.html', user_info)
