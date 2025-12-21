from typing import Optional

from sqlmodel import SQLModel, Field


class TodoBase(SQLModel):
    task: str
    done: bool = False

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int

class TodoUpdate(SQLModel):
    task: Optional[str] = None
    done: Optional[bool] = None