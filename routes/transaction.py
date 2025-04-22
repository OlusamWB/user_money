from fastapi import APIRouter, Depends
from deps import get_current_user
from services.transaction import transaction_service

transaction_router = APIRouter()


@transaction_router.get("")
def get_account_transactions(account_id: str, current_user=Depends(get_current_user)):
    return transaction_service.get_transactions_for_account(account_id)
