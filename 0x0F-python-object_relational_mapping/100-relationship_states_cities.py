#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database
"""
import sys
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    newState = State(name="California")
    newCity = City(name="San Francisco")
    newCity.state = newState
    session.add(newState)
    session.add(newCity)
    session.commit()
