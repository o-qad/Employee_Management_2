from fastapi import HTTPException
import pandas as pd
from src.schemas.employee_schemas import EmployeeCreate, EmployeeUpdate,Employee

EMPLOYEE_DATA_PATH = "data/employee_data.csv"
EMPLOYEE_SALARY_PATH = "data/employee_salaries.csv"

def update_null_values(dff: pd.DataFrame, columns: list):
    for column in columns:
        dff[column] = dff[column].fillna('null')
    return dff

def load_employee_data():
    da=pd.read_csv("data/employee_data.csv")
    df=pd.DataFrame(da)
    return df

def load_salary_data():
    da=pd.read_csv("data/employee_salaries.csv")
    df=pd.DataFrame(da)
    return df

class employee_services():
  
  def get_all_employees():
    df = pd.read_csv("data/employee_data.csv")
    selected_columns = df[["EmployeeID", "FirstName", "Surname", "Department", "Position"]]
    return selected_columns.to_dict(orient="records")

  def get_employee_by_id(employee_id: int):
    df = load_employee_data()
    employee = df[df["EmployeeID"] == employee_id]
    if employee.empty:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee.iloc[0].to_dict()

  def add_employee(employee: EmployeeCreate):
    df = load_employee_data()  # Make sure this returns a DataFrame
    
    new_employee = pd.DataFrame([employee.dict(by_alias=True)])
    
    for column in new_employee.columns:
        if column not in df.columns:
            df[column] = None  # Ensure new columns are added if necessary

    new_employee = new_employee[df.columns]  # Align new employee with existing DataFrame
    df = pd.concat([df, new_employee], ignore_index=True)
    df.to_csv(EMPLOYEE_DATA_PATH, index=False)
    
    columns_to_update = ['Start_date','End_date']
    dff = update_null_values(df, columns_to_update)  # Ensure this function is defined
    dff.to_csv(EMPLOYEE_DATA_PATH, index=False)

    return {"message": "Employee added successfully", "id": df.index[-1]}

  def update_employee(employee_id: int, employee: EmployeeUpdate):
    df = load_employee_data()
    if employee_id not in df["EmployeeID"].values:
        return {"error": "Employee not found"}
    df.update(df[df["EmployeeID"] == employee_id].assign(**employee.dict()))
    df.to_csv(EMPLOYEE_DATA_PATH, index=False)
    return {"message": "Employee updated successfully"}

  def delete_employee(employee_id: int):
    df = load_employee_data()
    if employee_id not in df["EmployeeID"].values:
        return {"error": "Employee not found"}
    df = df[df["EmployeeID"] != employee_id]
    df.to_csv(EMPLOYEE_DATA_PATH, index=False)
    return {"message": "Employee deleted successfully"}

  def get_avg_salary_by_employee_id(employee_id: int) -> float:
    # Load data
    ed = load_employee_data()
    es = load_salary_data()
    
    # Get the department of the employee
    employee_row = ed[ed["EmployeeID"] == employee_id]
    if employee_row.empty:
        print("Employee not found")
        return None  # Employee not found
    
    department = employee_row.iloc[0]["Department"]
    print(f"Department: {department}")
    
    # Merge employee data with salary data
    merged_data = pd.merge(es, ed[['EmployeeID', 'Department']], on='EmployeeID')
    
    # Filter by department
    department_salaries = merged_data[merged_data["Department"] == department]
    if department_salaries.empty:
        print("No salaries found for the department")
        return None
    
    # Calculate the average salary for that department
    avg_salary = department_salaries["Salary"].mean()
    print(f"Average Salary: {avg_salary} £")
    
    return avg_salary
        
  def get_months_of_service(employee_id: int):
    employee_df = load_employee_data()
    employee = employee_df[employee_df["EmployeeID"] == employee_id]
    if employee.empty:
        return {"error": "Employee not found"}
    start_date = pd.to_datetime(employee["Start_date"].values[0])if not pd.isnull(employee["Start_date"].values[0]) else pd.to_datetime("2020-10-10")
    end_date = pd.to_datetime(employee["End_date"].values[0]) if not pd.isnull(employee["End_date"].values[0]) else pd.to_datetime("today")
    months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    return {"months": months}

  def get_years_of_service(employee_id: int):
    employee_df = load_employee_data()
    employee = employee_df[employee_df["EmployeeID"] == employee_id]
    if employee.empty:
        return {"error": "Employee not found"}
    start_date = pd.to_datetime(employee["Start_date"].values[0])if not pd.isnull(employee["Start_date"].values[0]) else pd.to_datetime("2020-10-10")
    end_date = pd.to_datetime(employee["End_date"].values[0]) if not pd.isnull(employee["End_date"].values[0]) else pd.to_datetime("today")
    years = end_date.year - start_date.year
    return {"years": years}
