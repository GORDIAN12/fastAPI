from fastapi import APIRouter
from pydantic import BaseModel
router=APIRouter()

class Todo(BaseModel):
    id: int
    item: str

todo_list = []

@router.post("/")
async def add_todo(todo: Todo):
    todo_list.append(todo)
    return {"message": "Todo added successfully", "todo": todo}

@router.get("/")
async def retrieve_todos():
    return {"todos": todo_list}
