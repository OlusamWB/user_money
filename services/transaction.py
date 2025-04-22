from database import transactions_collection
from serializers import transaction_serializer


class TransactionService:

    @staticmethod
    def get_transactions_for_account(account_id: str) -> list[dict]:
        transactions_cursor = transactions_collection.find(
            {"account_id": account_id}
        ).sort("date", -1)  # Sort by most recent

        return [transaction_serializer(txn) for txn in transactions_cursor]


transaction_service = TransactionService()
