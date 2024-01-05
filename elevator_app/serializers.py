from rest_framework import serializers
from .models import Elevator,FloorRequest

class ElevatorSerializer(serializers.ModeSerializer):
    class Meta:
        model = Elevator
        fields = ('__all__')

class FloorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorRequest
        fields = '__all__'