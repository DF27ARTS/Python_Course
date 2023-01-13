
from pymongo import MongoClient

# Base de datos local
# db_client = MongoClient().local

# Base de datos remota
db_client = MongoClient(
    "mongodb+srv://drawings:drawings27@cluster0.xlzzcd1.mongodb.net/?retryWrites=true&w=majority").test
