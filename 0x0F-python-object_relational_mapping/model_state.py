#!/usr/bin/python3
"""a python file that contains the class definition of a State and
   an instance Base = declarative_base()"""
from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ A class that defines a states table """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
