from rest_framework import viewsets
from rest_framework.response import Response
from elevator_app.models import Elevator, Floor
from elevator_app.serializers import ElevatorSerializer, FloorSerializer
from rest_framework.decorators import action


class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

    @action(detail=True, methods=['get'])
    def elevators_on_floor(self, request, pk=None):
        floor = self.get_object()
        elevators = floor.elevators.all()  # Assuming the related_name in Elevator model is 'elevators'
        serializer = ElevatorSerializer(elevators, many=True)
        return Response(serializer.data)

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def move_up_or_down(self, elevator, user_requests):
        current_floor = elevator.current_floor
        closest_request_above = None
        closest_request_below = None

        # Find the closest user requests above and below the current floor
        for user_req in user_requests:
            if user_req['floor'] > current_floor:
                if closest_request_above is None or user_req['floor'] < closest_request_above['floor']:
                    closest_request_above = user_req
            elif user_req['floor'] < current_floor:
                if closest_request_below is None or user_req['floor'] > closest_request_below['floor']:
                    closest_request_below = user_req

        # Decide whether to move up or down based on the closest requests
        if closest_request_above is not None:
            elevator.direction = 'up'
            elevator.current_floor = closest_request_above['floor']
        elif closest_request_below is not None:
            elevator.direction = 'down'
            elevator.current_floor = closest_request_below['floor']
        else:
            # No user requests, stay in the current direction
            pass

        elevator.save()

    def move_up(self, request, pk=None):
        elevator = self.get_object()

        user_request = request.data.get('user_requests', [])
        elevator.direction = 'up'
        current_floor = elevator.current_floor

        for user_req in user_request:
            if user_req['floor'] == current_floor:
                elevator.door_status = 'open'
            else:
                elevator.current_floor, created = Floor.objects.get_or_create(number=current_floor + 1)
                elevator.direction = 'up'
                elevator.save()

        return Response({"message": f"Elevator is moving up. Current floor: {elevator.current_floor}"})

    def move_down(self, request, pk=None):
        elevator = self.get_object()

        elevator.direction = 'down'
        if elevator.current_floor.number > 1:
            elevator.current_floor, created = Floor.objects.get_or_create(number=elevator.current_floor.number - 1)
            elevator.save()
            return Response({"message": f"Elevator is moving down to floor {elevator.current_floor}"})
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
    
    @action(detail=True, methods=['post'])
    def move_up_or_down_action(self, request, pk=None):
        elevator = self.get_object()
        user_requests = request.data.get('user_requests', [])
        self.move_up_or_down(elevator, user_requests)
        return Response({"message": "Elevator is moving based on user requests."})
