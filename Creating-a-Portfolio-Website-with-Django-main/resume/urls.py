from django.urls import path
from django.contrib.auth import views as auth_views



from .views import (
    home,
    about,
    projects,
    experience,
    certificate,
    contact,
    success_view,
    resume,
    
)


 # Import necessary views

from django.urls import path
from .views import home, about, projects, experience, contact, resume, success_view, certificate  # Import the certificate view

urlpatterns = [
    path('', home, name='home'),  # Home view
    path('about/', about, name='about'),  # About view
    path('projects/', projects, name='projects'),  # Projects view
    path('experience/', experience, name='experience'),  # Experience view
    path('contact/', contact, name='contact'),  # Contact view
    path('resume/', resume, name='resume'),  # Resume download view
    path('success/', success_view, name='success'),  # Success view
    path('certificate/', certificate, name='certificate'),  # Certificate view
]

