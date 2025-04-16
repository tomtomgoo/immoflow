# app/api/schemas/user_schemas.py

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str = "agent"  # par défaut "agent"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        # Pour Pydantic V2, remplacez orm_mode par from_attributes
        from_attributes = True