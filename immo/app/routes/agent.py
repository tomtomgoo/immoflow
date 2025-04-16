# app/routes/agent.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services.dashboard_service import get_dashboard_kpis
from app.api.schemas.dashboard_schemas import DashboardAgent

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/kpis", response_model=DashboardAgent)
def agent_kpis(db: Session = Depends(get_db)):
    kpis = get_dashboard_kpis(db)
    return kpis