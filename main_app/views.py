from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def cities_index(request):
    return render(request, 'cities/index.html')