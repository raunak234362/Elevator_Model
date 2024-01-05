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