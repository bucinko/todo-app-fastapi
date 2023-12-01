from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
import crud

app = FastAPI()


#app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


# Dependency to get the database session
def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@app.get("/todos/")
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db_connection)):
    return crud.get_todos(db=db, skip=skip, limit=limit)
  
  
@app.get("/todo/{id}")
def get_todo_by_id(id: int, db: Session = Depends(get_db_connection)):
    return crud.get_todo_by_id(db=db, todo_id=id)
    if todo_id is None:
        raise HTTPException(status_code=404, detail="Todo not found")    


@app.get("/")
def home(request: Request, db: Session = Depends(get_db_connection), skip: int = 0, limit: int = 100):
    todos = crud.get_todos(db=db)
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

        
@app.post("/todo")
def add_todo(task: str, db: Session = Depends(get_db_connection)):
    return crud.create_todo(db=db, task=task)
    
@app.delete("/todo/{id}")
async def delete_todo(id: int, db: Session = Depends(get_db_connection)):
    db_todo = crud.get_todo_by_id(db=db, todo_id=id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {
        "message": f"Todo {id} deleted successfully",
        "todo_content": f"{db_todo.task} "
            }
    

