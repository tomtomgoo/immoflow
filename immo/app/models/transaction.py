# app/models/transaction.py
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    bien_id = Column(Integer, ForeignKey("biens.id"), nullable=False)
    date_vente = Column(DateTime, default=datetime.utcnow)
    commission = Column(Float, default=0.0)

    bien = relationship("Bien", backref="transactions")