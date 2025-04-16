# app/models/prospect.py
from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Prospect(Base):
    __tablename__ = "prospects"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    actif = Column(Boolean, default=True)