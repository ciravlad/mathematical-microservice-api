import json
from ..models.db_session import SessionLocal
from ..models.request_log import RequestLog


def log_request(operation: str, input_data: dict, result: int):
    session = SessionLocal()
    try:
        log_entry = RequestLog(
            operation=operation,
            input_data=json.dumps(input_data),
            result=str(result),
        )
        session.add(log_entry)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
