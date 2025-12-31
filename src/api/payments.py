from fastapi import APIRouter
from src.models.schemas import PaymentRequest, PaymentStatusResponse
from src.services.payment_service import initiate_payment, get_payment_status

router = APIRouter()

@router.post("/initiate", response_model=PaymentStatusResponse)
def initiate(request: PaymentRequest):
    return initiate_payment(request)

@router.get("/{payment_id}", response_model=PaymentStatusResponse)
def status(payment_id: str):
    return get_payment_status(payment_id)
