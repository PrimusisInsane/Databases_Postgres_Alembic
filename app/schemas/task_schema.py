from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    project_id: int
    user_id: int