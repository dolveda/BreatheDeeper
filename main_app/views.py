from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, City
from .forms import LogForm
import requests

def home(request):
    return render(request, 'home.html')

@login_required
def profiles_index(request):
    profiles = Profile.objects.filter(user=request.user)
    return render(request, 'profiles/profiles.html', {'profiles': profiles})

@login_required
def profiles_detail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    id_list = profile.cities.all().values_list('id')
    unassociated_cities = City.objects.exclude(id__in=id_list)
    log_form = LogForm()
    return render(request, 'profiles/detail.html', { 
        'profile': profile, 
        'log_form': log_form , 
        'cities': unassociated_cities}
        )

@login_required
def add_log(request, profile_id):
    form = LogForm(request.POST)
    if form.is_valid():
        new_log = form.save(commit=False)
        new_log.profile_id = profile_id
        new_log.save()
    return redirect('detail', profile_id=profile_id)

@login_required
def cities_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})

@login_required
def city_detail(request, city_id):
    city = City.objects.get(id=city_id)
    coordinates = City.objects.get(id=city_id).coordinates
    url = f"https://air-quality-api.open-meteo.com/v1/air-quality?{coordinates}&hourly=us_aqi&timezone=America%2FLos_Angeles"
    response = requests.get(url).json()
    return render(request, 'cities/city_detail.html', {
        'city': city,
        'response': response
        })

@login_required
def assoc_city(request, profile_id, city_id):
    Profile.objects.get(id=profile_id).cities.add(city_id)
    return redirect('detail', profile_id=profile_id)

@login_required
def unassoc_city(request, profile_id, city_id):
    Profile.objects.get(id=profile_id).cities.remove(city_id)
    return redirect('detail', profile_id=profile_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = '__all__'

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    success_url = '/profiles'