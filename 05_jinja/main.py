from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

DOGS = [{"name": "Tyson", "type": "Labra"}, {"name": "Mike", "type": "German"}]

@app.get("/")
async def name(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "Home Page", "dogs": DOGS})