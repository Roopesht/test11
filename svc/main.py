from fastapi import FastAPI, Depends
import logging
logging.basicConfig(level=logging.INFO)
from datetime import datetime
from pydantic import BaseModel, Field, validator
from fastapi.responses import JSONResponse
from fastapi import HTTPException
# sqlalchemy
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Task

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Read all tasks
@app.get("/tasks")
def get_all_tasks (db: Session = Depends(get_db)):
    logging.info("Fetching all tasks")
    tasks = db.query(Task).all()
    return tasks

# Healrth check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }
