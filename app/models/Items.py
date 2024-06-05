from sqlalchemy import Column, Integer, String

from app.database_conf import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String,index=True)
