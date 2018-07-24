#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """
        get list of City instances with state_id equals to the current State.id
        """
        list_cities = []
        all_cities = self.cities
        for city in all_cities:
            if city.state_id == State.id:
                list_cities.append(city)
        return list_cities
