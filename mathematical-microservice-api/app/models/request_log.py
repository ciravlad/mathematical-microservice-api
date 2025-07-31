from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .base import Base

class RequestLog(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String(50), nullable=False)
    input_data = Column(Text, nullable=False)
    result = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)