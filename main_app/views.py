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
    log_form = LogForm()
    return render(request, 'profiles/detail.html', { 'profile': profile, 'log_form': log_form })

def add_log(request, profile_id):
    form = LogForm(request.POST)
    if form.is_valid():
        new_log = form.save(commit=False)
        new_log.profile_id = profile_id
        new_log.save()
    return redirect('detail', profile_id=profile_id)

def cities_index(request):
    return render(request, 'cities/index.html')

class ProfileCreate(CreateView):
    model = Profile
    fields = '__all__'

class ProfileUpdate(UpdateView):
    model = Profile
    fields = '__all__'

class ProfileDelete(DeleteView):
    model = Profile
    success_url = '/profiles'