#!/usr/bin/python3
"""module for state class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class for State table"""

    __tablename__ = "states"

    id = Column(
        "id",
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )
    name = Column("name", String(128), nullable=False)
