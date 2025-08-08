from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.post_schema import PostCreate, PostResponse
from app.services.post_service import create_post, like_post, get_feed
from app.database import SessionLocal

router = APIRouter(prefix="/posts", tags=["Posts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PostResponse)
def new_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_post(db, post)

@router.post("/{post_id}/like")
def like(post_id: int, db: Session = Depends(get_db)):
    return like_post(db, post_id)

@router.get("/feed", response_model=list[PostResponse])
def feed(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    return get_feed(db, limit, offset)
