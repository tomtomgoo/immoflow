from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services.settings_service import list_rates, create_rate
from app.api.schemas.commission_rate_schemas import CommissionRateCreate, CommissionRateOut

router = APIRouter(prefix="/settings", tags=["settings"])

def get_db():
    db = SessionLocal()
    try:   yield db
    finally: db.close()

@router.get("/commission-rates", response_model=list[CommissionRateOut])
def read_commission_rates(db: Session = Depends(get_db)):
    return list_rates(db)

@router.post("/commission-rates", response_model=CommissionRateOut, status_code=status.HTTP_201_CREATED)
def add_commission_rate(rate: CommissionRateCreate, db: Session = Depends(get_db)):
    return create_rate(db, rate)