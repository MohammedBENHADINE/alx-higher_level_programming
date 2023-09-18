#!/usr/bin/python3
"""city module"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """Class city"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State")

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id
