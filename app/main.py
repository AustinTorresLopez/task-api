from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import SessionLocal, init_db
from app.models import Task
from app.schemas import TaskIn, TaskOut, TaskUpdate

app = FastAPI(title="Task API")


# Dependencia de DB
#DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
#Crear tablas al iniciar
@app.on_event("startup")
def on_startup():
    init_db()

#Endpoints
@app.get("/")
def root():
	return {"message": "Hello Austin, FastAPI is running!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tasks", response_model=TaskOut, status_code=201)
def create_task(payload: TaskIn, db: Session = Depends(get_db)):
    task = Task(title=payload.title, done=False)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get("/tasks", response_model=list[TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=TaskOut)
@app.patch("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if payload.title is not None:
        task.title = payload.title
    if payload.done is not None:
        task.done = payload.done
    
    db.commit()
    db.refresh(task)
    return task

@app.post("/tasks/{task_id}/done", response_model=TaskOut)
def mark_done(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.done = True
    db.commit()
    db.refresh(task)
    return task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return None














