# app/services/bien_service.py

from sqlalchemy.orm import Session
from app.models.bien import Bien
from app.api.schemas.bien_schemas import BienCreate

def create_bien(db: Session, data: BienCreate) -> Bien:
    db_bien = Bien(**data.dict())
    db.add(db_bien)
    db.commit()
    db.refresh(db_bien)
    return db_bien