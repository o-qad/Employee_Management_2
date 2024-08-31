from fastapi import FastAPI
from src.controller.employee_controller import employee_router
from src.controller.department_controller import department_router
 
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Employee Management System"} 
 
app.include_router(employee_router)     
app.include_router(department_router)     
      
   
    
     
    
 
   

 








