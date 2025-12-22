import os
from datetime import datetime, timedelta, UTC
from logging import getLogger
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlmodel import select, Session

from app.auth.models import User

LOGGER = getLogger(__name__)

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    LOGGER.info(f"DEBUG: Password-Typ: {type(password)}, Länge: {len(password)}, Inhalt: {password[:5]}...")
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        return username
    except JWTError:
        return None


def seed_users(session: Session):
    for user in [{"name": "Leon", "pw": "sGZA8j1h8lwN94nEW2ah"}, {"name": "Hanna", "pw": "2syTkB0qvtrSn3fK2N5g"}]:
        statement = select(User).where(User.username == user['name'])
        existing_user = session.exec(statement).first()
        if not existing_user:
            session.add(
                User(username=user['name'], hashed_password=get_password_hash(user['pw']))
            )
            session.commit()
