from sqlalchemy.orm import Session

from app.models import Items


def get_items(db: Session, skip: int =0, limit:  int = 100):
    return db.query(Items.Item).offset(skip).limit(limit).all()


