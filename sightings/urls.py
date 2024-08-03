from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BirdViewSet, LocationViewSet, SightingViewSet

router = DefaultRouter()
router.register(r'birds', BirdViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'sightings', SightingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
