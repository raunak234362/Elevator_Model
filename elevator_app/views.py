from rest_framework import viewsets
from rest_framework.response import Response
from elevator_app.models import Elevator
from elevator_app.serializers import ElevatorSerializer
from rest_framework.decorators import action

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def move_up(self, request, pk=None):
        elevator = self.get_object()

        user_request = request.data.get('user_requests', [])
        elevator.direction = 'up'
        current_floor = elevator.current_floor
        for user_req in user_request:
            if user_req['floor'] == current_floor:
                elevator.door_status = 'open'
            else:
                elevator.current_floor += 1

        elevator.save()

        return Response({"message": "Elevator is moving up."})

    def move_down(self, request, pk=None):
        elevator = self.get_object()

        elevator.direction = 'down'
        if elevator.current_floor > 1:
            elevator.current_floor -= 1
            elevator.save()
            return Response({"message": "Elevator is moving down to floor {}".format(elevator.current_floor)})
        else:
            return Response({"message": "Elevator is already at the lowest floor."})

    def open_door(self, request, pk=None):
        elevator = self.get_object()
        if elevator.door_status != 'open':
            elevator.door_status = 'open'
            elevator.save()
            return Response({"message": "Elevator door is open."})
        else:
            return Response({"message": "Elevator door is already open."})

    def close_door(self, request, pk=None):
        elevator = self.get_object()
        if elevator.door_status != 'closed':
            elevator.door_status = 'closed'
            elevator.save()
            return Response({"message": "Elevator door is closed."})
        else:
            return Response({"message": "Elevator door is already closed."})

    def start_running(self, request, pk=None):
        elevator = self.get_object()
        if elevator.direction is None or elevator.direction == '':
            elevator.direction = 'up' 
            elevator.save()
            return Response({"message": "Elevator is now running."})
        else:
            return Response({"message": "Elevator is already running."})

    def stop_running(self, request, pk=None):
        elevator = self.get_object()
        if elevator.direction != 'stop':
            elevator.direction = 'stop'
            elevator.save()
            return Response({"message": "Elevator is stopped."})
        else:
            return Response({"message": "Elevator is already stopped."})

    def current_status(self, request, pk=None):
        elevator = self.get_object()
        current_floor = elevator.current_floor
        direction = elevator.direction
        door_status = elevator.door_status

        return Response({
            "current_floor": current_floor,
            "direction": direction,
            "door_status": door_status,
        })
