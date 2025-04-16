from pydantic import BaseModel
from decimal import Decimal

class CommissionRateCreate(BaseModel):
    threshold:   Decimal
    rate_unique: Decimal
    rate_simple: Decimal

class CommissionRateOut(CommissionRateCreate):
    id: int

    class Config:
        from_attributes = True