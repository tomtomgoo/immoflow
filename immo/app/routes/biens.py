# app/routes/biens.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.api.schemas.bien_schemas import BienCreate, BienOut
from app.services.bien_service import create_bien

router = APIRouter()

def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()

@router.post("/", response_model=BienOut)
def add_bien(b: BienCreate, db: Session = Depends(get_db)):
    return create_bien(db, b)