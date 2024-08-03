from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Backyard Birds API")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sightings.urls')),
    path('', home),  # Add this line to handle the root URL
]
