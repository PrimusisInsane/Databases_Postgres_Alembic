from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.project_schema import ProjectCreate
from app.services.project_service import create_project_service, list_projects_service

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project_service(db, project)


@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return list_projects_service(db)