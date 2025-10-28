from typing import Dict, List

from models.accounts import Account, TransactionLog
from models.users import User

# Accounts data
ACCOUNTS: Dict[int, Account] = {}
NEXT_ACCOUNT_ID = 1

# Logs data
NEXT_LOG_ID = 1
TRANSACTIONS: List[TransactionLog] = []

# Users data
USERS: Dict[int, User] = {}
