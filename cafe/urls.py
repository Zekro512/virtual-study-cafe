from django.urls import path
from .views import home, about, study_rooms, resources, contact

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('study_rooms/', study_rooms, name='study_rooms'),
    path('resources/', resources, name='resources'),
    path('contact/', contact, name='contact'),
]
