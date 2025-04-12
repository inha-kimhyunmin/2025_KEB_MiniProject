from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserLogin
from passlib.context import CryptContext  # 패스워드 해싱 라이브러리

# 비밀번호 해시를 위한 CryptContext 인스턴스 생성
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 비밀번호 해싱 함수
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# 비밀번호 검증 함수
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user and verify_password(password, user.password):  # 해시된 비밀번호 비교
        return user
    return None

def create_user(db: Session, email: str, password: str):
    hashed_password = hash_password(password)  # 비밀번호 해싱
    db_user = User(email=email, password=hashed_password)  # 새로운 사용자 생성
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
