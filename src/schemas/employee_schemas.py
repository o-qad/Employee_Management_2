from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import date

class Employee:
    def __init__(self, employee_id: int, first_name: str, surname: str, email: EmailStr, department: str, position: str, salary: float, date_of_birth: date, start_date: Optional[date] = None, end_date: Optional[date] = None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.department = department
        self.position = position
        self.salary = salary
        self.date_of_birth = date_of_birth
        self.start_date = start_date
        self.end_date = end_date

class EmployeeUpdate(BaseModel):
    FirstName: str = Field(min_length=1)
    Surname: str = Field(min_length=1)
    Email: EmailStr
    Department: str = Field(min_length=1)
    Position: str = Field(min_length=1)
    DateOfBirth: date = Field(description="Date of birth in format YYYY-MM-DD")
    Start_date: Optional[date] = Field(None, description="Start date in format YYYY-MM-DD")
    End_date: Optional[date] = Field(None, description="End date in format YYYY-MM-DD")

    class Config:
        json_schema_extra = {
            'example': {
                'FirstName': 'John',
                'Surname': 'Doe',
                'Email': 'john.doe@example.com',
                'Department': 'Sales',
                'Position': 'Manager',
                'DateOfBirth': '1985-10-21',
                'Start_date': '2010-01-01',
                'End_date': '2024-05-20'
            }
        }

class EmployeeCreate(BaseModel):
    EmployeeID: int
    FirstName: str = Field(min_length=1)
    Surname: str = Field(min_length=1)
    Email: EmailStr
    Department: str = Field(min_length=1)
    Position: str = Field(min_length=1)
    DateOfBirth: date = Field(description="Date of birth in format YYYY-MM-DD")
    Start_date: Optional[date] = Field(None, description="Start date in format YYYY-MM-DD")
    End_date: Optional[date] = Field(None, description="End date in format YYYY-MM-DD")

    class Config: 
        json_schema_extra = { 
            'example': {
                'EmployeeID': 1,
                'FirstName': 'John',
                'Surname': 'Doe',
                'Email': 'john.doe@example.com',
                'Department': 'AI',
                'Position': 'Manager',
                'DateOfBirth': '1985-10-21',
                'Start_date': '2010-01-01',
                'End_date': '2024-05-20'
            }
        }
