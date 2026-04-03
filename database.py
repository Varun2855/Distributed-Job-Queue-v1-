from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DB=os.getenv("DB")

engine=create_engine(DB)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()


