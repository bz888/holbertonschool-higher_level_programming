#!/usr/bin/python3
"""
Module that prints all states that have the letter 'a' in DB
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

    states = (
        session.query(State).filter(State.name.like("%a%")).order_by(State.id)
    )

    for state in states:
        print(f"{state.id}: {state.name}")
