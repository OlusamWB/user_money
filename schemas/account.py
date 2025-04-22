from decimal import Decimal
from typing import Union
from pydantic import BaseModel, condecimal
from datetime import datetime
from enum import Enum


class AccountType(Enum):
    savings = "savings"
    current = "current"


class AccountBase(BaseModel):
    account_type: Union[AccountType, str] = AccountType.savings.value


class AccountCreatePayload(AccountBase):
    pass


class AccountCreate(AccountBase):
    user_id: str
    balance: Decimal = condecimal(ge=0, decimal_places=2)
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class Account(AccountBase):
    user_id: str
    balance: Decimal
    created_at: datetime
    updated_at: datetime


class AccountDb(Account):
    id: str

class TransactionPayload(BaseModel):
    amount: Decimal