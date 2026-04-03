from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError
from sqlalchemy.orm import Session

from database import get_db
from models import User
from .utils import decode_token
from dotenv import load_dotenv

load_dotenv()

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):

    try:
        payload=decode_token(token)
        username=payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401,detail="Invalid Token")
        
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid Token")
    
    user=db.query(User).filter(User.username==username).first()

    if user is None:
        raise HTTPException(status_code=401,detail="User not found")
    
    return user


