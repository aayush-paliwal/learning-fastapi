from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi




uri = "mongodb+srv://dbUser:dbUserPassword@cluster0.gnt7h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.todo_db
collection_name = db["todo_collection"]