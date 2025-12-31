import uuid
from src.models.schemas import PaymentRequest, PaymentStatusResponse

# In-memory mock store
PAYMENTS = {}

def initiate_payment(request: PaymentRequest) -> PaymentStatusResponse:
    payment_id = f"PAY-{uuid.uuid4().hex[:8].upper()}"

    payment = PaymentStatusResponse(
        payment_id=payment_id,
        order_id=request.order_id,
        status="INITIATED",
        amount=request.amount
    )

    PAYMENTS[payment_id] = payment
    return payment

def get_payment_status(payment_id: str) -> PaymentStatusResponse:
    return PAYMENTS.get(
        payment_id,
        PaymentStatusResponse(
            payment_id=payment_id,
            order_id="UNKNOWN",
            status="NOT_FOUND",
            amount=0.0
        )
    )
