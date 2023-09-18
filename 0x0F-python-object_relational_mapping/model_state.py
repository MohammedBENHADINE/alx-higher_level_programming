#!/usr/bin/python3
"""model state module"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy import create_engine


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
