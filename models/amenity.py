#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    def places(self):
        """ Returns the list of Place instances with this Amenity """
        from models import storage
        place_amenities = []
        for place in storage.all("Place").values():
            if self.id in [amenity.id for amenity in place.amenities]:
                place_amenities.append(place)
        return place_amenities
