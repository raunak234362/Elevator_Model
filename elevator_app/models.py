from django.db import models


class Floor(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f"Floor {self.number}"

class Elevator(models.Model):
    #This model represents an elevator in the building.
    id=models.AutoField(primary_key=True)
    current_floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='current')
    user_requests = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='request')
    operational=models.BooleanField(default=True)

    direction=models.CharField(max_length=10,choices=[
        ('up','Up'),
        ('down','Down'),
        ('stop','Stop')
        ],default='stop')

    door_status = models.CharField(max_length=10, choices=[
        ('open', 'Open'),
        ('closed', 'Closed')
    ], default='closed')

    def __str__(self):
        return f"Elevator {self.id} - {self.direction} at {self.current_floor}"

class FloorRequest(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='floor_requests')
    elevators_count = models.IntegerField(default=1)  # Specify the number of elevators on this floor
    user_requests = models.JSONField(default=list)

    def __str__(self):
        return f"Floor {self.floor.number} - Elevators Count: {self.elevators_count}"
    

