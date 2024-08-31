from fastapi import APIRouter, HTTPException
from src.schemas.employee_schemas import EmployeeCreate, EmployeeUpdate
from src.services.employee_service import employee_services as e

employee_router = APIRouter()

@employee_router.get("/employee/get/all")
def fetch_all_employees():
    return e.get_all_employees()

@employee_router.get("/employee/get/by(ID)/{employee_id}")
def fetch_employee(employee_id: int):
    employee = e.get_employee_by_id(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@employee_router.post("/employee/add")
def create_employee(employee: EmployeeCreate):
    return e.add_employee(employee)

@employee_router.put("/employee/update{employee_id}")
def modify_employee(employee_id: int, employee: EmployeeUpdate):
    return e.update_employee(employee_id, employee)

@employee_router.delete("/employee/del/{employee_id}")
def remove_employee(employee_id: int):
    return e.delete_employee(employee_id)



@employee_router.get("/employee/avg/{employee_id}/avg-salary")
def fetch_avg_salary(employee_id: int):
    avg_salary = e.get_avg_salary_by_employee_id(employee_id)
    if avg_salary is None:
        raise HTTPException(status_code=404, detail="Employee not found or department has no salaries.")
    
    return {"avg_salary": f"{avg_salary:.2f} £"}

@employee_router.get("/employee/month/{employee_id}/months-of-service")
def fetch_months_of_service(employee_id: int):
    return e.get_months_of_service(employee_id)

@employee_router.get("/employee/year/{employee_id}/years-of-service")
def fetch_years_of_service(employee_id: int):
    return e.get_years_of_service(employee_id)
