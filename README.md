# Django Elevator System

## Thought Process

### Problem Statement

The goal is to implement a simplified elevator system using Django and Django REST Framework. Key features include elevator movement, door control, system initialization, and handling user requests for optimal elevator assignment.

### Design Decisions

1. **Architecture:**
   - Django was chosen for its robustness in web development and the Django REST Framework for building APIs.
   - Model-View-Controller (MVC) architectural pattern: Django's structure naturally aligns with MVC, providing clear separation of concerns.

2. **Repository File Structure:**
   - `elevator_system/`: Django project folder.
   - `elevator/`: Django app for elevator-related models and views.
   - `requirements.txt`: Lists project dependencies.

3. **Database Modeling:**
   - `Elevator` model includes `current_floor`, `direction`, `operational`, and `total_floors`.
   - `Floor` model represents floors in the building.

4. **Libraries and Plugins:**
   - Django REST Framework: For building APIs efficiently.
   - SQLite (default Django database): Simple and lightweight, suitable for development.

## API Contracts

### Elevator Endpoints

- **GET `/api/elevators/`:**
  - Retrieves a list of all elevators.

- **POST `/api/elevators/`:**
  - Initializes a new elevator.
  - Payload: None.

- **POST `/api/elevators/{id}/move_up/`:**
  - Moves the elevator up to a specified floor.
  - Payload: `{ "target_floor": 3 }`

- **POST `/api/elevators/{id}/move_down/`:**
  - Moves the elevator down to a specified floor.
  - Payload: `{ "target_floor": 1 }`

- **GET `/api/elevators/{id}/current_status/`:**
  - Retrieves the current status of a specific elevator.

### Setup, Deploy, and Test

#### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/django-elevator-system.git
   cd django-elevator-system
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

#### Deploy

1. Choose a production-ready database (e.g., PostgreSQL).
2. Set environment variables for production settings (e.g., `DJANGO_SETTINGS_MODULE`).
3. Configure a web server (e.g., Gunicorn) and a reverse proxy (e.g., Nginx).

#### Testing

1. Run tests using Django's test runner:

   ```bash
   python manage.py test
   ```

2. Write additional tests for new features.

## Conclusion

The Django Elevator System project employs a straightforward design, utilizing Django and Django REST Framework for efficiency and maintainability. The project structure, database modeling, and API contracts are designed to be clear and scalable. Future improvements may include adding authentication, improving elevator movement logic, and enhancing error handling.


# Screenshot
![image](https://github.com/raunak234362/Elevator_Model/assets/64278503/544e3b7f-8501-49c6-9005-61201ac2f57f)
![image](https://github.com/raunak234362/Elevator_Model/assets/64278503/ea8d6b68-2ac0-461d-a9cb-5b848a3cd61a)
