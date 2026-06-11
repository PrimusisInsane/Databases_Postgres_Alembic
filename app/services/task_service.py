from app.repositories.task_repo import create_task, get_tasks

def create_task_service(db, data):
    return create_task(db, data.title, data.project_id, data.user_id)

def list_tasks_service(db):
    return get_tasks(db)