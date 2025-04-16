# app/models/bien.py
from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime
from app.core.database import Base

class Bien(Base):
    __tablename__ = "biens"
    
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)  # Titre court du bien, par exemple "Appartement lumineux au centre-ville"
    description = Column(Text)  # Description détaillée du bien
    adresse = Column(String, nullable=False)  # Adresse complète
    ville = Column(String, nullable=False)
    code_postal = Column(String, nullable=False)
    type_bien = Column(String, nullable=False)  # Par exemple: "Appartement", "Maison", "Villa", "Local commercial", etc.
    surface = Column(Float, nullable=False)  # Surface en m²
    nb_pieces = Column(Integer)  # Nombre de pièces
    etage = Column(Integer)  # Optionnel : étage si applicable (pour les appartements)
    statut = Column(String, default="en_gestion")  # Statut de la transaction, par exemple "en_gestion", "vendu"
    prix = Column(Float, nullable=False)  # Prix de vente du bien
    date_inscription = Column(DateTime, default=datetime.utcnow)  # Date d'inscription sur le marché