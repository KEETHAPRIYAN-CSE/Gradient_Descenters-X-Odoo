from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.core.database import get_db
from app.auth.auth_service import create_user

from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.name, user.email, user.password)

from app.auth.jwt_handler import create_access_token
from app.schemas.auth import LoginRequest
from app.auth.auth_service import authenticate_user

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
