from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Todo, TodoIn
from database import metadata, engine, database,todos

metadata.create_all(engine)

app = FastAPI(title="Fast Todo API")

### CORS ################
# Permit both client and server on the localhost but seemingly different origins.
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### Lifecycle Events ###

#TODO on_event is deprecated, use lifespan event handlers instead.
@app.on_event("startup")
async def startup():
    await database.connect()

#TODO on_event is deprecated, use lifespan event handlers instead.
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

### Routes ##############

@app.get("/")
async def root():
    timePart = datetime.now().strftime("%H:%M:%S")
    return {"message": f"Hello To Båbø's World at {timePart}!!!"}

# Get all todos
@app.get("/todos", response_model=list[Todo])
async def get_todos():
    query = todos.select()
    return await database.fetch_all(query)

# Get single todo
@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    query = f"SELECT * FROM todos WHERE id = {todo_id}"
    #TODO This is failing with a 500 server error if the passed in todo_id is not valid.
    try:
        return await database.fetch_one(query)
    except:
        raise HTTPException(status_code=404, detail="Item not found")
    
#TODO .dict() is also deprecated
# Create a todo
@app.post("/todos", response_model=Todo)
async def create_todo(todo: TodoIn):
    query = todos.insert().values(item=todo.item, completed=todo.completed)
    last_record_id = await database.execute(query)
    return {**todo.dict(), "id" : last_record_id}


# Update a todo
@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, updated_todo: TodoIn):
    query = f"UPDATE todos SET item = '{updated_todo.item}', completed = {updated_todo.completed} WHERE id = {todo_id}"
    await database.execute(query)
    new_query = f"SELECT * from todos where id = {todo_id}"
    return await database.fetch_one(new_query)

# Delete a todo
@app.delete("/todos/{todo_id}", response_model=list[Todo])
async def delete_todo(todo_id: int):
    query = f"DELETE FROM todos WHERE id = {todo_id}"
    await database.execute(query)
    new_query = todos.select()
    return await database.fetch_all(new_query)

