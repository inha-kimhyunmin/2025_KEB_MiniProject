from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserLogin
from app.database import SessionLocal
from app.crud.user import authenticate_user, create_user
from app.models import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    auth_user = authenticate_user(db, user.email, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"user_id": auth_user.id}


# 회원가입 엔드포인트 추가
@router.post("/register")
def register(user: UserLogin, db: Session = Depends(get_db)):
    # 이메일이 이미 존재하는지 체크
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 새로운 사용자 생성
    new_user = create_user(db, user.email, user.password)
    return {"user_id": new_user.id, "email": new_user.email}

