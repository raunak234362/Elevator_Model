from django.urls import path, include

from rest_framework.routers import DefaultRouter

from elevator_app.views import ElevatorViewSet

router = DefaultRouter()
router.register(r'elevators', ElevatorViewSet, basename='elevators')

urlpatterns = [
    path('', include(router.urls)),
]