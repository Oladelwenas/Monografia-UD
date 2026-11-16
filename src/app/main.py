"""
Configuaracion inicial de la aplicacion con fastapi.

Autor: Kevin Martinez <kamartinezm@udistrital.edu.co>
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="API Monografía UD",
    description="Backend desarrollado con FastAPI para el proyecto de monografía.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_DIR = BASE_DIR / "static"

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/", tags=["General"])
async def root():
    return {
        "mensaje": "ola wenas",
        "documentacion": "/docs",
    }

@app.get("/health", tags=["General"])
async def health_check():
    return {"status": "ok"}
