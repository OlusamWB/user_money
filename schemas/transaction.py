from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from enum import Enum


class TransactionType(Enum):
    debit = "debit"
    credit = "credit"


class TransactionBase(BaseModel):
    transaction_type: TransactionType
    amount: Decimal


class TransactionPayload(BaseModel):
    amount: Decimal


class Transaction(BaseModel):
    id: str
    account_id: str
    amount: Decimal
    transaction_type: str
    date: datetime


class DepositTransaction(BaseModel):
    account_id: str
    amount: Decimal
    transaction_type: str = TransactionType.credit.value
    date: datetime = datetime.now()


# class WithdrawTransaction(T)


class TransactionDb(TransactionBase):
    account_id: str
    date: datetime
