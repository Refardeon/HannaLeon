from sqlmodel import Session, select
from app.todo.models import Todo, TodoCreate, TodoUpdate


def get_todos(session: Session) -> list[Todo]:
    return list(session.exec(select(Todo)).all())


def get_todo(session: Session, todo_id: int) -> Todo | None:
    return session.get(Todo, todo_id)


def create_todo(session: Session, todo: TodoCreate) -> Todo:
    db_todo = Todo.model_validate(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


def update_todo(session: Session, todo_id: int, todo: TodoUpdate) -> Todo | None:
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        return None

    todo_data = todo.model_dump(exclude_unset=True)
    db_todo.sqlmodel_update(obj=todo_data)

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


def delete_todo(session: Session, todo_id: int) -> bool:
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        return False

    session.delete(db_todo)
    session.commit()
    return True
