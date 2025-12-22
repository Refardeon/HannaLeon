from typing import Optional

from fastapi import Depends, HTTPException, status, Cookie, Header
from fastapi.security import HTTPBearer, APIKeyCookie
from sqlmodel import Session, select
from app.database import get_session
from app.auth.models import User
from app.auth.utils import decode_token

security = HTTPBearer(auto_error=False)
cookie_scheme = APIKeyCookie(name="access_token", auto_error=False)


async def get_current_user(
        _token_bearer: Optional[str] = Depends(security),
        _token_cookie_ui: Optional[str] = Depends(cookie_scheme),
        access_token: Optional[str] = Cookie(None),
        authorization: Optional[str] = Header(None),
        session: Session = Depends(get_session)
) -> User:
    token = None

    if access_token:
        token = access_token
    elif authorization and authorization.startswith("Bearer "):
        token = authorization.replace("Bearer ", "")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    username = decode_token(token)

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )

    user = session.exec(select(User).where(User.username == username)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user
