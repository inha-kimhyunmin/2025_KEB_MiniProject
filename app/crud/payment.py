from sqlalchemy.orm import Session
from app.models import Payment
from app.schemas import PaymentInput

def create_payment(db: Session, user_id: int, payment: PaymentInput):
    db_payment = Payment(user_id=user_id, **payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_user_payments(db: Session, user_id: int):
    return db.query(Payment).filter(Payment.user_id == user_id).all()