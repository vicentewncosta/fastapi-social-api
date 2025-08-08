from pydantic import BaseModel
from app.schemas.post_schema import PostResponse
class UserCreate(BaseModel):
    username: str
    email: str
    posts: int = 0

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class UserWithPostsResponse(BaseModel):
    id: int
    username: str
    posts: int
    email: str
    user_posts: list[PostResponse]

    class Config:
        orm_mode = True