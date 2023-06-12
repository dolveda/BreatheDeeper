from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile, City
from .forms import LogForm

def home(request):
    return render(request, 'home.html')

def profiles_index(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/profiles.html', {'profiles': profiles})

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

def add_log(request, profile_id):
    form = LogForm(request.POST)
    if form.is_valid():
        new_log = form.save(commit=False)
        new_log.profile_id = profile_id
        new_log.save()
    return redirect('detail', profile_id=profile_id)

def cities_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})

def city_detail(request, city_id):
    city = City.objects.get(id=city_id)
    return render(request, 'cities/city_detail.html', {'city': city})

def assoc_city(requst, profile_id, city_id):
    Profile.objects.get(id=profile_id).cities.add(city_id)
    return redirect('detail', profile_id=profile_id)

class ProfileCreate(CreateView):
    model = Profile
    fields = ['name']

class ProfileUpdate(UpdateView):
    model = Profile
    fields = '__all__'

class ProfileDelete(DeleteView):
    model = Profile
    success_url = '/profiles'