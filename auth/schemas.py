from pydantic import BaseModel, Field #It just lets you add constraints + validation to your inputs.

class UserCreate(BaseModel):
    username:str=Field(min_length=3,max_length=50)
    password:str

class UserLogin(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    username:str|None=None

class UserResponse(BaseModel):
    id:int
    username:str

    class Config:
        orm_mode:True



