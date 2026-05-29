'''async job handling
producer (API) / consumer (worker) model
queue (DB-based)
background processing'''

import time
from sqlalchemy.orm import Session

from database import session
from models import Job

from redisclient import redis_client

#THESE ARE DUMMY JOBS BECAUSE THEY ARE NOT THE FOCUS OF THE PROJECT

def process_job(job:Job):
    print(f"Processing {job.id}")

    if job.task_type == "broken":
        raise Exception("Intentional test failure")

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
            job_data=redis_client.blpop("job_queue")
            job_id=int(job_data[1])
            job=db.query(Job).filter(Job.id==job_id).first()

            if not job:
                continue

            job.status="running"
            db.commit()

            process_job(job)

            job.status="completed"
            db.commit()

        except Exception as e:
            print(e)
            if(job):
                job.status="failed"
                job.error_message=str(e)
                job.retry_count+=1
                db.commit()

        finally:
            db.close()

if __name__=="__main__":
    worker_loop()   

