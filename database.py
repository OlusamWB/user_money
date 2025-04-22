import os
from pymongo import mongo_client
from dotenv import load_dotenv

load_dotenv()


client = mongo_client.MongoClient(os.environ.get("DB_URL"))

accounts_collection = client["user_money"]["accounts"]
users_collection = client["user_money"]["users"]
transactions_collection = client["user_money"]["transactions"]
