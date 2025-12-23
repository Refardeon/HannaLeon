from sqlmodel import SQLModel, Field
from typing import Optional


class UserBase(SQLModel):
    username: str = Field(unique=True, index=True)
    logo: Optional[int] = Field(ge=1, le=3, default=None)

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

class UserUpdate(SQLModel):
    username: Optional[str] = None
    logo: Optional[int] = None

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    username: Optional[str] = None

