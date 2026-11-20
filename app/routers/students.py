from fastapi import APIRouter, HTTPException, status
from app.models import Student

router = APIRouter(prefix="/students", tags=["Students"])

# Temporary in-memory storage. Data is lost when the server restarts.
students: list[dict] = []


@router.post("", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    # First check whether the ID already exists.
    for existing_student in students:
        if existing_student["id"] == student.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Student ID already exists",
            )

    # Insert only after the duplicate check has completed.
    students.append(student.model_dump())

    return {
        "message": "Student created successfully",
        "student": student,
    }


@router.get("")
def get_students():
    return students


@router.get("/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found",
    )


@router.put("/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            if updated_student.id != student_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Student ID cannot be changed",
                )

            students[index] = updated_student.model_dump()
            return {"message": "Student updated successfully"}

    # Raise 404 only after every student has been checked.
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found",
    )


@router.delete("/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found",
    )
