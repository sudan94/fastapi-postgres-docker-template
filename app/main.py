from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.database_conf import SessionLocal
from app.models import Items
from app.database_conf import engine
from app.routers import itemRouter

Items.Base.metadata.create_all(bind= engine)

app = FastAPI(openapi_url="/fastapi/openapi.json", docs_url="/fastapi/docs",)

origins = [
    "*",
]

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(itemRouter.router)

