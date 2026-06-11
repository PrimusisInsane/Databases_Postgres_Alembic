from app.repositories.user_repo import create_user, get_users

def create_user_service(db, data):
    return create_user(db, data.name, data.email)

def list_users_service(db):
    return get_users(db)