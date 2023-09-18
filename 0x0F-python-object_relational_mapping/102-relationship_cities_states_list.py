#!/usr/bin/python3
"""script to create city and state object"""
from sqlalchemy.engine import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import Base, State
from sys import argv


if __name__ == "__main__":

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}"
            .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city, state in session.query(City, State)\
                              .filter(City.state_id == State.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
