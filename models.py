from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Session

from database import Base

class ToDo(Base):
    __tablename__ = 'todo'
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    