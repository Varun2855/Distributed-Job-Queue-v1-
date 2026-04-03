from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta,timezone
import os
from dotenv import getenv

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(password:str,hashed_password:str)->bool:
    return pwd_context.verify(password,hashed_password)

def create_access_token(data:dict, expires_delta:timedelta|None=None):
    to_encode=data.copy()

    expire=datetime.now(timezone.utc)+(expires_delta or timedelta(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp":expire})

    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def decode_token(token:str):
    return jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)