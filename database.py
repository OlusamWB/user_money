import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("DB_URL"))

db = client["user_money"] 
accounts_collection = db["accounts"]
users_collection = db["users"]
transactions_collection = db["transactions"]
