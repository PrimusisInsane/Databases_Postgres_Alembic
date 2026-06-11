from app.repositories.project_repo import create_project, get_projects

def create_project_service(db, data):
    return create_project(db, data.name, data.owner_id)

def list_projects_service(db):
    return get_projects(db)