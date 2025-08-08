from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    posts: int = 0

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
