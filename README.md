# Task API (FastAPI)

API minima para gestionar tareas. Hecha para practicar FastAPI, SQLAlchemy y despliegue

## Requisitos
- Python 3.10+
- Linux/WSL o macOS (Windows con WSL)

## Instalar y correr
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# Abrir: http://127.0.0.1:8000/docs
```
