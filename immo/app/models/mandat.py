from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Mandat(Base):
    __tablename__ = "mandats"

    id = Column(Integer, primary_key=True, index=True)
    bien_id = Column(Integer, ForeignKey("biens.id"), nullable=False)
    agent_entree_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pourcentage_entree = Column(Numeric(5,2), nullable=False)  # ex. 50.00 pour 50%
    agent_sortie_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    pourcentage_sortie = Column(Numeric(5,2), nullable=True)   # peut être null si pas encore affecté
    date_debut = Column(DateTime, default=datetime.utcnow)     # date de prise de mandat
    date_fin = Column(DateTime, nullable=True)                 # date de fin de mandat (vente / expiration)

    bien = relationship("Bien", back_populates="mandats")
    agent_entree = relationship("User", foreign_keys=[agent_entree_id])
    agent_sortie = relationship("User", foreign_keys=[agent_sortie_id])
