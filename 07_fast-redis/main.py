import json
import httpx 
from redis import Redis
from fastapi import FastAPI


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    # app.state.redis: Here, a Redis client is instantiated and connected to a Redis server running on localhost at port 6379. This Redis client is assigned to the app's state so it can be accessed globally in the app.
    # app.state.http_client: An asynchronous HTTP client (httpx.AsyncClient()) is also instantiated and stored in the app's state. This client will be used for making non-blocking HTTP requests.
    app.state.redis = Redis(host='localhost', port=6379)
    app.state.http_client = httpx.AsyncClient()

@app.on_event("shutdown")
async def shutdown_event():
    app.state.redis.close()


@app.get("/entries")
async def read_items():
    value = app.state.redis.get('entries')

    if value is None:
        response = await app.state.http_client.get("https://jsonplaceholder.typicode.com/comments")
        value = response.json()
        data_str = json.dumps(value)
        app.state.redis.set('entries', data_str)
    
    return json.loads(value)