from django.shortcuts import render
from rest_framework import viewsets
from .models import Bird, Location, Sighting
from .serializers import BirdSerializer, LocationSerializer, SightingSerializer

class BirdViewSet(viewsets.ModelViewSet):
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class SightingViewSet(viewsets.ModelViewSet):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer
