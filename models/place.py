#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ This is the class for Place """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    @property
    def reviews(self):
        """ Returns list of Review instances with this Place """
        from models import storage
        reviews = []
        for review in storage.all("Review").values():
            if review.place_id == self.id:
                reviews.append(review)
        return reviews

    @property
    def amenities(self):
        """ Returns list of Amenity instances with this Place """
        from models import storage
        amenities = []
        for amenity in storage.all("Amenity").values():
            if amenity.id in self.amenity_ids:
                amenities.append(amenity)
        return amenities

    @amenities.setter
    def amenities(self, obj=None):
        """ Appends amenity ids to the attribute """
        if type(obj) is Amenity and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)
