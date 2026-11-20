# Student Management API

A beginner-friendly REST API built with FastAPI. It demonstrates CRUD operations
using temporary in-memory storage.

## Features

- Create a student
- List all students
- Retrieve a student by ID
- Update a student
- Delete a student
- Pydantic request validation
- Automatic Swagger UI documentation

## Requirements

- Python 3.10+
- pip

## Setup (Windows PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the API

Run this command from the project root (the folder containing `app/`):

```powershell
uvicorn app.main:app --reload
```

Open:
- API root: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Example student JSON

```json
{
  "id": 1,
  "name": "Rahul",
  "age": 21,
  "course": "Python"
}
```

## Endpoints

| Method | URL | Purpose |
|---|---|---|
| GET | `/` | Welcome message |
| POST | `/students` | Create a student |
| GET | `/students` | List students |
| GET | `/students/{student_id}` | Get one student |
| PUT | `/students/{student_id}` | Replace a student's details |
| DELETE | `/students/{student_id}` | Delete a student |

## Important limitation

Student records are stored in a Python list in memory. They are erased when the
server process restarts. This project is for learning; connect a database before
using it for persistent or production data.
