from faker import Faker
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user_model import User
from app.models.post_model import Post
import time

fake = Faker()
db: Session = SessionLocal()

def seed_users_and_posts(user_count=100, posts_per_user=100):
    start = time.time()
    users = []
    posts = []

    for _ in range(user_count):
        username = fake.unique.user_name()
        email = fake.unique.email()
        user = User(username=username, email=email, posts=posts_per_user)
        users.append(user)

    db.bulk_save_objects(users)
    db.commit()

    db_users = db.query(User).all()

    for user in db_users:
        for _ in range(posts_per_user):
            post = Post(
                title=fake.sentence(nb_words=6),
                content=fake.paragraph(nb_sentences=3),
                user_id=user.id
            )
            posts.append(post)

        if len(posts) >= 1000:
            db.bulk_save_objects(posts)
            db.commit()
            posts.clear()

    if posts:
        db.bulk_save_objects(posts)
        db.commit()

    print(f"⏱️ Tempo de execução: {time.time() - start:.2f} segundos")
    db.close()
    print(f"✅ Seed finalizado: {user_count} usuários e {user_count * posts_per_user} posts.")

if __name__ == "__main__":
    seed_users_and_posts()