from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base() 


class Todo(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    