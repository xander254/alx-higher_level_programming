#!/usr/bin/python3
"""
a script that prints all City objects from the database
"""
import sys
from model_city import City
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id.asc())
        .all()
    )

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
