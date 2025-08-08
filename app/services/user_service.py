from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from sqlalchemy.orm import Session, joinedload
from app.models.user_model import User

def create_user(db: Session, user_data: UserCreate):
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users_with_posts(db: Session, limit: int, offset: int):
    return db.query(User).offset(offset).limit(limit).all()

def get_users_with_posts(db: Session, limit: int, offset: int):
    return (
        db.query(User)
        .options(joinedload(User.posts))
        .offset(offset)
        .limit(limit)
        .all()
    )