#!/usr/bin/python3
"""
Module that takes arg and prints the matching state object
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
        f"@localhost:3306/{sys.argv[3]}",
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = sys.argv[4]

    state = (session.query(State).filter(State.name == state_name)).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")
