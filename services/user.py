from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from auth import get_password_hash
from schemas.user import UserCreate
from database import users_collection
from serializers import user_in_db_serializer
from bson.objectid import ObjectId


class UserService:

    @staticmethod
    def create_user(user_data: UserCreate):
        user_data = user_data.model_dump()
        user_data["password"] = get_password_hash(user_data["password"])
        user_id = users_collection.insert_one(jsonable_encoder(user_data)).inserted_id
        new_user = users_collection.find_one({"_id": user_id})
        return user_in_db_serializer(new_user)

    @staticmethod
    def get_user_by_email(email: str):
        user = users_collection.find_one({"email": email})
        return user_in_db_serializer(user)

    @staticmethod
    def get_user_by_id(user_id: str):
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail="User with ID does not exist.")
        return user_in_db_serializer(user)


user_service = UserService()
