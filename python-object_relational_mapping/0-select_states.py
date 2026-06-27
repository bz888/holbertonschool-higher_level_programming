#!/usr/bin/python3
"""List all states from a MySQL database using SQLAlchemy."""

import sys

from sqlalchemy import MetaData, Table, create_engine, select


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True,
    )

    metadata = MetaData()
    states = Table("states", metadata, autoload_with=engine)
    stmt = select(states).order_by(states.c.id)

    with engine.connect() as connection:
        for row in connection.execute(stmt):
            print(tuple(row))
