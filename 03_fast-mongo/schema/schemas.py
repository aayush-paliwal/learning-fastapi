def getTodo(todo): 
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "completed": todo["completed"],
    }


def getAllTodos(todos):
    return [getTodo(todo) for todo in todos]