# app/models/commission_rate.py
from sqlalchemy import Column, Integer, Numeric
from app.core.database import Base

class CommissionRate(Base):
    __tablename__ = "commission_rates"

    id = Column(Integer, primary_key=True, index=True)
    threshold = Column(Numeric(12, 2), nullable=False)  # palier de CA
    rate_unique = Column(Numeric(5, 2), nullable=False)  # % mandat exclusif
    rate_simple = Column(Numeric(5, 2), nullable=False)  # % mandat simple