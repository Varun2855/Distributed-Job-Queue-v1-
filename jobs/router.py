from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import User
from auth.deps import get_current_user

from .schemas import JobCreate,JobResponse
from .service import create_job,get_jobs_by_id,get_user_jobs

router=APIRouter(prefix="/jobs",tags=["jobs"])

@router.post("/",response_model=JobResponse)
def create_job_route(job:JobCreate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return create_job(db,job,current_user)

@router.get("/",response_model=List[JobResponse])
def get_jobs_route(current_user=Depends(get_current_user),db:Session=Depends(get_db)):

    return get_user_jobs(db,current_user)

@router.get("/{job_id}",response_model=JobResponse)
def get_single_job(job_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_jobs_by_id(db,)