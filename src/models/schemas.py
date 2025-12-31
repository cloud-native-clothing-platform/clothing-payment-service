from pydantic import BaseModel

class PaymentRequest(BaseModel):
    order_id: str
    amount: float
    currency: str = "INR"

class PaymentStatusResponse(BaseModel):
    payment_id: str
    order_id: str
    status: str
    amount: float
