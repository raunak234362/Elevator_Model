from django.db import models

class Elevator(models.Model):
    #This model represents an elevator in the building.
    id=models.AutoField(primary_key=True)
    current_floor=models.IntegerField(default=0)
    direction=models.CharField(max_length=10,choices=[
        ('up','Up'),
        ('down','Down'),
        ('stop','Stop')
        ],default='stop')
    operational=models.BooleanField(default=True)
    available=models.BooleanField(default=True)

class FloorRequest(models.Model):
    #This model represents a floor request to go to a specific floor.
    id=models.AutoField(primary_key=True)
    elevator=models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor_req=models.IntegerField()
    status=models.CharField(max_length=10,choices=[
        ("Waiting","Waiting"),
        ("Completed","Completed")
    ],default="Waiting")