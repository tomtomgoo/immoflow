# app/api/schemas/dashboard_schemas.py
from typing import List
from pydantic import BaseModel

class Mandat(BaseModel):
    id: int
    description: str
    potentiel: str  # "élevé", "moyen", "faible"

class VenteEnCours(BaseModel):
    id: int
    progression: int  # en pourcentage
    taches_restantes: List[str]

class DashboardAgent(BaseModel):
    nb_mandats: int
    target_mois: float
    chiffre_mois: float
    commission_annuelle: float
    top_mandats: List[Mandat]
    ventes_en_cours: List[VenteEnCours]
    derniers_messages: List[str]

    class Config:
        # Pour Pydantic V2
        from_attributes = True