from pydantic import BaseModel
from datetime import datetime

class UserLogin(BaseModel):
    email: str
    password: str

class PaymentInput(BaseModel):
    amount: int
    date: datetime
    merchant_name: str

class PaymentOut(PaymentInput):
    id: int
    class Config:
        orm_mode = True