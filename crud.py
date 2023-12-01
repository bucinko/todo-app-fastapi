from sqlalchemy.orm import Session
from models import Todo

def create_todo(db: Session, task: str):
    db_todo = Todo(task=task)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Todo).offset(skip).limit(limit).all()

# def get_todo(db: Session, todo_id: int):
#     return db.query(Todo).filter(Todo.id == todo_id).first()


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


# def delete_todo_by_id(db: Session, todo_id: int):
#     todo = db.query(Todo).filter(Todo.id==id).first()
#     db.delete(todo)
    
#     return {"todo deleted": todo }