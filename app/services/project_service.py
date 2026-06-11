from app.repositories.project_repo import create_project, get_projects, get_project_by_id, delete_project, update_project

def create_project_service(db, data):
    return create_project(db, data.name, data.owner_id)

def list_projects_service(db):
    return get_projects(db)

def get_project_service(db, project_id):
    return get_project_by_id(db, project_id)

def delete_project_service(db, project_id):
    return delete_project(db, project_id)

def update_project_service(db, project_id, data):
    return update_project(db, project_id, data.name, data.owner_id)

