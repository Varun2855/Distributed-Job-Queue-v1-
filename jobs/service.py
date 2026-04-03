from models import Job,User
from sqlalchemy.orm import Session
from fastapi import HTTPException
from .schemas import JobCreate

def create_job(db:Session,job_data:JobCreate,current_user:User):
    new_job=Job(task_type=job_data.task_type,payload=job_data.payload,user_id=current_user.id)

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job

def get_user_jobs(db:Session,current_user:User):
    jobs=db.query(Job).filter(Job.user_id==current_user.id).all()
     
    return jobs

def get_jobs_by_id(db:Session,job_id:int,current:User):
    job=db.query(Job).filter(Job.id==job_id,Job.user_id==current.id).first()
    if not job:
        raise HTTPException(status_code=404,detail="Job not found")

    return job