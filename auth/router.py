from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from models import User
from .schemas import UserCreate
from .utils import hashpassword,verifypassword,create_access_token

router=APIRouter(prefix="/auth",tags=["auth"])

@router.post("/register")
def register(user:UserCreate,db:Session=Depends(get_db)):
    new_user=User(username=user.username,hashed_password=hashpassword(user.password))

    db.add(new_user)
    db.commit()

    return{"message":"user created"}

@router.post("/login")
def login(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):

    user=db.query(User.username==form_data.username).first()

    if not user or not verifypassword(form_data.password,user.hashed_password):
        raise HTTPException(status_code=401,detail="invalid credentials")
    
    token=create_access_token({"sub":user.username})

    return {"access_token":token,"token_type":"bearer"}
