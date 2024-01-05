from django.urls import path, include

from rest_framework.routers import DefaultRouter

from elevator_app.views import ElevatorViewSet, FloorViewSet

router = DefaultRouter()
router.register(r'elevators', ElevatorViewSet, basename='elevators')
router.register(r'floors', FloorViewSet, basename='floors')

urlpatterns = [
    path('', include(router.urls)),
]