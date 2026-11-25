"""SunuPrix - API backend (squelette).

Ce fichier est le point de depart : B1 le complete avec les endpoints
du contrat d'API (catalogue, prix, comparaison, auth, moderation...).
"""
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SunuPrix API",
    description="Consultation et comparaison des prix observes dans les marches senegalais.",
    version="0.1.0",
)

# Origines autorisees pour le frontend (a restreindre en production).
origins = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Sante"])
def health():
    """Health check utilise par Kubernetes (readiness / liveness)."""
    return {"status": "ok", "service": "sunuprix-backend"}
