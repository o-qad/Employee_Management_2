from fastapi import APIRouter, HTTPException
from src.schemas.department_schemas import DepartmentCreate, DepartmentUpdate
from src.services.department_service import department_service as d

department_router = APIRouter()

@department_router.get("/departments")
def fetch_all_departments():
    return d.get_all_departments()

@department_router.get("/departments/{department_name}/employees")
def fetch_department_employees(department_name: str):
    return d.get_department_employees(department_name)





