'''async job handling
producer (API) / consumer (worker) model
queue (DB-based)
background processing'''

import time
from sqlalchemy.orm import Session

from database import session
from models import Job

#THESE ARE DUMMY JOBS BECAUSE THEY ARE NOT THE FOCUS OF THE PROJECT

def process_job(job:Job):
    print(f"Processing {job.id} ({job.task_type})")
    time.sleep(2)
    if(job.task_type=='email'):
        print(f"Sending email to {job.payload}")

    elif(job.task_type=="report"):
        print("Generating report")

    else:
        print("Unregistered Job type")
    
def worker_loop():
    while True:
        db:Session=session()   

        try:
            job=db.query(Job).filter(Job.status=="pending").first()

            if(job):
                job.status="running"
                db.commit()

                process_job(job)
                job.status="completed"
                db.commit()

            else:
                time.sleep(3)

        except Exception:
            if(job):
                job.status="failed"
                db.commit()

        finally:
            db.close()

    





if __name__=="__main__":
    worker_loop()

