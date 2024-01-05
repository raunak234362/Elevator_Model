# Elevator_Model API

## Overview

This project implements a simplified elevator system using Django and Django REST Framework. The elevator system can be initialized with multiple elevators and supports basic operations such as moving up and down, opening and closing doors, starting and stopping, and fetching the current status. Each elevator is associated with specific floors, and the system takes user requests into account for optimal elevator assignment.

## Features

- **Move Up and Down:** Elevators can move between floors based on user requests.
- **Open and Close Door:** Elevators can open and close doors.
- **Start and Stop Running:** Elevators can start running in a specific direction or stop.
- **Display Current Status:** Users can fetch the current status of each elevator.
- **User Requests:** Elevators handle user requests for moving up or down.
- **Elevator System Initialization:** Multiple elevators can be initialized in the system.
- **Total Floors:** The system now tracks the total number of floors in the building.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/raunakd234362/Elevator_Model
   cd Elevator_Model
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Apply migrations and run the development server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. Access the API at `http://localhost:8000/api/elevators/`.

## API Endpoints

- **GET `/api/elevators/`:** Retrieve a list of all elevators.
- **POST `/api/elevators/`:** Initialize a new elevator.
- **POST `/api/elevators/{id}/move_up/`:** Move the elevator up to a specified floor.
- **POST `/api/elevators/{id}/move_down/`:** Move the elevator down to a specified floor.
- **GET `/api/elevators/{id}/current_status/`:** Retrieve the current status of a specific elevator.


## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Open a pull request.



# Screenshot
<img width="960" alt="image" src="https://github.com/raunak234362/Elevator_Model/assets/64278503/20515b5b-e48e-42fd-9aa4-0847bf828692">
<img width="725" alt="image" src="https://github.com/raunak234362/Elevator_Model/assets/64278503/1e0cde5f-bff1-4c1b-9399-13c59bfea259">

