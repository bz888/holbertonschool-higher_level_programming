#!/usr/bin/python3
"""module for city class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Class for city table"""

    __tablename__ = "cities"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False,
    )
