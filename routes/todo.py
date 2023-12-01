


def find_todo_by_id(target_id):
    for todo in todos:
        if todo["id"] == target_id:
            return todo
    return None

def get_all_todos(todos: dict):
    for todo in todos:
        return todo

@app.get('/todos/{todo_id}')
def read_todo(todo_id: int):
    todo = find_todo_by_id(todo_id)
    if todo:
        return todo
    raise HTTPException(status_code=400, detail="Todo with this ID already exists")

@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    todo = find_todo_by_id(todo_id)
    if todo:
        todos.remove(todo)
        return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

def add_todo_with_check(new_todo):
    target_id = new_todo["id"]
    if find_todo_by_id(target_id):
        raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    else:
        todos.append(new_todo)
        return {"message": "Todo added successfully"}
    
@app.post("/todos/")
def create_todo(new_todo: dict):
    try:
        result = add_todo_with_check(new_todo)
        return result
    except HTTPException as e:
        raise e

@app.get("/todos/")
def query_todos(search : str = Query(None, description="seach todos by value")):
    if search:
        search = search.lower()
        matching_todos = [
           todo for todo in todos
                if search in todo["title"] or search in todo["todos"] 
            ]
        return matching_todos
    return todos



