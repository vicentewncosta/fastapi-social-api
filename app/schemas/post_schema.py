from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    user_id: int
    content: str

class PostResponse(BaseModel):
    id: int
    user_id: int
    content: str
    likes: int
    created_at: datetime

    class Config:
        orm_mode = True
