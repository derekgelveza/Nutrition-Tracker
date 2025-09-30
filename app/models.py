from sqlalchemy import Column, Integer, String, Float, ForeignKey, DataTime #foreignKey creates link between tables
from sqlalchemy.orm import relationship #relationship allows to move between tables
from .database import Base #imports base from .database and tells sqlalchemy that those classes should be tables
import datetime

class User(Base):
    __tablename__ = "users" #determines name of table in databes

    id = Column (Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    sex = Column(String) #male, female, other, prefer not to say
    height = Column(float) #in cm
    weight = Column(float) #in kg
    goal = Column(String) #lose, gain, maintain