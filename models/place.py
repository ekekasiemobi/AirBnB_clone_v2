#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    if HBNB_TYPE_STORAGE == 'db':
        pass
    else:
        @property
        def reviews(self):
            """Getter attribute for reviews related to the current Place"""
            from models import storage
            reviews = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews
