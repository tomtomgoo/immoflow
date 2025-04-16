from sqlalchemy.orm import Session
from app.models.commission_rate import CommissionRate
from app.api.schemas.commission_rate_schemas import CommissionRateCreate

def list_rates(db: Session):
    return db.query(CommissionRate).order_by(CommissionRate.threshold).all()

def create_rate(db: Session, data: CommissionRateCreate):
    rate = CommissionRate(**data.dict())
    db.add(rate)
    db.commit()
    db.refresh(rate)
    return rate