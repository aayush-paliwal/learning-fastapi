from fastapi import APIRouter, HTTPException
from config.database import collection_name
from schema.schemas import getAllTodos
from models.todos import Todo
from bson import ObjectId


router = APIRouter()


# GET request 
@router.get("/")
async def get_todos():
    todos = getAllTodos(collection_name.find())
    return todos


@router.post("/")
async def create_todo(todo: Todo):
    try:
        res = collection_name.insert_one(dict(todo))
        return {"status_code": 200, "id": str(res.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occurred {e}")
        

@router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    try:
        res = collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
        return {"status_code": 200, "message": "Task updated successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occurred {e}")
        

@router.delete("/{id}")
async def delete_todo(id: str):
    try:
        collection_name.find_one_and_delete({"_id": ObjectId(id)})
        return {"status_code": 200, "message": "Task deleted successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occurred {e}")