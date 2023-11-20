from dataclasses import dataclass
from typing import Optional

from sqlalchemy import Column, BigInteger, String

from app.store.database.sqlalchemy_base import db


@dataclass
class Map:
    id: Optional[int]
    x: int
    y: int
    type: str
    resource: str

class MapModel(db):
    __tablename__ = "map"
    id = Column(BigInteger, primary_key = True)
    x = Column(BigInteger)
    y = Column(BigInteger)
    type = Column(String)
    resource = Column(String)
