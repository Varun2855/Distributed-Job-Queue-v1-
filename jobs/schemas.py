from pydantic import BaseModel

class JobCreate(BaseModel):
    task_type:str
    payload:str

class JobResponse(BaseModel):
    id:int
    task_type:str
    payload:str
    status:str

    class Config:
        orm_mode=True
        