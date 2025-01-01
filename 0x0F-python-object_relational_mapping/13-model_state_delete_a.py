#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import delete
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    conn = engine.connect()
    stmt = delete(State).where(State.name.like('%a%'))
    conn.execute(stmt)
    session.commit()
    session.close()
