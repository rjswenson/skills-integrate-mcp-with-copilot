# Mergington High School Activities API

A FastAPI application that allows students to view, join, and leave extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities
- Unregister from activities
- Persist activities and registrations in SQLite/SQL via SQLAlchemy

## Getting Started

1. Install dependencies:

   ```
   pip install -r ../requirements.txt
   ```

2. (Optional) Run database migrations:

   ```
   # from repository root
   alembic upgrade head
   ```

3. Run the application:

   ```
   python app.py
   ```

4. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## Configuration

- `MAIN_DB_URI` (optional): SQLAlchemy database URL.
  - Default: `sqlite:///src/activities.db`

Examples:

```
export MAIN_DB_URI="sqlite:///src/activities.db"
# or
export MAIN_DB_URI="postgresql+psycopg2://user:pass@localhost/activities"
```

## API Endpoints

| Method | Endpoint                                                              | Description                                                         |
| ------ | --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                         | Get all activities with details and participant list                |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu`    | Sign up for an activity                                             |
| DELETE | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Unregister from an activity                                         |

## Data Model

1. **Activity**
   - `name` (unique)
   - `description`
   - `schedule`
   - `max_participants`

2. **Registration**
   - `activity_id`
   - `email`
   - Unique constraint on (`activity_id`, `email`)

On first startup, the app seeds default activities if the database is empty.
