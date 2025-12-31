from fastapi import FastAPI
from src.api.payments import router as payment_router

app = FastAPI(title="Clothing Payment Service")

app.include_router(payment_router, prefix="/payments", tags=["Payments"])

@app.get("/health")
def health_check():
    return {"status": "UP"}
