#!/usr/bin/python3
"""prints the State object with the name passed as argument
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    res = session.query(State).order_by(State.id) \
        .filter_by(name=sys.argv[4]).first()
    if not res:
        print("Not found")
    else:
        print(res.id)
