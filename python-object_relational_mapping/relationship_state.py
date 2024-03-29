#!/usr/bin/python3
"""
    This module defines the State class with attributes id and name
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from re import Base


Base = declarative_base()


class State(Base):
    """
        State class with attributes id and name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
