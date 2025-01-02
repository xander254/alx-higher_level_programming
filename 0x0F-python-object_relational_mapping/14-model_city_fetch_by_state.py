#!/usr/bin/python3
"""
Fetches and prints all City objects from the database hbtn_0e_14_usa,
sorted by cities.id in ascending order.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/"
        f"{database_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
