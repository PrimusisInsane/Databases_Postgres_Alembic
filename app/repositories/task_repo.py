from sqlalchemy.orm import Session
from app.models.task_model import Task

def create_task(db: Session, title: str, project_id: int, user_id: int):
    task = Task(
        title=title,
        project_id=project_id,
        user_id=user_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(Task).all()