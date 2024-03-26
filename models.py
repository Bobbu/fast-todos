from fastapi import FastAPI
from pydantic import BaseModel

# Use TodoIn when creating a todo, since the database will provide the ID upon insertion of the new ToDo.
class TodoIn(BaseModel):
    item: str
    completed: bool
    
class Todo(BaseModel):
    id: int
    item: str
    completed: bool
