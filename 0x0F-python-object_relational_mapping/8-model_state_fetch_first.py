#!/usr/bin/python3
""" Display the first state from db """

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

    try:
        state = session.query(State).order_by(State.id).first()
        print("{}: {}".format(state.id, state.name))
    except Exception:
        print("Nothing")
