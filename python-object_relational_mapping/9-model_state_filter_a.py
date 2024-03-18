#!/usr/bin/python3
"""
Write a script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
"""

from model_state import State
from model_state import Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    access to the database and get the states from database.
    """
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.contains('a')):
        print(f"{instance.id}: {instance.name}")
