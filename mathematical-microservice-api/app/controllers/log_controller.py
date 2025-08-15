from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models.db_session import SessionLocal
from ..models.request_log import RequestLog

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    return db.query(RequestLog).all()
