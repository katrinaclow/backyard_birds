from django.db import models
from django.contrib.auth.models import User

class Bird(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    range_map_url = models.URLField()

class Location(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Sighting(models.Model):
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sighted_at = models.DateTimeField()
    number_observed = models.IntegerField()
    behavior = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    photo_url = models.URLField(blank=True, null=True)
