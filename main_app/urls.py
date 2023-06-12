from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/', views.profiles_index, name='profiles'),
    path('profiles/<int:profile_id>/', views.profiles_detail, name='detail'),
    path('profiles/create', views.ProfileCreate.as_view(), name='profiles_create'),
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('profiles/<int:pk>/delete', views.ProfileDelete.as_view(), name='profiles_delete'),
    path('profiles/<int:profile_id>/add_log/', views.add_log, name='add_log'),
    path('cities/', views.cities_index, name='index'),
]