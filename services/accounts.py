from models.accounts import TransactionLog
import in_memory_db
from datetime import datetime, UTC


def log_transaction(**kwargs):
    log = TransactionLog(
        id=in_memory_db.NEXT_LOG_ID, timestamp=datetime.now(UTC), **kwargs
    )
    in_memory_db.TRANSACTIONS.append(log)
    in_memory_db.NEXT_LOG_ID += 1
    return log
