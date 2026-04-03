from fastapi import FastAPI
from dotenv import load_dotenv

from database import Base, engine
from auth.router import router as auth_router
from jobs.router import router as jobs_router

load_dotenv()
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth_router)
app.include_router(jobs_router)


@app.get("/")
def root():
    return {"message": "Job Queue System API running"}