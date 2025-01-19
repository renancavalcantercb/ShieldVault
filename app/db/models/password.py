from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from datetime import datetime
from app.db.session import Base


class Password(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    service_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password_encrypted = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    url = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
