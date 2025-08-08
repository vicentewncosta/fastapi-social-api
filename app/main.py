from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user_router, post_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Social API")

app.include_router(user_router.router)
app.include_router(post_router.router)
