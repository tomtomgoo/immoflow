# app/api/schemas/bien_schemas.py
from pydantic import BaseModel
class BienCreate(BaseModel):
    titre: str; description: str; adresse: str
    ville: str; code_postal: str; type_bien: str
    surface: float; nb_pieces: int; prix: float
class BienOut(BienCreate):
    id: int
    class Config: from_attributes = True