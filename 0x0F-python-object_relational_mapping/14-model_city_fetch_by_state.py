#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_4_usa.
"""
import sys
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    try:
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
            ),
            pool_pre_ping=True
        )
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

    except Exception as e:
        print(f"Error: {e}")
