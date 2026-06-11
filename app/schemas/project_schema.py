from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    owner_id: int