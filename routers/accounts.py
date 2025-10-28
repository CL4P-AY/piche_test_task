from fastapi import APIRouter, HTTPException

import in_memory_db
from models.accounts import (
    Account,
    CreateAccountRequest,
    DepositRequest,
    WithdrawRequest,
    TransferRequest,
    TransactionLog,
)
from services.accounts import log_transaction

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.get("/transactions", response_model=list[TransactionLog])
def get_transactions():
    return in_memory_db.TRANSACTIONS


@router.get("/", response_model=list[Account])
def get_all_accounts():
    return list(in_memory_db.ACCOUNTS.values())


@router.get("/{account_id}", response_model=Account)
def get_account(account_id: int):
    if account_id not in in_memory_db.ACCOUNTS:
        raise HTTPException(status_code=404, detail="Account not found")
    return in_memory_db.ACCOUNTS[account_id]


@router.post("/create_account", response_model=Account)
def create_account(request: CreateAccountRequest):
    for account in in_memory_db.ACCOUNTS.values():
        if account.name == request.name:
            raise HTTPException(
                status_code=400, detail="Account with this name already exists"
            )

    account = Account(
        id=in_memory_db.NEXT_ACCOUNT_ID,
        name=request.name,
        balances={request.currency: request.initial_balance},
    )
    in_memory_db.ACCOUNTS[in_memory_db.NEXT_ACCOUNT_ID] = account
    in_memory_db.NEXT_ACCOUNT_ID += 1
    return account


@router.post("/withdraw", response_model=Account)
def withdraw(request: WithdrawRequest):
    if request.account_id not in in_memory_db.ACCOUNTS:
        raise HTTPException(404, "Account not found")
    acc = in_memory_db.ACCOUNTS[request.account_id]
    bal = acc.balances.get(request.currency, 0)
    if bal < request.amount:
        raise HTTPException(400, "Insufficient funds")
    acc.balances[request.currency] = bal - request.amount
    log_transaction(
        type="withdraw",
        account_id=request.account_id,
        amount=request.amount,
        currency=request.currency,
    )
    return acc


@router.post("/transfer", response_model=dict)
def transfer(request: TransferRequest):
    if request.from_account_id not in in_memory_db.ACCOUNTS:
        raise HTTPException(404, "Source account not found")
    if request.to_account_id not in in_memory_db.ACCOUNTS:
        raise HTTPException(404, "Destination account not found")
    from_acc = in_memory_db.ACCOUNTS[request.from_account_id]
    to_acc = in_memory_db.ACCOUNTS[request.to_account_id]
    bal = from_acc.balances.get(request.currency, 0)
    if bal < request.amount:
        raise HTTPException(400, "Insufficient funds")
    from_acc.balances[request.currency] = bal - request.amount
    to_acc.balances[request.currency] = (
        to_acc.balances.get(request.currency, 0) + request.amount
    )
    log_transaction(
        type="transfer",
        from_account_id=request.from_account_id,
        to_account_id=request.to_account_id,
        amount=request.amount,
        currency=request.currency,
    )
    return {"from_account": from_acc, "to_account": to_acc}
