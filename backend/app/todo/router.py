from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

import app.todo.crud as crud
from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.database import get_session
from app.todo.models import TodoRead, TodoCreate, TodoUpdate, TodoReorder

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=list[TodoRead])
def read_todos(
        session: Session = Depends(get_session),
        _current_user: User = Depends(get_current_user)):
    return crud.get_todos(session)


@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(
        todo_id: int,
        session: Session = Depends(get_session),
        _current_user: User = Depends(get_current_user)):
    todo = crud.get_todo(session, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.post("/", response_model=TodoRead, status_code=201)
def create_todo(
        todo: TodoCreate,
        session: Session = Depends(get_session),
        _current_user: User = Depends(get_current_user)):
    return crud.create_todo(session, todo)


# Befor /{todo_id} to avoid collision
@router.patch("/reorder")
def reorder_todos(
        reorders: list[TodoReorder],
        session: Session = Depends(get_session),
        _current_user: User = Depends(get_current_user)):
    reorder_dicts = [{"id": r.id, "order": r.order} for r in reorders]
    crud.reorder_todos(session, reorder_dicts)
    return {"success": True}


@router.patch("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int,
                todo: TodoUpdate,
                session: Session = Depends(get_session),
                _current_user: User = Depends(get_current_user)):
    return crud.update_todo(session, todo_id, todo)


@router.delete("/{todo_id}", status_code=204)
def delete_todo(
        todo_id: int,
        session: Session = Depends(get_session),
        _current_user: User = Depends(get_current_user)):
    success = crud.delete_todo(session, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
