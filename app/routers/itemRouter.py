from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import itemSchema
from app.controller import itemContoller
from app.database_conf import get_db

router = APIRouter(prefix="/fastapi/items",
    tags=["Items"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_db)],
)

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("", response_model=list[itemSchema.ItemBase])
def all_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = itemContoller.get_items(db, skip=skip, limit=limit)
    return items