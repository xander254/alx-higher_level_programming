#!/usr/bin/python3
"""
a script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).where(State.name == sys.argv[4]).all()
    if not states:
        print("Not found")
    for state in states:
        print(state.id)
    session.close()
