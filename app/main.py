from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import SessionLocal, init_db
from app.models import Task
from app.schemas import TaskIn, TaskOut, TaskUpdate

app = FastAPI(title="Task API")

#DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



app = FastAPI()

@app.get("/")
def root():
	return {"message": "Hello Austin, FastAPI is running!"}
