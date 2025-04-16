from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, biens, tasks, contacts, agent
from app.core.database import create_db_and_tables

app = FastAPI(
    title="Plateforme Immobilière",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tu peux restreindre ça aux domaines spécifiques
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(biens.router, prefix="/biens", tags=["biens"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
app.include_router(agent.router, prefix="/agent", tags=["agent"])