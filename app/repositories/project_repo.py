from sqlalchemy.orm import Session
from app.models.project_model import Project

def create_project(db: Session, name: str, owner_id: int):
    project = Project(name=name, owner_id=owner_id)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_projects(db: Session):
    return db.query(Project).all()