from sqlalchemy import Column, Integer, String, Float
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    sex = Column(String)
    height = Column(Float)
    weight = Column(Float)
    goal = Column(String)