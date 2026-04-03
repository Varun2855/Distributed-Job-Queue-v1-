from sqlalchemy import String,Column,Integer,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime,timezone

class Job(Base):

    __tablename__="job"

    id=Column(Integer,primary_key=True,unique=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    task_type=Column(String)
    payload=Column(String)

    status=Column(String,default="pending") #pending running completed failed

    created_at=Column(DateTime,default=datetime.now(timezone.utc))

    owner=relationship("User",back_populates="jobs")

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    hashed_password=Column(String)

    jobs=relationship("Job",back_populates="owner")
