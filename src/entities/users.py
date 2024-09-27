from sqlalchemy import Column, String, Integer, true
from src.config import Base

class Users(Base) :

    __tablename__="users"

    id = Column(Integer, primary_key=true)
    name = Column(String)

    def __repr__(self) -> str:
        return f"Users [name={self.name}]"