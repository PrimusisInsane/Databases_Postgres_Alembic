from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.task_schema import TaskCreate
from app.services.task_service import create_task_service, list_tasks_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(db, task)


@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return list_tasks_service(db)