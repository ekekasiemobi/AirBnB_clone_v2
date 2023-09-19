#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """ State class """
    storage_type = environ.get('HBNB_TYPE_STORAGE', 'file')

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        from models.city import City  # Import placed here
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ""

    # For FileStorage
    if storage_type != 'db':
        @property
        def cities(self):
            """Getter attribute cities that returns the list of City instances
               with state_id equals to the current State.id
            """
            city_instances = BaseModel._FileStorage__objects  # Assuming BaseModel has the __objects attribute
            return [city for city in city_instances.values() if city.state_id == self.id]
