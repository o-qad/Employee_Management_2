import pandas as pd
from src.schemas.department_schemas import DepartmentCreate, DepartmentUpdate

def load_employee_data():
    da=pd.read_csv("data/employee_data.csv")
    df=pd.DataFrame(da)
    return df

def load_salary_data():
    da=pd.read_csv("data/employee_salaries.csv")
    df=pd.DataFrame(da)
    return df


class department_service():

    
  def get_all_departments():
    df = load_employee_data()  # Load your employee data
    departments = df['Department'].dropna().unique().tolist()
    return {"Departments": departments}

  def get_department_employees(department_name: str):
    df = load_employee_data()  # Load your employee data
    department_employees = df[df['Department'].str.lower() == department_name.lower()]
    
    if department_employees.empty:
        return {"message": f"No employees found in department '{department_name}'"}
    
    employees_list = department_employees[['EmployeeID', 'FirstName', 'Surname', 'Department', 'Position']].to_dict(orient='records')
    return employees_list
