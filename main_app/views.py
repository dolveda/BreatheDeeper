from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Profile, City

def home(request):
    return render(request, 'home.html')

def profiles_index(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profiles.html', {'profiles': profiles})

def cities_index(request):
    return render(request, 'cities/index.html')

class ProfileCreate(CreateView):
    model = Profile
    fields = '__all__'