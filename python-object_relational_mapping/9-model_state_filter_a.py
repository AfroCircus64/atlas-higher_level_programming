#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database"""

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

    first = session.query(State).order_by(State.id).first()

    for first in session.query(State).\
            filter(State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(first.id, first.name))
    session.close()
