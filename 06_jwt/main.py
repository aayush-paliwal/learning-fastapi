from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from database import engine, SessionLocal, Base
import models
import auth
from auth import get_current_user

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# Annotated allows us to put additinal metadata along with the types
# Ex: name: Annotated[str, "this is just metadata"]
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return {"User": user}


app.include_router(auth.router)