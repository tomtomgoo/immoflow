# app/services/dashboard_service.py
from sqlalchemy.orm import Session
from app.models.bien import Bien
from app.models.transaction import Transaction
from app.models.prospect import Prospect
from datetime import datetime

def get_dashboard_kpis(db: Session):
    # Exemple de calculs
    # Biens en gestion : nombre de biens avec statut "en_gestion"
    nb_mandats = db.query(Bien).filter(Bien.statut == "en_gestion").count()

    # Pour l'exemple, nous utilisons le début du mois pour filtrer les ventes
    debut_mois = datetime(datetime.now().year, datetime.now().month, 1)
    ventes_finalisees = db.query(Transaction).filter(Transaction.date_vente >= debut_mois).count()

    # Prospects actifs
    prospects_actifs = db.query(Prospect).filter(Prospect.actif == True).count()

    # Total des commissions sur le mois (ici pour l'exemple, somme des commissions des transactions du mois)
    transactions = db.query(Transaction).filter(Transaction.date_vente >= debut_mois).all()
    commission_annuelle = sum(t.commission for t in transactions) if transactions else 0.0

    # Pour target_mois, chiffre_mois, top_mandats, ventes_en_cours, derniers_messages,
    # nous utilisons des valeurs par défaut ou des listes vides pour l'instant
    return {
         "nb_mandats": nb_mandats,
         "target_mois": 120000.0,       # Valeur d'exemple, à adapter
         "chiffre_mois": 95000.0,       # Valeur d'exemple, à adapter
         "commission_annuelle": commission_annuelle,
         "top_mandats": [],           # Liste vide pour l'instant (à remplacer par des données réelles)
         "ventes_en_cours": [],       # Idem
         "derniers_messages": []      # Idem
    }