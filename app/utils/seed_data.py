from faker import Faker
from app.database import SessionLocal
from app.models.user_model import User
from app.models.post_model import Post

def seed():
    db = SessionLocal()
    fake = Faker()
    for i in range(1000):
        user = User(username=fake.user_name(), email=fake.email(), posts=1000)
        db.add(user)
        db.commit()
        db.refresh(user)
        for _ in range(1000):
            post = Post(user_id=user.id, content=fake.text())
            db.add(post)
        db.commit()
    db.close()
