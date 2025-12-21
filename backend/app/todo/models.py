from typing import Optional

from sqlmodel import SQLModel, Field


class TodoBase(SQLModel):
    task: str
    done: bool = False

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order: int = 0

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: int
    order: int


class TodoUpdate(SQLModel):
    task: Optional[str] = None
    done: Optional[bool] = None

class TodoReorder(SQLModel):
    id: int
    order: int