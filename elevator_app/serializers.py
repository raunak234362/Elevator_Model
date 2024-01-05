from rest_framework import serializers
from elevator_app.models import Elevator, Floor

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ('__all__')


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model: Floor
        fields = ('__all__')