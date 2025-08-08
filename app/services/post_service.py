from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.schemas.post_schema import PostCreate

def create_post(db: Session, post_data: PostCreate):
    post = Post(**post_data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def like_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.likes += 1
        db.commit()
        db.refresh(post)
    return post

def get_feed(db: Session, limit: int, offset: int):
    return db.query(Post).order_by(Post.created_at.desc()).offset(offset).limit(limit).all()
