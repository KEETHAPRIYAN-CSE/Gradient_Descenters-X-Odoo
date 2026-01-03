from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.hashing import hash_password, verify_password

def create_user(db: Session, name: str, email: str, password: str):
    hashed = hash_password(password)
    user = User(name=name, email=email, password_hash=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

def create_user(db: Session, name: str, email: str, password: str):
    user = User(
        name=name,
        email=email,
        password_hash=hash_password(password)
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    db.refresh(user)
    return user

from app.auth.hashing import verify_password
from app.models.user import User

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user
