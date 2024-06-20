#!/usr/bin/python3
"""print the State object w/ the name passed as argument from the database"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    first = session.query(State).filter(State.name == argv[4]).first()

    if first:
        print("{}".format(first.id))
    else:
        print("Not found")
    session.close()
