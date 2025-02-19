from fastapi import APIRouter, Path, HTTPException, status
from pydantic import BaseModel
router=APIRouter()

class Todo(BaseModel):
    id: int
    item: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra={
            "example":{
                "item": "Read the next chapter of the book"
                }
            }

class TodoItems(BaseModel):
    todos: list[TodoItem]

    class Config:
        json_schema_extra={
                    "example":{
                        "todos": [
                            {    "item": "Example schema 1"},
                            {    "item": "Example schema 2"},
                            {    "item": "Example schema 3"},
                            ]
                        }
                }

todo_list = []

@router.post("/")
async def add_todo(todo: Todo):
    todo_list.append(todo)
    return {"message": "Todo added successfully", "todo": todo}
    
@router.get("/")
async def retrieve_todos():
    return {"todos": todo_list}

@router.get("/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrive.")):
    for todo in todo_list:
        if todo.id==todo_id:
            return {
                "todo": todo
                    }
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn´t exist",
            )

@router.put("/{todo_id}")
async def update_todo(todo_data: TodoItem,  todo_id: int= Path(..., title="The Id of the todo to be update")):
    for todo in todo_list:
        if todo.id==todo_id:
            todo.item=todo_data.item
            return {
                    "message": "Todo updated successfully"
                    }
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn´t exist",
            )

@router.delete("/{todo_id}")
async def delete_single_todo(todo_id: int):
    for index in range(len(todo_list)):
        todo=todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                    "message":"Todo deleted succesfully" 
                    }
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Todo with supplied ID doesn´t exist",
            )

@router.delete("/")
async def delete_all_todo():
    todo_list.clear()
    return {
        "message": "Todos deleted succesfully"
            }

@router.get("/", response_model=TodoItems)
async def retrieve_todo():
    return {
        "todos": todo_list
    }
