from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database import get_session
import app.todo.crud as crud
from app.todo.models import TodoRead, TodoCreate, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=list[TodoRead])
def read_todos(session: Session = Depends(get_session)):
    return crud.get_todos(session)

@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = crud.get_todo(session, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoUpdate, session: Session = Depends(get_session)):
    return crud.update_todo(session, todo_id, todo)
@router.post("/", response_model=TodoRead, status_code=201)
def create_todo(todo: TodoCreate, session: Session = Depends(get_session)):
    return crud.create_todo(session, todo)

@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    success = crud.delete_todo(session, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")