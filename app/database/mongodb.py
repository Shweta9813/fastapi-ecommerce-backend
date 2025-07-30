from pymongo import MongoClient
from config import settings

client = MongoClient(settings.MONGO_URI)

db = client["ecommerce_db"]

users_collection = db["users"]
products_collection = db["products"]
orders_collection = db["orders"]
<<<<<<< HEAD

=======
>>>>>>> af3ec91 (Implemented user registration router)
