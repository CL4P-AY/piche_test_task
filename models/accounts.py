from datetime import datetime
from pydantic import BaseModel, Field
from typing import Literal

default_currency = "USD"


class Account(BaseModel):
    id: int
    name: str
    balances: dict[str, float]


class CreateAccountRequest(BaseModel):
    name: str
    initial_balance: float = Field(ge=0)
    currency: str = default_currency


class DepositRequest(BaseModel):
    account_id: int
    amount: float = Field(gt=0)
    currency: str = default_currency


class WithdrawRequest(BaseModel):
    account_id: int
    amount: float = Field(gt=0)
    currency: str = default_currency


class TransferRequest(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float = Field(gt=0)
    currency: str = default_currency


class TransactionLog(BaseModel):
    id: int
    timestamp: datetime
    type: Literal["deposit", "withdraw", "transfer"]
    account_id: int | None = None
    from_account_id: int | None = None
    to_account_id: int | None = None
    amount: float
    currency: str
