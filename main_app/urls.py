from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.profiles_index, name='profiles'),
    path('profiles/create', views.ProfileCreate.as_view(), name='profiles_create'),
    path('cities/', views.cities_index, name='index'),
]