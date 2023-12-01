import csv
import uuid
#from datetime   import timedelta
from fastapi import FastAPI, HTTPException, Query, Depends, Form, Request, Response
from fastapi.responses import HTMLResponse, FileResponse

from fastapi.templating import Jinja2Templates
import sqlalchemy , sqlite3
from database import SessionLocal, Base, engine
from models import ToDo
from sqlalchemy.orm import Session


app = FastAPI()
conn = sqlite3.connect("todos.db")
cursor = conn.cursor()


Base.metadata.create_all(bind=engine)

def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def home(request: Request, db: Session = Depends(get_db_connection), skip: int = 0, limit: int = 100):
    todos = db.query(ToDo).offset(skip).limit(limit).all()
    return todos
        
@app.post("/create")
def add_todo(request: Request, content: str , db: Session = Depends(get_db_connection)):
    todo = ToDo(content=content)
    print(todo.content)
    db.add(todo)
    db.commit()
    return todo.content
    
@app.delete("/delete/{id}")
async def delete_todo(id: int, request: Request, db: Session = Depends(get_db_connection)):
    todo = db.query(ToDo).filter(ToDo.id==id).first()
    db.delete(todo)
    db.commit()
    return {"todo deleted": todo.content}


