#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", primaryjoin="City.state_id==State.id", cascade="delete")
