from pydantic import BaseModel, Field

class DepartmentCreate(BaseModel):
    department_name: str = Field(min_length=1)

    class Config:
        json_schema_extra = {
            'example': {
                'department_name': 'Sales'
            }
        }

class DepartmentUpdate(BaseModel):
    department_name: str = Field(min_length=1)

    class Config:
        json_schema_extra = {
            'example': {
                'department_name': 'Sales'
            }
        }