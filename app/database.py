import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Database URL (This is where all the users info will exsist)
SQLALCHEMY_DATABASE_URL = "sqlite:///./nutrition.db"

#connection for the database
engine = create_engine (
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#autocommit-False -> changes are not saved unil you say commit
#autoflush=False -> stops automatic sending of changes until you're ready
#bind=engine ties the session to database (sqlconnection)
#Hanlde for databse. Every request is its own session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#allows for python to map to sql tables
Base = declarative_base ()

#database.py connectos to pythong and sqlite
#other fiels define the tables using Base
#this will allow users to store weight goals, meals, progress withing the database safely