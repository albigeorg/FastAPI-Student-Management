from pydantic import BaseModel, Field


class Student(BaseModel):
    id: int = Field(gt=0, description="Student ID must be a positive integer")
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=5, le=100)
    course: str = Field(min_length=2, max_length=100)
