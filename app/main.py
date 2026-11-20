from fastapi import FastAPI
from app.routers import students

app = FastAPI(
    title="Student Management API",
    description="A beginner-friendly API for managing student records.",
    version="1.0.0",
)

app.include_router(students.router)


@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}
