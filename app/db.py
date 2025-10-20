import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

load_dotenv() #carga las variables del archivo .env

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./taskdb.sqlite3")

engine = create_engine(
        DATABASE_URL, 
        connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {
                #nada
            }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def on_start
