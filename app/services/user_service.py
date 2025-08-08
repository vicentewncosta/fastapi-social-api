from typing import Optional, List
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session, joinedload
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

def create_user(db: Session, user_data: UserCreate) -> User:
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_users_with_posts(
    db: Session,
    limit: int,
    offset: int,
    username: Optional[str] = None,  
    email: Optional[str] = None,
    order: Optional[str] = None
) -> List[User]:
    query = _build_base_query(db)
    query = _apply_filters(query, username, email)
    query = _apply_ordering(query, order)
    return query.offset(offset).limit(limit).all()

def _build_base_query(db: Session):
    return db.query(User).options(joinedload(User.user_posts))

def _apply_filters(query, username: Optional[str], email: Optional[str]):
    if username:
        query = query.filter(User.username.ilike(f"%{username}%"))
    if email:
        query = query.filter(User.email.ilike(f"%{email}%"))
    return query

def _apply_ordering(query, order: Optional[str]):
    if order == "asc":
        return query.order_by(asc(User.posts))
    elif order == "desc":
        return query.order_by(desc(User.posts))
    return query