from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import PaymentInput, PaymentOut
from app.crud.payment import create_payment, get_user_payments
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/{user_id}/payments", response_model=PaymentOut)
def add_payment(user_id: int, payment: PaymentInput, db: Session = Depends(get_db)):
    return create_payment(db, user_id, payment)

@router.get("/users/{user_id}/payments", response_model=List[PaymentOut])
def read_payments(user_id: int, db: Session = Depends(get_db)):
    return get_user_payments(db, user_id)