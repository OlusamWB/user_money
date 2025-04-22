from schemas.user import User, UserDb
from schemas.account import AccountDb
from schemas.transaction import Transaction


def user_serializer(user) -> User:
    user_dict = {
        "id": str(user.get("_id")),
        "first_name": user.get("first_name"),
        "last_name": user.get("last_name"),
        "bvn": user.get("bvn"),
        "phone": user.get("phone"),
        "email": user.get("email"),
    }
    return User(**user_dict)


def user_in_db_serializer(user) -> UserDb:
    user_dict = {
        "id": str(user.get("_id")),
        "first_name": user.get("first_name"),
        "last_name": user.get("last_name"),
        "bvn": user.get("bvn"),
        "phone": user.get("phone"),
        "email": user.get("email"),
        "password": user.get("password")
    }
    return UserDb(**user_dict)


def account_serializer(account) -> AccountDb:
    account_dict = {
        "id": str(account.get("_id")),
        "user_id": account.get("user_id"),
        "created_at": account.get("created_at"),
        "updated_at": account.get("updated_at"),
        "balance": account.get("balance"),
        "account_type": account.get("account_type"),
    }
    return AccountDb(**account_dict)



def transaction_serializer(transaction) -> Transaction:
    transaction_dict = {
        "id": str(transaction["_id"]),
        "account_id": transaction.get("account_id"),
        "amount": transaction["amount"],
        "transaction_type": transaction["transaction_type"],
        "date": transaction["date"].isoformat(),
    }
    return Transaction(**transaction_dict)